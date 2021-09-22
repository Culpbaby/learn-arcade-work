"""
Lab 2 Moon
"""
import arcade

arcade.open_window(600, 600, "Thor")

arcade.start_render()
# Background of f
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


arcade.finish_render()
arcade.run()