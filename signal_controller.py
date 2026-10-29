def get_signal_time(vehicle_count):

    if vehicle_count <= 10:
        density = "LOW"
        green_time = 15

    elif vehicle_count <= 20:
        density = "MEDIUM"
        green_time = 30

    else:
        density = "HIGH"
        green_time = 45

    return density, green_time