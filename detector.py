import cv2
import json
from ultralytics import YOLO
from signal_controller import get_signal_time

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Vehicle classes
vehicle_classes = [
    "car",
    "motorcycle",
    "bus",
    "truck"
]

# Video source
cap = cv2.VideoCapture("videos/traffic.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, verbose=False)

    total = 0
    car_count = 0
    bike_count = 0
    bus_count = 0
    truck_count = 0

    emergency_detected = False
    emergency_vehicle = "None"

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])
            label = model.names[cls]

            # Vehicle counting

            if label == "car":
                car_count += 1
                total += 1

            elif label == "motorcycle":
                bike_count += 1
                total += 1

            elif label == "bus":
                bus_count += 1
                total += 1

            elif label == "truck":
                truck_count += 1
                total += 1

            # Demo mode
            # Treat buses as ambulances

            if label == "bus":
                emergency_detected = True
                emergency_vehicle = "Ambulance"

            # Draw rectangles

            if label in vehicle_classes:

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Signal control

    if emergency_detected:
        density = "EMERGENCY"
        green_time = 120
    else:
        density, green_time = get_signal_time(total)

    # Store data

    data = {
        "total": total,
        "cars": car_count,
        "bikes": bike_count,
        "buses": bus_count,
        "trucks": truck_count,
        "density": density,
        "green_time": green_time,
        "emergency": emergency_detected,
        "vehicle": emergency_vehicle
    }

    with open(
        "data/traffic_data.json",
        "w"
    ) as file:

        json.dump(data, file, indent=4)

    # Information panel

    cv2.rectangle(
        frame,
        (10, 10),
        (420, 300),
        (0, 0, 0),
        -1
    )

    cv2.putText(
        frame,
        f"Total Vehicles: {total}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Density: {density}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Green Signal: {green_time} sec",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Cars: {car_count}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Bikes: {bike_count}",
        (20, 190),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Buses: {bus_count}",
        (20, 220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Trucks: {truck_count}",
        (20, 250),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    if emergency_detected:

        cv2.putText(
            frame,
            "EMERGENCY VEHICLE DETECTED",
            (20, 280),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    cv2.imshow(
        "AI Traffic Management System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()