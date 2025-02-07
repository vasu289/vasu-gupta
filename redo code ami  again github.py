import serial
import time
import random

# Establish a connection with the Arduino
arduino = serial.Serial('COM9', 9600, timeout=1)

def transmit_data():
    """Generate a random number and send it to the Arduino."""
    blink_cycles = random.randint(1, 5)  
    arduino.write(f"{blink_cycles}\n".encode())  
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] → Data sent: {blink_cycles}")
    return blink_cycles

def listen_for_reply():
    """Wait for a response from Arduino and process it."""
    while True:
        if arduino.in_waiting > 0:
            try:
                received_data = arduino.readline().decode().strip()  
                delay_duration = int(received_data)  
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ← Response received: {delay_duration}")
                
                time.sleep(delay_duration)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]  Sleeping for {delay_duration} seconds.")
                break  
            except ValueError:
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]  Invalid data received, retrying...")

def initiate_serial_communication():
    """Continuously exchange data with Arduino."""
    while True:
        transmit_data()  
        time.sleep(0.3)  # Slightly increased delay
        listen_for_reply()  

if _name_ == "_main_":
    initiate_serial_communication()