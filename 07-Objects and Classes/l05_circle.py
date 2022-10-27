class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.diameter * self.__pi

    def calculate_area(self):
        return (self.diameter / 2) ** 2 * self.__pi

    def calculate_area_of_sector(self, area_angle):
        angle_in_rad = (area_angle * self.__pi) / 180
        return ((self.diameter / 2) ** 2) * (angle_in_rad / 2)


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

