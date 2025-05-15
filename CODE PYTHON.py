import serial
import time
import csv

# ===== CONFIGURATION =====
PORT = 'COM3'
BAUD_RATE = 9600
CSV_FILENAME = 'ldr_readings.csv'
LOG_DURATION = 3600

# ===== CONNECT TO ARDUINO =====
try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"[INFO] Connected to Arduino on {PORT}")
except Exception as e:
    print(f"[ERROR] Connection error: {e}")
    exit()

# ===== OPEN CSV FILE =====
with open(CSV_FILENAME, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Milliseconds", "LightValue"])

    print(f"[INFO] Logging data to '{CSV_FILENAME}' for {LOG_DURATION} seconds...")
    start_time = time.time()

    while time.time() - start_time < LOG_DURATION:
        try:
            line = arduino.readline().decode('utf-8', errors='ignore').strip()
            if ',' in line:
                millis, light = line.split(',')
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([timestamp, millis.strip(), light.strip()])
                print(f"{timestamp}, {millis.strip()}, {light.strip()}")
        except Exception as e:
            print(f"[WARNING] Error: {e}")
            continue

# ===== DONE =====
arduino.close()
print(f"[INFO] Logging complete. File saved as '{CSV_FILENAME}'")
