def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.1f}°C")
    return celsius

celsius_to_fahrenheit(33)
celsius_to_fahrenheit(22)

fahrenheit_to_celsius(75)
fahrenheit_to_celsius(100)