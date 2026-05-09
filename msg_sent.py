import pywhatkit
from datetime import datetime ,timedelta

now= datetime.now()

# Set the time for sending the message (e.g., 3 minute from now)
send_time= now+ timedelta(minutes=3)

print("Message will be sent at:", send_time.strftime("%H:%M"))
# Send the message at the specified time
pywhatkit.sendwhatmsg("+880 1704-180211", "Hello! This is a scheduled",
                       send_time.hour, send_time.minute)