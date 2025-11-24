from collections import deque
import random

class Process:
    def __init__(self, pid, burst_time):
        # Fixed: Removed the random '3' that was causing a syntax error
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        print(f"Process {self.pid} created with burst time {self.burst_time}ms.")

    def run(self, quantum):
        if self.remaining_time > quantum:
            self.remaining_time -= quantum
            print(f"Process {self.pid} ran for {quantum}ms. Left: {self.remaining_time}ms.")
            return True  # Process is still pending
        else:
            time_ran = self.remaining_time
            self.remaining_time = 0
            print(f"Process {self.pid} ran for {time_ran}ms. Completed.")
            return False # Process is finished

def round_robin_scheduling(processes, quantum):
    # Fixed: Variable names cannot contain hyphens in Python (changed ready-queue to ready_queue)
    ready_queue = deque(processes)
    total_cycles = 0
    
    # Added total_cycles increment to prevent potential infinite loops if logic fails
    while ready_queue and total_cycles < 50:
        total_cycles += 1 
        current_process = ready_queue.popleft()
        
        print(f"\nCycle {total_cycles}: Scheduling process {current_process.pid}")
        is_pending = current_process.run(quantum)
        
        if is_pending:
            ready_queue.append(current_process)
            
    print("\n---- Simulation Complete ----")

# --- Main Execution Block ---
# Logic Fix: Processes must be created BEFORE calling the function
if __name__ == "__main__":
    p1 = Process(1, random.randint(20, 100))
    p2 = Process(2, random.randint(20, 100))
    p3 = Process(3, random.randint(20, 100))

    process_list = [p1, p2, p3]
    time_quantum = 20

    round_robin_scheduling(process_list, time_quantum)