#-------------------------------------------------------------------------------
# Name:        module1
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

import threading
import time

# Function for each thread to calculate the average
def calculate_average(start, end, result, thread_num):
    total = 0
    for number in range(start, end):
        total += number
    avg = total / (end - start)
    result[thread_num] = avg
    print(f"Thread {thread_num} calculated the average in {time.time() - start_time:.4f} seconds")

# Define the number of threads and segments
num_threads = 5
n = 1000000
segment_size = n // num_threads

# Create a list to store thread objects
threads = []

# Create a list to store results
results = [0] * num_threads

# Record the start time
start_time = time.time()

# Create and start the threads
for i in range(num_threads):
    start = i * segment_size + 1
    end = (i + 1) * segment_size + 1
    thread = threading.Thread(target=calculate_average, args=(start, end, results, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Calculate the overall average
overall_avg = sum(results) / num_threads

# Record the end time
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

# Print the overall average and execution time
print(f"The average of numbers from 1 to {n} is: {overall_avg}")
print(f"Total execution time: {execution_time:.4f} seconds")


# Wait for the monitoring thread to complete
monitor_thread.join()
