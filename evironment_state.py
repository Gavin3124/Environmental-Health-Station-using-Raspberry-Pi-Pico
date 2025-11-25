from machine import Pin, ADC, I2C
import ssd1306
import dht
import network
import urequests
import time

# WiFi and ThingSpeak credentials
SSID = 'your_wifi_ssid'
PASSWORD = 'your_wifi_password'
THINGSPEAK_API_KEY = 'your_thingspeak_write_api_key'

# Initialize I2C for OLED (GPIO 4 = SDA, GPIO 5 = SCL)
i2c = I2C(0, scl=Pin(5), sda=Pin(4))

# Initialize OLED display (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize DHT11 sensor on GPIO15
dht_sensor = dht.DHT11(Pin(15))

# Initialize gas sensor on ADC0 (GPIO26)
gas_sensor = ADC(26)

# Initialize buzzer on GPIO14
buzzer = Pin(14, Pin.OUT)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print('Connected with IP:', wlan.ifconfig()[0])
    return wlan

def read_sensors():
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    gas_val = gas_sensor.read_u16()
    return temp, hum, gas_val

def update_oled(temp, hum, gas):
    oled.fill(0)
    oled.text('Env Health Station', 0, 0)
    oled.text(f'Temp: {temp} C', 0, 16)
    oled.text(f'Hum: {hum} %', 0, 32)
    oled.text(f'Gas: {gas}', 0, 48)
    oled.show()

def alert_check(temp, hum, gas):
    buzzer.value(0)  # Turn buzzer off initially
    # Thresholds for alerts (adjust based on calibration)
    if gas > 30000 or temp > 35 or temp < 10 or hum > 80 or hum < 20:
        buzzer.value(1)  # Turn buzzer on
    else:
        buzzer.value(0)  # Keep buzzer off

def upload_to_thingspeak(temp, hum, gas):
    url = f'https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}&field1={temp}&field2={hum}&field3={gas}'
    try:
        response = urequests.get(url)
        response.close()
        print('Uploaded data to ThingSpeak.')
    except:
        print('Failed to upload data.')

def main():
    connect_wifi()
    while True:
        temp, hum, gas = read_sensors()
        update_oled(temp, hum, gas)
        alert_check(temp, hum, gas)
        upload_to_thingspeak(temp, hum, gas)
        time.sleep(15)  # Wait 15 seconds between readings (ThingSpeak limit)

if __name__ == '__main__':
    main()
