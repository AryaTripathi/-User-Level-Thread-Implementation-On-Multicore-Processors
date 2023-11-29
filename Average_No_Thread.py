#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Arya Tripathi
#
# Created:     05-11-2023
# Copyright:   (c) Arya Tripathi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import psutil
import threading

# Function to monitor CPU usage for each core
def monitor_cpu_usage():
    # Get CPU usage percentages for each core
    cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
    for core, usage in enumerate(cpu_percent_per_core):
        print(f"Core {core}: {usage}%")

# Start monitoring CPU usage before your main code
monitor_thread = threading.Thread(target=monitor_cpu_usage)
monitor_thread.start()

import time

# Calculate the average of numbers from 1 to 1,000,000
n = 1000000  # The upper limit
total = 0

# Record the start time
start_time = time.time()

# Sum all numbers from 1 to n
for number in range(1, n + 1):
    total += number

# Calculate the average
average = total / n

# Record the end time
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

print(f"The average of numbers from 1 to {n} is: {average}")
print(f"Execution time: {execution_time:.4f} seconds")


# Wait for the monitoring thread to complete
monitor_thread.join()





