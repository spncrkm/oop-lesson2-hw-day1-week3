from dmv import Vehicle

if __name__ == "__main__":
    vehicle_one = Vehicle("GRV1234", "Minivan", "Spencer Kim")
    vehicle_two = Vehicle("VAC9876", "Motorcycle", "Emily Kim")

print("Original details:")
print("Vehicle 1 - Registration Number: ", vehicle_one.reg_num, "Type: ", vehicle_one.type, "Owner: ", vehicle_one.owner)
print("Vehicle 2 - Registration Number: ", vehicle_two.reg_num, "Type: ", vehicle_two.type, "Owner: ", vehicle_two.owner)

vehicle_one.update_owner("Alice Kim")

print("\nAfter updating owner of vehicle 1:")
print("Vehicle 1 - Registration Number: ", vehicle_one.reg_num, "Type: ", vehicle_one.type, "Owner: ", vehicle_one.owner)
print("Vehicle 2 - Registration Number: ", vehicle_two.reg_num, "Type: ", vehicle_two.type, "Owner: ", vehicle_two.owner)