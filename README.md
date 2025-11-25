# Environmental-Health-Station-using-Raspberry-Pi-Pico
IoT Environmental Health Station using Raspberry Pi Pico with gas and DHT sensors. Displays real-time air quality, temperature, and humidity on an OLED screen. Sends data to ThingSpeak cloud for remote monitoring and triggers buzzer alerts for unsafe conditions. Programmed in MicroPython via Thonny IDE
Problem Statement
Design an environmental monitoring station that measures air quality and environmental parameters using gas and DHT sensors. Display real-time data on an I2C OLED screen and generate buzzer alerts upon detecting poor air quality or adverse conditions. Send sensor data to a cloud platform (ThingSpeak) for remote monitoring and analytics to support campus wellness.

Scope of the Solution
Measure air quality (gas sensor) and environmental parameters (temperature, humidity from DHT sensor).

Display data live on the OLED display.

Trigger buzzer alerts when sensor readings exceed safe limits.

Send sensor data to ThingSpeak for remote visualization and data logging.

Access dashboard remotely for campus safety monitoring.

Required Components
Hardware:

Raspberry Pi Pico microcontroller

MQ-series gas sensor (such as MQ-2 or MQ-135) for air quality

DHT11 or DHT22 sensor for temperature and humidity

0.96 inch I2C OLED Display (SSD1306 driver)

Buzzer (active or passive)

Connecting wires, breadboard, power supply

Software:

Thonny IDE for MicroPython code development and uploading

MicroPython firmware flashed on Pico

ThingSpeak account for IoT dashboard and data logging
