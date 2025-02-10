import pandas as pd
import matplotlib.pyplot as plt
import re 

file_path = r"D:\nanoarduinopython\adi.csv"
df = pd.read_csv(file_path)


df["Distance"] = df["Value"].str.extract(r"(\d+\.\d+)").astype(float)


df = df.dropna()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Distance"], linestyle="-", color="#4682B4", linewidth=2,  
         marker="o", markersize=3, markerfacecolor="black", markeredgewidth=0.5, label="Distance (cm)")  
plt.xlabel("Measurement Number")  
plt.ylabel("Distance (cm)")
plt.title("HC-SR04 Ultrasonic Sensor Distance Readings")
plt.legend()
plt.grid()

plt.show()
