"""
Bender vs Slurm
Survive the Slurm monsters and teleport out of there factory.
"""
import random
import arcade
import time

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

# Player health.
PLAYER_HEALTH = 100

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
        self.EXIT = 0

        # Track the current state o what key is pressed
        self.left_pressed = False
        self.right_pressed = False

        # Track the current state of what key is pressed.
        self.physics_engine = False
        self.physics_engine = False

        # Store our tile map.
        self.tile_map = None

        # Sound creation.
        self.key_sound = arcade.load_sound("arcade_resources_sounds_jump4.wav")
        self.key_sound2 = arcade.load_sound("arcade_resources_sounds_lose1.wav")
        self.key_sound3 = arcade.load_sound("arcade_resources_sounds_error4.wav")
        self.key_sound4 = arcade.load_sound("arcade_resources_sounds_hurt3.wav")

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

        # Set up the player
        self.player_sprite = arcade.Sprite("robot_idle.png",
                                           scale=0.45)
        self.player_sprite.center_x = 390
        self.player_sprite.center_y = 112
        self.player_list.append(self.player_sprite)
        self.player_sprite.health = PLAYER_HEALTH
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
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        if self.player_sprite.health < 100:
            self.player_sprite.health += 0.004

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

        # Purple enemies when hitting robot.
        purple_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.purple_list)

        for self.purple in purple_hit_list:
            self.player_sprite.health -= random.randrange(1, 2)
            arcade.play_sound(self.key_sound)

        # Green enemies when hitting robot.
        green_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.green_list)

        for self.green in green_hit_list:
            self.player_sprite.change_y = JUMP_SPEED * 0.6
            self.player_sprite.change_x = self.player_sprite.change_x + self.boss_sprite.change_x
            arcade.play_sound(self.key_sound3)

        jump_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.super_jump_list)

        for self.super_jump_sprite in jump_hit_list:
            self.player_sprite.change_y = SUPER_JUMP_SPEED
            arcade.play_sound(self.key_sound4)

        switch_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.switch_list)
        # Exit sign.
        for self.switch_sprite in switch_hit_list:
            self.switch_sprite.remove_from_sprite_lists()
            self.EXIT += 1

        boss_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.boss_list)

        # Boss damaging player.
        for self.boss_sprite in boss_hit_list:
            self.player_sprite.change_y = JUMP_SPEED*1.3
            self.player_sprite.change_x = self.player_sprite.change_x + self.boss_sprite.change_x * 2
            self.player_sprite.health -= random.randrange(5, 20)
            arcade.play_sound(self.key_sound2)
        # Scroll the screen to the player
        self.scroll_to_player()

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

        # Draw health.
        health = f"Robot battery percentage: ({self.player_sprite.health})"
        arcade.draw_text(health, 400, 10, arcade.color.BLACK, 20)

        # Game explanation.
        if self.player_sprite.center_y < 300 and self.player_sprite.center_x < 600:
            game_define = f"You, Bender, need to escape this dungeon before the"
            game_define2 = f"Slurm get to you! The pink slurm will take your battery"
            game_define3 = f"and the green slurm will limit your jumping ability."
            game_define4 = f"The green boss at the top will knock you around"
            game_define5 = f"and take your battery percentage down considerably."

            arcade.draw_text(game_define, 70, 400, arcade.color.BLACK, 20)
            arcade.draw_text(game_define2, 70, 350, arcade.color.BLACK, 20)
            arcade.draw_text(game_define3, 70, 300, arcade.color.BLACK, 20)
            arcade.draw_text(game_define4, 70, 250, arcade.color.BLACK, 20)
            arcade.draw_text(game_define5, 70, 200, arcade.color.BLACK, 20)

        # Exit sign
        if self.EXIT > 0:
            find_exit = f"You need to find the exit fast!"
            find_exit2 = f"Then you'll win the game!!"
            arcade.draw_text(find_exit, 200, 400, arcade.color.YELLOW, 25)
            arcade.draw_text(find_exit2, 200, 350, arcade.color.YELLOW, 25)
            self.exit_list.draw()
            exit_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.exit_list)
            game_over = 0

            for self.exit_sprite in exit_hit_list:
                game_over += 1

            frame = 0
            timer = 0
            if game_over > 0:
                gameover = f"You won the game."
                arcade.draw_text(gameover, 300, 300, arcade.color.RED, 25)
                timer += 1

                time.sleep(3)
            if timer == 1:
                frame += 2
            if frame > 2:
                exit()

        if self.player_sprite.health <= 0:
            gameover = f"GAME OVER."
            frame = 0
            timer = 0
            arcade.draw_text(gameover, 400, 400, arcade.color.BLUE_SAPPHIRE, 25)
            if timer == 1:
                frame += 2
            if frame > 2:
                exit()

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
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.player_sprite.change_x = 0

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