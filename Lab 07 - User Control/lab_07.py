""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class UFO:
    def __init__(self, position_x, position_y, change_x, change_y):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    # First ufo object.
    def draw_ufo(self):
        x = self.position_x
        y = self.position_y
        arcade.draw_rectangle_filled(x, y, 60, 60, arcade.color.ASH_GREY)
        arcade.draw_arc_filled(x, y, 68, 78, arcade.color.ASH_GREY, 0, 180)
        arcade.draw_arc_filled(x, y, 90, 60, arcade.color.ASH_GREY, -90, 90)
        arcade.draw_arc_filled(x, y, 68, 78, arcade.color.ASH_GREY, -180, 0)
        arcade.draw_arc_filled(x, y, 90, 60, arcade.color.ASH_GREY, 90, 270)

class UFOB:
    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    # Second ufo object.
    def draw_ufob(self):
        x = self.position_x
        y = self.position_y
        arcade.draw_circle_filled(x, y + 10, 30, arcade.color.BLACK)
        arcade.draw_circle_filled(x, y + 40, 20, arcade.color.BLACK)
        arcade.draw_circle_filled(x, y + 60, 10, arcade.color.BLACK)
        arcade.draw_line(x, y, x + 40, y + 50, arcade.color.BLACK, 2)
        arcade.draw_line(x, y, x - 40, y + 50, arcade.color.BLACK, 2)

    # Keeping UFOB from leaving the screen.
    def update(self):

        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 30:
            self.position_x = 30

        if self.position_x > SCREEN_WIDTH - 30:
            self.position_x = SCREEN_WIDTH - 30

        if self.position_y < 20:
            self.position_y = 20

        if self.position_y > SCREEN_HEIGHT - 70:
            self.position_y = SCREEN_HEIGHT - 70

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        # Create the ufo
        self.ufo = UFO(1, 1, 0, 0)

        # Create the ufob
        self.ufob = UFOB(1, 1, 0, 0)

        self.set_mouse_visible(False)
        # Sounds
        self.laser_sound = arcade.load_sound("arcade_resources_sounds_laser2.wav")
        self.hit_wall_sound = arcade.load_sound("arcade_resources_sounds_jump4.wav")

    def on_draw(self):

        arcade.start_render()

        # Background
        arcade.draw_lrtb_rectangle_filled(0, 600, 600, 0, (48, 107, 255))
        # Fading night sky
        arcade.draw_ellipse_filled(300, 400, 1000, 500, (0, 43, 186), 0, -1)
        arcade.draw_ellipse_filled(300, 500, 1000, 500, (0, 57, 148), 0, -1)
        arcade.draw_ellipse_filled(300, 600, 1000, 500, (0, 40, 105), 0, -1)
        arcade.draw_ellipse_filled(300, 700, 1000, 500, (0, 27, 71), 0, -1)
        # Stars in blue third
        arcade.draw_circle_filled(10, 500, 5, arcade.color.WHITE)
        arcade.draw_circle_filled(590, 510, 4, arcade.color.WHITE)
        arcade.draw_circle_filled(567, 590, 3, arcade.color.WHITE)
        arcade.draw_circle_filled(500, 510, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(372, 580, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(400, 560, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(80, 580, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(340, 530, 4, arcade.color.WHITE)
        arcade.draw_circle_filled(35, 550, 4, arcade.color.WHITE)
        arcade.draw_circle_filled(444, 518, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(499, 520, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(520, 570, 3, arcade.color.WHITE)
        arcade.draw_circle_filled(489, 530, 4, arcade.color.WHITE)
        arcade.draw_circle_filled(514, 526, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(70, 550, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(90, 480, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(177, 533, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(114, 520, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(139, 570, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(146, 543, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(150, 520, 2, arcade.color.WHITE)
        arcade.draw_circle_filled(142, 535, 2, arcade.color.WHITE)
        # Shooting Stars
        arcade.draw_circle_filled(400, 270, 4, arcade.color.YELLOW)
        arcade.draw_line(400, 270, 300, 330, arcade.color.YELLOW, 3)
        arcade.draw_circle_filled(200, 220, 3, arcade.color.YELLOW)
        arcade.draw_line(200, 220, 100, 300, arcade.color.YELLOW, 2)
        arcade.draw_circle_filled(190, 370, 4, arcade.color.YELLOW)
        arcade.draw_line(190, 370, 90, 450, arcade.color.YELLOW, 3)
        # Clouds
        arcade.draw_arc_filled(30, 170, 200, 170, arcade.color.WHITE, -10, 180)
        arcade.draw_arc_filled(125, 140, 200, 170, arcade.color.WHITE, -10, 180)
        arcade.draw_arc_filled(570, 170, 200, 170, arcade.color.WHITE, -10, 180)
        arcade.draw_arc_filled(450, 130, 200, 190, arcade.color.WHITE, -10, 180)
        arcade.draw_arc_filled(300, 110, 200, 170, arcade.color.WHITE, -10, 180)
        arcade.draw_arc_filled(590, 230, 100, 70, arcade.color.WHITE, -10, 180)
        arcade.draw_lrtb_rectangle_filled(0, 600, 140, 0, (255, 255, 255))
        arcade.draw_lrtb_rectangle_filled(0, 100, 200, 0, (255, 255, 255))
        arcade.draw_lrtb_rectangle_filled(500, 600, 200, 0, (255, 255, 255))
        # Moon
        arcade.draw_circle_filled(300, 500, 90, (207, 226, 255))
        arcade.draw_circle_outline(300, 500, 100, (158, 196, 255), 2, 0, 0)

        self.ufo.draw_ufo()

        self.ufob.draw_ufob()

    def update(self, delta_time):
        self.ufob.update()

    # UFOB keyboard movement
    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.ufob.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ufob.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ufob.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ufob.change_y = -MOVEMENT_SPEED

        # Sound for UFOB hitting the borders.
        if self.ufob.position_x == SCREEN_WIDTH - 30:
            arcade.play_sound(self.hit_wall_sound)
        if self.ufob.position_x == 30:
            arcade.play_sound(self.hit_wall_sound)
        if self.ufob.position_y == SCREEN_HEIGHT - 70:
            arcade.play_sound(self.hit_wall_sound)
        if self.ufob.position_y == 20:
            arcade.play_sound(self.hit_wall_sound)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ufob.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ufob.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)

        self.ufo.draw_ufo()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ufo.position_x = x
        self.ufo.position_y = y

def main():
    window = MyGame()
    arcade.run()

main()