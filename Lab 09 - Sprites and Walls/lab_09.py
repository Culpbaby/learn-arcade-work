"""
Scroll around a large screen.
If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves.
PLAYER_MOVEMENT_SPEED = 11

# Number of keys.
SPRITE_SCALING_KEY = 0.5
KEY_COUNT = 50

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.key_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        # Sound Creation.
        self.key_sound = arcade.load_sound("arcade_resources_sounds_coin4.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("robot_walk0.png",
                                           scale=0.45)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        """Place walls with a loop."""
        # Bottom row of brown bricks.
        for x in range(0, 1400, 64):
            wall = arcade.Sprite("brickBrown.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)
        # Right column of brown bricks.
        for y in range(300, 1400, 64):
            wall = arcade.Sprite("brickBrown.png", SPRITE_SCALING)
            wall.center_x = 1405
            wall.center_y = y
            self.wall_list.append(wall)
        # Top row of brown bricks.
        for z in range(0, 1400, 64):
            wall = arcade.Sprite("brickBrown.png", SPRITE_SCALING)
            wall.center_x = z
            wall.center_y = 1388
            self.wall_list.append(wall)
        # Left column if brown bricks.
        for w in range(300, 1400, 64):
            wall = arcade.Sprite("brickBrown.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = w
            self.wall_list.append(wall)

        """Inside walls."""
        def square_walls(x, y):
            coordinate_list = [[326 + x, 431 + y],
                               [390 + x, 431 + y],
                               [326 + x, 495 + y],
                               [390 + x, 495 + y]]
            # Loop through coordinates
            for coordinate in coordinate_list:
                wall = arcade.Sprite("stoneCenter_rounded.png", SPRITE_SCALING)
                wall.center_x = coordinate[0]
                wall.center_y = coordinate[1]
                self.wall_list.append(wall)

        def horizontal_walls(x, y, z):
            for a in range(70 + x, 400 + z, 64):
                wall = arcade.Sprite("stoneCenter_rounded.png", SPRITE_SCALING)
                wall.center_x = a
                wall.center_y = 621 + y
                self.wall_list.append(wall)

        def vertical_walls(x, y, z):
            for b in range(366 + y, 800 + z, 64):
                wall = arcade.Sprite("stoneCenter_rounded.png", SPRITE_SCALING)
                wall.center_x = 513 + x
                wall.center_y = b
                self.wall_list.append(wall)

        # Sqaures.
        square_walls(-5, 0)
        square_walls(-187, 0)
        square_walls(886, 767)
        square_walls(886, 575)
        square_walls(250, 320)
        square_walls(568, 254)
        square_walls(760, 254)
        square_walls(694, 767)

        # Horizontals.
        horizontal_walls(-5, 0, 0)
        horizontal_walls(566, 0, 920)
        horizontal_walls(59, 320, 336)
        horizontal_walls(-6, 448, 272)
        horizontal_walls(59, 576, 336)
        horizontal_walls(-6, 704, 272)
        horizontal_walls(952, 254, 920)


        # Verticals.
        vertical_walls(0, 0, 64)
        vertical_walls(128, 64, -256)
        vertical_walls(256, 64, -256)
        vertical_walls(384, 0, -192)
        vertical_walls(512, 64, -256)
        vertical_walls(576, 0, -384)
        vertical_walls(832, 0, -384)
        vertical_walls(640, 64, -256)
        vertical_walls(768, 64, -256)
        vertical_walls(256, 384, 480)
        vertical_walls(-128, 384, 128)
        vertical_walls(-256, 384, 64)
        vertical_walls(-384, 318, 64)
        vertical_walls(384, 512, 544)
        vertical_walls(764, 318, 40)
        vertical_walls(510, 574, 328)
        vertical_walls(638, 574, 395)


        # Create the Keys.
        for i in range(KEY_COUNT):
            # Create the key instance
            key = arcade.Sprite("keyBlue.png", SPRITE_SCALING_KEY)

            # Boolean variable if we succesfully placed the key.
            key_placed_successfully = False

            # Keep trying until success.
            while not key_placed_successfully:
                # Position the key
                key.center_x = random.randrange(0, 1400)
                key.center_y = random.randrange(300, 1400)

                # See if the key is hitting a wall.
                wall_hit_list = arcade.check_for_collision_with_list(key, self.wall_list)

                # See if the key is hitting another coin.
                key_hit_list = arcade.check_for_collision_with_list(key, self.key_list)

                if len(wall_hit_list) == 0 and len(key_hit_list) == 0:
                    # It is!
                    key_placed_successfully = True

            # Add the key to the lists.
            self.key_list.append(key)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.YELLOW)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.key_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 14)
        if len(self.key_list) == 0:
            gameover = f"GAME OVER."
            arcade.draw_text(gameover, 400, 400, arcade.color.BLUE_SAPPHIRE, 25)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        key_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.key_list)

        for key in key_hit_list:
            key.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.key_sound)

        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()
        self.key_list.update()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.

        Anything between 0 and 1 will have the camera move to the location with a smoother

        pan.
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