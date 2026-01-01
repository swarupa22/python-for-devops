# Used functions, try & except blocks , built-inexceptions(ValueError , NameError , KeyboardInterrupt)

import psutil


def get_inputs():
        print("=============== User Inputs(CPU,DISK,MEMORY) ==========================\n")
        
        # Using try block here as the inputs might cause an exception if user gives any alphabet or special character values    
        try:
            cpu_threshold = int(input("Enter CPU threshold value(%):"))
            disk_threshold = int(input("Enter DISK threshold value(%):"))
            memory_threshold = int(input("Enter MEMORY threshold value(%):"))
            return cpu_threshold,disk_threshold,memory_threshold
        
        # Using except block if the exceptions (alphabet or special character values) occurred in try block
        except ValueError as ve:
            print("Value Error Exception Raised : ",ve)
            print("Invalid ! Please type/give only numerics again\n")
            return None,None,None
        
        # Using multiple except blocks if the exceptions (stopped by user) occurred in try block
        except KeyboardInterrupt:
            print("Input interrupted by user\n")
            return None, None, None

          

def system_metrics():
        print("=====================System Metrics(CPU,DISK,MEMORY)=============================\n")
        
        # Using try block here as the inputs might cause an exception if we forgot to import psutil library 
        try:
            system_cpu_usage = psutil.cpu_percent(interval=1)
            system_disk_usage = psutil.disk_usage('/').percent
            system_memory_usage = psutil.virtual_memory().percent
        
            print(f"Currrent system CPU Usage:{system_cpu_usage}")
            print(f"Current system DISK Usage:{system_disk_usage}")
            print(f"Current system MEMORY Usage:{system_memory_usage}")
            return system_cpu_usage,system_disk_usage,system_memory_usage
        
        # Using except block here if the exceptions(forgot to import psutil library) occurred in try block
        except NameError as e:
            print("Name Error Exception Raised :",e)
            print("System Metrics not fetched ! Please check if the psutil library is imported/defined or not\n")
            return None,None,None
        
   

def system_health_check(cpu_threshold,disk_threshold,memory_threshold,system_cpu_usage,system_disk_usage,system_memory_usage):
        print("===========================System Health Check================================\n")
        
        if None in (cpu_threshold,disk_threshold,memory_threshold,system_cpu_usage,system_disk_usage,system_memory_usage):
            print(" System Health Check skipped due to missing data/exceptions")
            return
        
        print("CPU CHECK")
        print("===========")
        if system_cpu_usage > cpu_threshold:
            print(f"High Alert for CPU Usage:{system_cpu_usage}")
        else:
            print("Safe")
            
        print("DISK CHECK")
        print("============")
        if system_disk_usage > disk_threshold:
            print(f"High Alert for DISK Usage:{system_disk_usage}")
        else:
            print("Safe")
            
        print("MEMORY CHECK")
        print("=============")
        if system_memory_usage > memory_threshold:
            print(f"Alert for MEMORY Usage:{system_memory_usage}")
        else:
            print("Safe")

cpu_threshold,disk_threshold,memory_threshold = get_inputs()
system_cpu_usage,system_disk_usage,system_memory_usage = system_metrics()       
system_health_check(cpu_threshold,disk_threshold,memory_threshold,system_cpu_usage,system_disk_usage,system_memory_usage)


