import psutil

# Takes threshold values (CPU, disk, memory) from user input
def get_inputs():
    print("-----------------User Inputs(CPU,DISK,MEMORY)-----------------")
    cpu_threshold = int(input("Enter CPU threshold value(%):"))
    disk_threshold = int(input("Enter DISK threshold value(%):"))
    memory_threshold = int(input("Enter MEMORY threshold value(%):"))
    return cpu_threshold,disk_threshold,memory_threshold
           
# Fetches system metrics using psutil python library (cpu_percent , disk_usage , virtual_memory)
def system_metrics():
    print("-----------------System Metrics(CPU,DISK,MEMORY)-----------------")
    system_cpu_usage = psutil.cpu_percent(interval=1)
    system_disk_usage = psutil.disk_usage('/').percent
    system_memory_usage = psutil.virtual_memory().percent
    
    print("Currrent system CPU Usage:",system_cpu_usage)
    print("Current system DISK Usage:",system_disk_usage)
    print("Current system MEMORY Usage:",system_memory_usage)
    return system_cpu_usage,system_disk_usage,system_memory_usage
    
# Compares metrics against thresholds
def system_health_check(cpu_threshold,disk_threshold,memory_threshold,system_cpu_usage,system_disk_usage,system_memory_usage):
    print("---------------System Health Check-----------------")
    # CPU Check
    print("CPU CHECK")
    print("----------")
    if system_cpu_usage > cpu_threshold:
        print(f"High Alert for CPU Usage:{system_cpu_usage}")
    else:
        print("Safe")
    # DISK Check
    print("DISK CHECK")
    print("----------")
    if system_disk_usage > disk_threshold:
        print(f"High Alert for DISK Usage:{system_disk_usage}")
    else:
        print("Safe")
    # MEMORY Check
    print("MEMORY CHECK")
    print("----------")
    if system_memory_usage > memory_threshold:
        print(f"Alert for MEMORY Usage:{system_memory_usage}")
    else:
        print("Safe")

# Calling functions
cpu_threshold,disk_threshold,memory_threshold = get_inputs()
system_cpu_usage,system_disk_usage,system_memory_usage = system_metrics()       
system_health_check(cpu_threshold,disk_threshold,memory_threshold,system_cpu_usage,system_disk_usage,system_memory_usage)