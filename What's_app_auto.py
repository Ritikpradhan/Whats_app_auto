import pywhatkit as pyw
number =input("Enter the number")
message = input("Enter the message")
pyw.sendwhatmsg(f"+91{number}",f"{message}",17,55)