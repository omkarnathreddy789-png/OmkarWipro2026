class Vehicle:
    # Class variable
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")


# Creating objects
v1 = Vehicle()
v2 = Vehicle()
v3 = Vehicle()

# Calling method
v1.start()

# Display vehicle count
print("Total vehicles created:", Vehicle.vehicle_count)
