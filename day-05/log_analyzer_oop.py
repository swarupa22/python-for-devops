class log_analysis():
    
    def __init__(self, log_file, output_file):
        self.log_file = log_file
        self.output_file = output_file
        # storing log counts here
        self.log_counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }
        
        
    def read_and_analyze_logs(self):
        # reading the application log line by line (all lines) and counting the specified errors
        print("\n=======================Reading the Application Log Data=================================")
        try:
            with open(self.log_file,"r") as rf:
                application_lines = rf.readlines()
            
            if not application_lines:
                print("Data is not present in application log file\n")
                return False
            
            for line in application_lines:
                if "INFO" in line:
                    self.log_counts["INFO"] += 1
                elif "WARNING" in line:
                    self.log_counts["WARNING"] +=1
                elif "ERROR" in line:
                    self.log_counts["ERROR"] +=1                   
            return True
                    
        except FileNotFoundError as fe:
            print("File Not Found Exception raised:", fe)
            return False
    
    
    def terminal_summary(self):
        # Printing the errors count here on terminal
        print("\n=======================Log Analysis Summary Data=================================")
        for error,count in self.log_counts.items():
            print(f"Count of {error} Messages in application log:{count}")
    
    
    def file_summmary(self):
    # Writing the errors count same in the output.txt file
        with open(self.output_file,"w") as rw:
            rw.write("\n=======================Log Analysis Summary Data=================================\n")
            for error,count in self.log_counts.items():
                rw.write(f"Count of {error} Messages in application log:{count}\n")
                
        print("\nSummary Data is successfully saved in output file\n")
        
if __name__ == "__main__":
    log_analyzer = log_analysis("application.log", "output.txt")
    
if log_analyzer.read_and_analyze_logs():
        log_analyzer.terminal_summary()
        log_analyzer.file_summmary()