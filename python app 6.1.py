import serial  # Import at the top

# Open the serial connection (change 'COM3' if needed)
ser = serial.Serial('COM3', 115200, timeout=1)  

# Open the CSV file for writing
with open("gyro_data.csv", "w") as f:
    f.write("Timestamp,X,Y,Z\n")  # Write header

    while True:
        try:
            # Read and decode a line from the serial port
            line = ser.readline().decode('utf-8').strip()

            # Ensure the line is not empty before writing
            if line:
                f.write(line + "\n")
                print(line)  # Print to console for debugging

        except KeyboardInterrupt:
            print("\nScript stopped by user.")
            break  # Exit loop on Ctrl+C

        except Exception as e:
            print(f"Error: {e}")