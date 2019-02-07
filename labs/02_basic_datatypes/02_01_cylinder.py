'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.

    '''


# Cylinder volume = π r² h
# Cylinder surface area = 2π r h + 2π r²
def cylinder_volume_surface(radius, height):
    volume = float((3.14 * radius ** 2 * height))
    surface = float((2 * 3.14 * height) + (2 * 3.14) * radius ** 2)
    print(f'\n The volume of a cylinder with a radius of 3.14 and a height of 5 is %.2f' % volume)
    print(f'\n The surface area of a cylinder with a radius of 3.14 and the height of 5 is %.2f' % surface)


cylinder_volume_surface(3.14, 5)


    

