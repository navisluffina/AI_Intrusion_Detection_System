# AI-Based Intrusion Detection System

## Overview

This project is a real-time AI-powered intrusion detection system built using Python, OpenCV, and YOLOv8. The system uses a webcam feed to detect human presence and automatically triggers alerts when an intrusion is detected.

The application performs:

* Real-time person detection
* Intrusion alert generation
* Automatic evidence image saving
* Live bounding box visualization
* Confidence-based object detection

The project demonstrates practical applications of computer vision and AI in surveillance and security systems.

---

# Features

* Real-time webcam monitoring
* YOLOv8-based person detection
* Automatic intrusion alerts
* Saves frames only when intrusion is detected
* Bounding box visualization
* Confidence score display
* Lightweight and fast implementation
* Easy to extend with advanced security features

---

# Technologies Used

* Python
* OpenCV
* YOLOv8
* Ultralytics
* NumPy

---

# Project Structure

```text
intrusion_project/
│
├── outputs/
│   └── intrusion images
│
├── main.py
├── intrusion.py
├── detector.py
├── utils.py
├── config.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/navisluffina/intrusion-detection-system.git
```

## Open Project Folder

```bash
cd intrusion_project
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python main.py
```

The webcam will open automatically.

When a person is detected:

* An alert is displayed
* Bounding boxes are drawn
* Intrusion frames are saved inside the `outputs/` folder

Press:

```text
q
```

to quit the application.

---

# Sample Output

The system displays:

* Person detection boxes
* Confidence scores
* Intrusion status
* Number of people detected

Example:

```text
Status: ALERT
People: 1
```

---

# Future Improvements

* Email alert system
* SMS/Telegram notifications
* Face recognition integration
* Motion tracking
* Restricted zone intrusion detection
* Video recording during alerts
* Low-light enhancement integration

---

# Applications

* Smart surveillance systems
* Home security
* Restricted area monitoring
* Office intrusion detection
* Industrial safety monitoring

---

# Author

Navis Luffina

---

# License

This project is for educational and research purposes.
