# 📘 Day 07 – Thinking Before Coding (DevOps Mindset)

## 📄Selected Script
log_analyzer_cli script (Day 06)


## ❓ What problem am I solving?
- Application log files are usually very large and hard to go through manually.
- It is not easy to quickly find how many INFO, WARNING, or ERROR messages are present.
- During debugging, scrolling through log files takes time and slows down the process.
- Need a quicker way to analyze logs directly from the command line.
- Want to filter logs by level and save the summary for future use.


## 📥 What input does my script need?
- The path of the application log file that needs to be analyzed.
- The path of the output file where the summary need to be saved.
- An optional log level (INFO, WARNING, or ERROR) to filter the results.
- All inputs are passed as command-line arguments while running the script.


## 📤 What output should my script give?
- A clear summary showing the count of INFO, WARNING, and ERROR messages displayed in the terminal.
- The same summary written to an output file for further use.
- If a log level is specified, only that level’s count should be shown in the output.
- Exception messages if the log file is missing or empty.


## 🔄 What are the main steps?
- Take input values from the command line from the user
- Check whether the log file exists and is readable.
- Read the log file line by line.
- Count INFO, WARNING, and ERROR messages from the logs.
- Apply log-level filtering if required.
- Display the summary in the terminal and save it to the output file.
