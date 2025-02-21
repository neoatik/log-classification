import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out)": "User Action",
        r"Backup (started|completed) at .*": "System Notification",
        r"Backup completed succesfuly.": "System Notification",
        r"File .* uploaded succesfully by user .*":"System Notification",
        r"Disk cleanup completed succesfully.":"System Notification",
        r"System reboot initiated by user .*":"System Notification",
        r"Account with ID .* created by .*":"User Action",
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None

if __name__ == "__main__":
    
    print(classify_with_regex("User User1 logged in"))
    print(classify_with_regex("Backup started at 2021-01-01 12:00:00"))     
    print(classify_with_regex("Backup completed succesfuly."))
    print(classify_with_regex("File myfile.txt uploaded succesfully by user User1"))
    print(classify_with_regex("Disk cleanup completed succesfully."))
    print(classify_with_regex("System reboot initiated by user User1"))
    print(classify_with_regex("Account with ID 123 created by User1"))
    print(classify_with_regex("hABINX"))