"""
Bender vs Slurm
Survive the Slurm monsters and teleport out of there factory.
"""
import random
import arcade

TILE_SCALING = 0.9
GRID_PIXEL_SIZE = 128
GRAVITY = 0.50

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Slurm Factory"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves.
PLAYER_MOVEMENT_SPEED = 7
JUMP_SPEED = 11
SUPER_JUMP_SPEED = 22

# Number of Enemies
SPRITE_SCALING_SLIME = 0.5
purple_count = 15
green_count = 15

class Purple(arcade.Sprite):
    def __init__(self,filename, scale):
        super().__init__(filename, scale)
        self.physics_engine = None

        self.change_x = None
        self.change_y = 0
        self.frame = 0
        self.center_y = None

    def update(self):
        self.frame += random.randrange(-2, 2)
        if self.frame > 100:
            self.change_x *= -1
            self.frame = 0
        if self.frame < -100:
            self.change_x *= -1
            self.frame = 0
        if self.center_y < 200:
            self.center_x = random.randrange(0, 1750)
            self.center_y = random.randrange(300, 1750)

class Green(arcade.Sprite):
    def __init__(self,filename, scale):
        super().__init__(filename, scale)
        self.physics_engine = None

        self.change_x = None
        self.change_y = 0
        self.frame = 0
        self.center_y = None

    def update(self):
        self.frame += random.randrange(-2, 2)
        if self.frame > 100:
            self.change_x *= -1
            self.frame = 0
        if self.frame < -100:
            self.change_x *= -1
            self.frame = 0
        if self.center_y < 200:
            self.center_x = random.randrange(0, 1750)
            self.center_y = random.randrange(300, 1750)


class Boss(arcade.Sprite):
    def __init__(self,filename, scale):
        super().__init__(filename, scale)
        self.physics_engine = None

        self.change_x = 0
        self.change_y = 0
    def update(self):

        # Move the Boss.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If Boss reaches the edge.
        if self.center_x < 330:
            self.change_x *= -1

        if self.center_x > 1450:
            self.change_x *= -1

