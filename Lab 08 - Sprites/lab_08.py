""" Lab 8 Zombies """

import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_ZOMBIE = 0.5
SPRITE_SCALING_MOUSE = 0.25
SPRITE_SCALING_SAW = 0.18
MOUSE_COUNT = 50
SAW_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Mouse(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the mouse
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'.
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class Saw(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = random.randrange(SCREEN_WIDTH)
        self.circle_center_y = random.randrange(SCREEN_HEIGHT)

    def update(self):

        """ Update saw's position"""
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 Zombies")

        # Variables that hold sprite lists.
        self.zombie_list = None
        self.mouse_list = None
        self.saw_list = None

        # Set up the player information
        self.zombie_sprite = None
        self.score = 0

        # Don't show the mouse cursor.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        # Sound creation
        self.mouse_sound = arcade.load_sound("arcade_resources_sounds_rockHit2.wav")
        self.saw_sound = arcade.load_sound("arcade_resources_sounds_hurt1.wav")

    def setup(self):
        """ Set up game & initialize the variables. """

        # Sprite lists
        self.zombie_list = arcade.SpriteList()
        self.mouse_list = arcade.SpriteList()
        self.saw_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image
        self.zombie_sprite = arcade.Sprite("zombie_walk3.png", SPRITE_SCALING_ZOMBIE)
        self.zombie_sprite.center_x = 50
        self.zombie_sprite.center_y = 50
        self.zombie_list.append(self.zombie_sprite)

        # Create the mice.
        for i in range(MOUSE_COUNT):
            # Create the mouse instance.
            mouse = Mouse("mouse.png", SPRITE_SCALING_MOUSE)

            # Position the mouse.
            mouse.center_x = random.randrange(SCREEN_WIDTH)
            mouse.center_y = random.randrange(SCREEN_HEIGHT)
            mouse.change_x = random.randrange(-3, 4)
            mouse.change_y = random.randrange(-3, 4)

            # Add the mouse to the lists.
            self.mouse_list.append(mouse)

        # Create the saws.
        for i in range(SAW_COUNT):
            # Create the saw instance.
            saw = Saw("saw.png", SPRITE_SCALING_SAW)

            # Position the saw.
            saw.center_x = random.randrange(SCREEN_WIDTH)
            saw.center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200.
            saw.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi.
            saw.circle_angle = random.random() * 2 * math.pi

            # Add the saw to the lists.
            self.saw_list.append(saw)

    def on_draw(self):
        arcade.start_render()

        # Sprite lists here.
        self.mouse_list.draw()
        self.zombie_list.draw()
        self.saw_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)
        if len(self.mouse_list) == 0:
            gameover = f"GAME OVER."
            arcade.draw_text(gameover, 300, 300, arcade.color.YELLOW, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y.
        if len(self.mouse_list) > 0:
            self.zombie_sprite.center_x = x
            self.zombie_sprite.center_y = y

    def update(self, delta_time):
        """ Movement & game logic """

        if len(self.mouse_list) > 0:
            # Call update on all sprites.
            self.mouse_list.update()
            self.saw_list.update()

        # Generate a list of all sprites that collided with the zombie.
        mouse_hit_list = arcade.check_for_collision_with_list(self.zombie_sprite, self.mouse_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for mouse in mouse_hit_list:
            mouse.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.mouse_sound)

        saw_hit_list = arcade.check_for_collision_with_list(self.zombie_sprite, self.saw_list)
        for saw in saw_hit_list:
            saw.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.saw_sound)

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()