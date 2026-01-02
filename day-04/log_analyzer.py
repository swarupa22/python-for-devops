def log_analysis(): 
    
    # storing log counts here
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    
    # reading the application log line by line (all lines) and counting the specified errors
    print("\n=======================Reading the Application Log Data=================================")
    try:
        with open("application.log","r") as rf:
            application_lines = rf.readlines()
        
        if not application_lines:
            print("Data is not present in application log file\n")
            return
        
        for line in application_lines:
            if "INFO" in line:
                log_counts["INFO"] += 1
            elif "WARNING" in line:
                log_counts["WARNING"] +=1
            elif "ERROR" in line:
                log_counts["ERROR"] +=1
                
    except FileNotFoundError as fe:
        print("File Not Found Exception raised:", fe)
        return   
    
    # Printing the errors count here on terminal
    print("\n=======================Log Analysis Summary Data=================================")
    for error,count in log_counts.items():
        print(f"Count of {error} Messages in application log:{count}")    
    
    # Writing the errors count same in the output.txt file
    with open("output.txt","w") as rw:
        rw.write("\n=======================Log Analysis Summary Data=================================")
        for error,count in log_counts.items():
            rw.write(f"\nCount of {error} Messages in application log:{count}")
            
    print("\nSummary Data is successfully saved in output file\n")
    
log_analysis()