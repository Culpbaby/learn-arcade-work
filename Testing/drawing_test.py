def volume_cylinder(radius, height):
    pi = 3.141592653
    volume = pi * radius ** 2 * height
    return volume
my_volume = volume_cylinder(2.5, 5) * 6
print(my_volume)