import matplotlib.pyplot as plt
import datetime

# Read data from the CSV file
data = []
with open('totals.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            time_str, _, second_str = line.split(',')
            time = datetime.datetime.strptime(time_str, '%m/%d/%Y %H:%M:%S').time()
            second = int(second_str)
            data.append((time, second))

# Extract time and second values
times = [d[0] for d in data]
seconds = [d[1] for d in data]

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(range(len(times)), seconds, color='pink')

# Customize the plot
plt.xlabel('Time')
plt.ylabel('Number of Cars')
plt.title('Number of Cars vs. Time')

# Format the x-axis labels
plt.xticks(range(len(times)), [t.strftime('%H:%M:%S') for t in times], rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
