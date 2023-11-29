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

import multiprocessing
import time
import psutil
import threading

# Function to calculate the average for a range of numbers
def calculate_average(start, end, result, process_num):
    process_start_time = time.time()  # Record the start time for this process
    total = 0
    for number in range(start, end):
        total += number
    avg = total / (end - start)
    process_end_time = time.time()  # Record the end time for this process
    result.put((avg, process_end_time - process_start_time, process_num))

# Function to monitor CPU usage for each core
def monitor_cpu_usage():
    # Get CPU usage percentages for each core
    cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
    for core, usage in enumerate(cpu_percent_per_core):
        print(f"Core {core}: {usage}%")

if __name__ == "__main__":
    num_processes = 4  # Number of processes to use
    n = 1000000  # The upper limit
    segment_size = n // num_processes

    # Create a threading thread to monitor CPU usage
    monitor_thread = threading.Thread(target=monitor_cpu_usage)

    # Create a multiprocessing queue to collect results
    result_queue = multiprocessing.Queue()

    # Record the start time for the entire program
    start_time = time.time()

    # Create and start multiple processes
    processes = []

    for i in range(num_processes):
        start = i * segment_size + 1
        end = (i + 1) * segment_size + 1
        process = multiprocessing.Process(target=calculate_average, args=(start, end, result_queue, i))
        processes.append(process)
        process.start()

    # Start the monitoring thread
    monitor_thread.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Calculate the overall average and total execution time
    overall_total = 0
    process_execution_times = {}

    for _ in range(num_processes):
        avg, execution_time, process_num = result_queue.get()
        overall_total += avg
        process_execution_times[process_num] = execution_time

    overall_avg = overall_total / num_processes

    # Record the end time for the entire program
    end_time = time.time()

    # Print the overall average, total execution time, and execution time for each process
    print(f"The average of numbers from 1 to {n} is: {overall_avg}")
    print(f"Total execution time: {end_time - start_time:.4f} seconds")
    for process_num, execution_time in process_execution_times.items():
        print(f"Process {process_num} execution time: {execution_time:.4f} seconds")

    # Wait for the monitoring thread to complete
    monitor_thread.join()
