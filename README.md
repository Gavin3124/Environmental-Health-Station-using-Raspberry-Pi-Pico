# Environmental-Health-Station-using-Raspberry-Pi-Pico
IoT Environmental Health Station using Raspberry Pi Pico with gas and DHT sensors. Displays real-time air quality, temperature, and humidity on an OLED screen. Sends data to ThingSpeak cloud for remote monitoring and triggers buzzer alerts for unsafe conditions. Programmed in MicroPython via Thonny IDE
Problem Statement
Design an environmental monitoring station that measures air quality and environmental parameters using gas and DHT sensors. Display real-time data on an I2C OLED screen and generate buzzer alerts upon detecting poor air quality or adverse conditions. Send sensor data to a cloud platform (ThingSpeak) for remote monitoring and analytics to support campus wellness.

# Scope of the Solution
Measure air quality (gas sensor) and environmental parameters (temperature, humidity from DHT sensor).
Display data live on the OLED display.
Trigger buzzer alerts when sensor readings exceed safe limits.
Send sensor data to ThingSpeak for remote visualization and data logging.
Access dashboard remotely for campus safety monitoring.

# Required Components
Hardware:
- Raspberry Pi Pico microcontroller
- MQ-series gas sensor (such as MQ-2 or MQ-135) for air quality
- DHT11 or DHT22 sensor for temperature and humidity
- 0.96 inch I2C OLED Display (SSD1306 driver)
- Buzzer (active or passive)
- Connecting wires, breadboard, power supply

Software:
- Thonny IDE for MicroPython code development and uploading
- MicroPython firmware flashed on Pico
- ThingSpeak account for IoT dashboard and data logging


## code logic implementation

The code logic implementation for your IoT Environmental Health Station follows these steps:

- Initialization: The program begins by importing required libraries and initializing hardware components—the I2C OLED display, DHT temperature and humidity sensor, gas sensor (connected to ADC), and buzzer. It also sets up the WiFi credentials and ThingSpeak API key.

- WiFi Connection: The function connect_wifi() activates the device’s WiFi interface and attempts to connect to the specified network. It loops until connected and then prints the assigned IP address.

- Sensor Reading: The read_sensors() function triggers the DHT sensor to measure temperature and humidity, reads the analog value from the gas sensor, and returns these values for further processing.

- Display Update: The update_oled() function clears the OLED screen and displays the latest temperature, humidity, and gas sensor readings in a readable text format.

- Alerts: The alert_check() function compares sensor readings against pre-defined safe thresholds (e.g., temperature range, humidity limits, and gas concentration). If any reading exceeds limits, the buzzer is activated as an alert; otherwise, it remains off.

- Cloud Upload: The upload_to_thingspeak() function formats the sensor data into HTTP GET parameters and sends this to the ThingSpeak server, enabling remote monitoring and analytics through the ThingSpeak dashboard.

- Looping: The main() function starts by connecting to WiFi, then enters an infinite loop where it continuously takes sensor readings, updates the OLED display, checks and triggers alerts, uploads data to ThingSpeak, and waits 15 seconds before repeating. The 15-second interval respects ThingSpeak’s update rate limits.
