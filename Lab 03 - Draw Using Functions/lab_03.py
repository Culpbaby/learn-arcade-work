""" Lab 3 - Clouds & Moons """
import arcade

def draw_skyline():
    """Draw the skyline"""
    arcade.draw_ellipse_filled(300, 400, 1000, 500, (0, 43, 186), 0, -1)
    arcade.draw_ellipse_filled(300, 500, 1000, 500, (0, 57, 148), 0, -1)
    arcade.draw_ellipse_filled(300, 600, 1000, 500, (0, 40, 105), 0, -1)
    arcade.draw_ellipse_filled(300, 700, 1000, 500, (0, 27, 71), 0, -1)

def draw_cloud(x, y):
    """Draw a cloud"""
    arcade.draw_rectangle_filled(290+ x, 240 + y, 60, 60, (255, 255, 255))
    arcade.draw_arc_filled(290 + x, 250 + y, 68, 78, arcade.color.WHITE, 0, 180)
    arcade.draw_arc_filled(300 + x, 240 + y, 90, 60, arcade.color.WHITE, -90, 90)
    arcade.draw_arc_filled(290 + x, 230 + y, 68, 78, arcade.color.WHITE, -180, 0)
    arcade.draw_arc_filled(280 + x, 240 + y, 90, 60, arcade.color.WHITE, 90, 270)

def draw_moon():
    """draw a moon"""
    arcade.draw_circle_filled(300, 500, 90, (207, 226, 255))
    """draw the glow"""
    arcade.draw_circle_outline(300, 500, 92, (158, 196, 255), 1, 0, 0)
    arcade.draw_circle_outline(300, 500, 94, (158, 196, 255), 1, 0, 0)
    arcade.draw_circle_outline(300, 500, 96, (158, 196, 255), 1, 0, 0)

def draw_stars(x, y):
    """draw the stars"""
    arcade.draw_circle_filled(590 + x, 510 + y, 4, arcade.color.WHITE)
    arcade.draw_circle_filled(567 + x, 590 + y, 3, arcade.color.WHITE)
    arcade.draw_circle_filled(500 + x, 510 + y, 2, arcade.color.WHITE)
    arcade.draw_circle_filled(372 + x, 580 + y, 2, arcade.color.WHITE)
    arcade.draw_circle_filled(400 + x, 560 + y, 2, arcade.color.WHITE)
    arcade.draw_circle_filled(444 + x, 518 + y, 2, arcade.color.WHITE)
    arcade.draw_circle_filled(499 + x, 520 + y, 2, arcade.color.WHITE)
    arcade.draw_circle_filled(520 + x, 570 + y, 3, arcade.color.WHITE)
    arcade.draw_circle_filled(489 + x, 530 + y, 4, arcade.color.WHITE)
    arcade.draw_circle_filled(514 + x, 526 + y, 2, arcade.color.WHITE)

def draw_shooting_star(x, y, z):
    """Shooting star"""
    arcade.draw_triangle_filled(396 + x, 268 + y, 404 + x, 274 + y, 406 + x, 268 + y, arcade.color.YELLOW)
    arcade.draw_line(400 + x, 270 + y, 300 + x, 330 + y, arcade.color.YELLOW, 3 + z)
    arcade.draw_line(401 + x, 271 + y, 301 + x, 331 + y, arcade.color.YELLOW, 2 + z)

def main():
    arcade.open_window(600, 600, "Moons")
    arcade.draw_lrtb_rectangle_filled(0, 600, 600, 0, (48, 107, 255))
    arcade.start_render()

    draw_skyline()

    draw_cloud(0, 0)
    draw_cloud(-90, -100)
    draw_cloud(-200, 150)
    draw_cloud(100, -130)
    draw_cloud(-210, -120)
    draw_cloud(-170, 0)

    draw_stars(0, 0)
    draw_stars(-350, 0)

    draw_moon()

    draw_shooting_star(0, 0, 0)
    draw_shooting_star(70, 50, -1)
    draw_shooting_star(110, -40, 0)
    draw_shooting_star(123, 80, 3)

    arcade.finish_render()
    arcade.run()


main()

