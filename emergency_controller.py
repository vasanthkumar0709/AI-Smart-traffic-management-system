def emergency_priority(vehicle_name):

    emergency_vehicles = [
        "ambulance",
        "fire_truck",
        "police"
    ]

    return vehicle_name.lower() in emergency_vehicles