# Task 1: format() function
def format_example(a, b):
    result = format(a, b)
    return result

formatted_value = format_example(145, 'o')
print("Task 1")
print("Formatted result:", formatted_value)
print("Representation used: Octal (base 8)")

# Task 2: Area of circular pond + total water
radius = 84
pi = 3.14

area = pi * radius * radius
print("\nTask 2")
print("Area of the pond:", area, "square meters")

water_per_sq_meter = 1.4  
total_water = area * water_per_sq_meter

print("Total water in pond :", int(total_water))

# Task 3: Speed calculation
distance = 490  
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds

print("\nTask 3")
print("Speed in meters per second:", int(speed))
