# LogFileAnalyzer

# Log File Analyzer

A simple Python script that analyzes SSH auth logs and detects suspicious activity.

## What it does
- Counts failed login attempts per IP
- Flags IPs with 5+ failed attempts as brute force
- Lists all successful logins

## How to run

```bash
python log_analyzer.py
```

## Requirements
- Python 3.x
- No external libraries needed

## Sample Output

```
==================================================
       LOG FILE ANALYZER - REPORT
==================================================

Total failed attempts : 24
Total successful logins : 4

--- Brute Force Alerts ---
  [!] 185.220.101.1 -> 10 failed attempts  ** BRUTE FORCE **
  [!] 192.168.1.105 -> 6 failed attempts  ** BRUTE FORCE **

--- Successful Logins ---
  [+] User: john  |  IP: 10.0.0.5
```

## Author
**Thanvik S**  
GitHub: [github.com/ThanvikS102](https://github.com/ThanvikS102)  
LinkedIn: [linkedin.com/in/thanvik-s-a8a226364](https://linkedin.com/in/thanvik-s-a8a226364)
