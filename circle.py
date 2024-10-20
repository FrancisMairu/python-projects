import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

def circle_calculator():
    while True:
        print("\nCircle Calculator")
        print("1. Calculate area and circumference")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            try:
                radius = float(input("Enter the radius of the circle: "))
                if radius < 0:
                    print("Radius cannot be negative. Please enter a positive number.")
                    continue
                circle = Circle(radius)
                print(f"Area of the circle: {circle.area():.2f}")
                print(f"Circumference of the circle: {circle.circumference():.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            print("Thank you for using the Circle Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    circle_calculator()