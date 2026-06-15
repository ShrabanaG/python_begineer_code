# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(cel:float) -> float:
    return (cel * 9 / 5) + 32

print(f"After conversion {convert_celsius_to_fahrenheit(32):.2f}")