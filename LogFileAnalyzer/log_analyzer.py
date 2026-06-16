import re
from collections import defaultdict

# How many failed attempts = brute force
THRESHOLD = 5

failed_attempts = defaultdict(int)  # IP -> count
successful_logins = []

with open("sample_auth.log", "r") as f:
    for line in f:

        # Check for failed login
        failed = re.search(r"Failed password for (\S+) from (\d+\.\d+\.\d+\.\d+)", line)
        if failed:
            user, ip = failed.groups()
            failed_attempts[ip] += 1

        # Check for successful login
        success = re.search(r"Accepted password for (\S+) from (\d+\.\d+\.\d+\.\d+)", line)
        if success:
            user, ip = success.groups()
            successful_logins.append((user, ip))

# Print Report 
print("=" * 50)
print("       LOG FILE ANALYZER - REPORT")
print("=" * 50)

print(f"\nTotal failed attempts : {sum(failed_attempts.values())}")
print(f"Total successful logins : {len(successful_logins)}")

print("\n--- Brute Force Alerts ---")
found = False
for ip, count in sorted(failed_attempts.items(), key=lambda x: x[1], reverse=True):
    if count >= THRESHOLD:
        found = True
        print(f"  [!] {ip} -> {count} failed attempts  ** BRUTE FORCE **")
    else:
        print(f"  [ ] {ip} -> {count} failed attempts")
if not found:
    print("  No brute force detected.")

print("\n--- Successful Logins ---")
for user, ip in successful_logins:
    print(f"  [+] User: {user}  |  IP: {ip}")

print("\n" + "=" * 50)
