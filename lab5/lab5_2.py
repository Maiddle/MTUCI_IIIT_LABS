class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):  
        self.radius = radius

while True:
    try:
        initial_radius = float(input('Enter the initial radius of the circle: '))
        if initial_radius > 0:
            break
        else:
            print('Radius must be a positive number.')
    except ValueError:
        print('Please enter a valid number for the radius.')
circle1 = Circle(initial_radius)

print(f'Initial radius: {circle1.get_radius()}')

while True:
    try:
        new_radius = float(input('Enter the new radius of the circle: '))
        if new_radius > 0:
            break
        else:
            print('Radius must be a positive number.')
    except ValueError:
        print('Please enter a valid number for the radius.')
circle1.set_radius(new_radius)
print(f'Updated radius: {circle1.get_radius()}')