# Create all the other stuff first then as k for help with the sprites.

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists.
        self.player_list = None
        self.wall_list = None
        self.boss_list = None
        self.green_list = None
        self.purple_list = None
        self.switch_list = None
        self.switch_pressed_list = None
        self.exit_list = None
        self.super_jump_list = None

        # Set up the player.
        self.player_sprite = None
        self.boss_sprite = None
        self.switch_sprite = None
        self.switch_pressed_sprite = None
        self.super_jump_sprite = None
        self.exit_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state o what key is pressed
        self.left_pressed = False
        self.right_pressed = False

        # Track the current state of what key is pressed.
        self.physics_engine = False
        self.physics_engine = False

        # Store our tile map.
        self.tile_map = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.boss_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.purple_list = arcade.SpriteList()
        self.green_list = arcade.SpriteList()
        self.switch_list = arcade.SpriteList()
        self.switch_pressed_list = arcade.SpriteList()
        self.super_jump_list = arcade.SpriteList()
        self.exit_list = arcade.SpriteList()

        # Score

        # Set up the player
        self.player_sprite = arcade.Sprite("robot_idle.png",
                                           scale=0.45)
        self.player_sprite.center_x = 1390
        self.player_sprite.center_y = 1812
        self.player_list.append(self.player_sprite)

        # Set up the super jump.
        self.super_jump_sprite = arcade.Sprite("switchGreen.png", scale=0.63)
        self.super_jump_sprite.center_x = 1550
        self.super_jump_sprite.center_y = 155
        self.super_jump_list.append(self.super_jump_sprite)

        """ Load our map."""
        # read in tiled map.
        map_name = "Game_layout.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=TILE_SCALING)

        self.wall_list = self.tile_map.sprite_lists["Walls"]

        # Set up the boss
        self.boss_sprite = Boss("slimeBlock.png", scale=1.25)
        self.boss_sprite.center_x = 1350
        self.boss_sprite.center_y = 1812
        self.boss_sprite.change_x = random.randrange(-3, -2)
        self.boss_list.append(self.boss_sprite)
        # Keep player from running through the wall_list layer.
        self.boss_sprite.physics_engine = arcade.PhysicsEnginePlatformer(self.boss_sprite, self.wall_list,
                                                                         gravity_constant=GRAVITY)
        # Set up the button to exit.
        self.switch_sprite = arcade.Sprite("switchRed.png", scale=0.33)
        self.switch_sprite.center_x = 950
        self.switch_sprite.center_y = 1748
        self.switch_list.append(self.switch_sprite)

        self.switch_pressed_sprite = arcade.Sprite("switchRed_pressed.png", scale=0.33)
        self.switch_pressed_sprite.center_x = 950
        self.switch_pressed_sprite.center_y = 1748
        self.switch_pressed_list.append(self.switch_pressed_sprite)

        self.exit_sprite = arcade.Sprite("signExit.png", scale=.63)
        self.exit_sprite.center_x = 1700
        self.exit_sprite.center_y = 155
        self.exit_list.append(self.exit_sprite)

        # Set the background color
        arcade.set_background_color((3, 211, 252))

        # Keep player from running through the wall_list layer.
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)

        for i in range(purple_count):
            self.purple = Purple("slimePurple.png", SPRITE_SCALING_SLIME)

            # Boolean variable if the key is succesfully placed.
            purple_placed_successfully = False

            # Keep trying until it works.
            while not purple_placed_successfully:
                # Position the purple enemy.
                self.purple.center_x = random.randrange(0, 1750)
                self.purple.center_y = random.randrange(300, 1750)

                # If it is hitting a wall.
                # See if the key is hitting a wall.
                wall_hit_list = arcade.check_for_collision_with_list(self.purple, self.wall_list)

                # See if purple is hitting another purple.
                purple_hit_list = arcade.check_for_collision_with_list(self.purple, self.purple_list)

                if len(wall_hit_list) == 0 and len(purple_hit_list) == 0:
                    purple_placed_successfully = True
                    self.purple.change_x = random.randrange(-5, 5)
                    if self.purple.center_y < 200:
                        purple_placed_successfully = False

                    # Add the purple to the lists.
                    self.purple_list.append(self.purple)

                self.purple.physics_engine = arcade.PhysicsEnginePlatformer(self.purple, self.wall_list,
                                                                     gravity_constant=GRAVITY)
        # Set up the green enemies.
        for i in range(green_count):
            self.green = Green("slimeGreen.png", SPRITE_SCALING_SLIME)

            # Boolean variable if the key is succesfully placed.
            green_placed_successfully = False

            # Keep trying until it works.
            while not green_placed_successfully:
                # Position the purple enemy.
                self.green.center_x = random.randrange(0, 1750)
                self.green.center_y = random.randrange(300, 1750)


                # If it is hitting a wall.
                # See if the key is hitting a wall.
                wall_hit_list = arcade.check_for_collision_with_list(self.green, self.wall_list)

                # See if purple is hitting another purple.
                green_hit_list = arcade.check_for_collision_with_list(self.green, self.purple_list)

                if len(wall_hit_list) == 0 and len(green_hit_list) == 0:
                    green_placed_successfully = True
                    self.green.change_x = random.randrange(-5, 5)
                    if self.green.center_y < 200:
                        green_placed_successfully = False

                    # Add the green to the lists.
                    self.green_list.append(self.green)

                self.green.physics_engine = arcade.PhysicsEnginePlatformer(self.green, self.wall_list,
                                                                     gravity_constant=GRAVITY)


    def on_draw(self):
        """ Render the screen."""

        arcade.start_render()

        # Camera I'm using to draw all of my sprites.
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.purple_list.draw()
        self.boss_list.draw()
        self.switch_pressed_list.draw()
        self.switch_list.draw()
        self.green_list.draw()
        self.super_jump_list.draw()
        self.exit_list.draw()



        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
        self.boss_sprite.update()
        self.physics_engine.update()
        self.boss_sprite.physics_engine.update()
        for purple in self.purple_list:
            purple.physics_engine.update()
            purple.update()

        for green in self.green_list:
            green.physics_engine.update()
            green.update()

        jump_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.super_jump_list)

        for self.super_jump_sprite in jump_hit_list:
            self.player_sprite.change_y = SUPER_JUMP_SPEED

        switch_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.switch_list)

        for self.switch_sprite in switch_hit_list:
            self.switch_sprite.remove_from_sprite_lists()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a
        smoother pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()