class Temperature:
    def __init__(self):
        pass
    
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

def temperature_calculator():
    temp = Temperature()
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = temp.convertFahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = temp.convertCelsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            print("Thank you for using the Temperature Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    temperature_calculator()2
    
