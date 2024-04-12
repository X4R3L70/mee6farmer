import time
import requests

# Enter the channel URL you want to post in, it can be retrieved in the "message" post request when you do a network capture in your browser, alternatively you can right click on a channel and select "copy channel ID" and replace the X's
url = "https://discord.com/api/v9/channels/0000000000000000/messages"

# In a network capture of you discord session, you can see in the message post request a header named "Authorization", copy it's value and replace the X's
headers = {
    "Authorization": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
}

# Function to automatically send a message
def send_message(message):
    message_id = None
# set payload function to make requests functions shorter
    payload = {
        "content": message
    }
# Make a post requests using the requests function to send a message
    res = requests.post(url, json=payload, headers=headers)

# Check if message was sent successfully
    if res.status_code == 200:
        print("Message sent successfully")

# Extract the message ID from your request
        message_id = res.json().get('id')
    else:
        print("Failed to send message")

# Delete your message to make the farming invisible to admin eyes
    if message_id != None:
        delete_url = f"{url}/{message_id}"
        res = requests.delete(delete_url, headers=headers)
        if res.status_code == 204:
            print(f"Message {message_id} deleted successfully")
        else:
            print(f"Failed to delete message {message_id}")

def main():

# Change your message here
    message='''⠸⢢⡀　　　⠘⡉⠉⢍⠒⢄\n  ⠑⢜⠈⣶⣾⣿⣿⣿⡦⠄⠑⠞⣷⣄\n   ⣴⣿⣿⣿⣿⣿⡏⢠⣶⣦⡀⠈⣿⣦\n ⣾⣿⣿⣿⣿⡿⠟⠁⡏⢿⣿⣷  ⢹⣿⣧\n ⢿⣿⣿⠟⢡⣶⣄  
⢃  ⡠⠊  ⣸⣿⣿⣧\n   ⠻⠁    ⠑⡤⠃  ⠁    ⠘⣿⣿⣿⣿\n　　 　 　 ⢀⣑⠼⠤⢤⠊⢀⣾⣿⣿⣿⡇\n　　　　⡔    ⡇  ⡎  ⣿⠿⣫⣿⣿⡇\n　　　　⡇
 ⢠⠁⡠⣇    ⣾⣿⣿⠟⠅\n　　　　⢣  ⠈⠁  ⡸    ⠻⠟⠁  ⠈⠂⢄\n　　　　　⠑⠒⠒⢁⠃  ⢸  ⢀⠊⠉⠉⠁  ⠈⠢\n　　　　 　　 ⢀⠃    ⠏⠢⡈⢄
            ⣆⣀⣤⣶⣶⣶⣦⣄\n　　　 　 　 ⡠⠁    ⣌⠔⠂⠉⠢⣑⠤⠤    ⠚⢌⠉⠲⢶⣦⠙⣿⣿⣷\n　　　　　⢔⣀⣀⣀⣰⠁    ⡐⠁      ⡠⠒⠉  ⣀⣤⣾
⡿  ⣿⣿⡿\n　 　 　 　 　 　⠈⠒⠂⠉⠁⢇⣀⠤⠄⠃⣠⣶⣿⣿⣿⣟⣉⣀⣾⣿'''

# Mee6 has a 1 minute cooldown, wait before sending the next messages, cooldowns vary to make farming more organic
    interval_1 = 90  # 1 minute and 30 seconds
    interval_2 = 120  # 2 minutes

# Send/delete/wait loop, happy farming!
    try:
        while True:
            send_message(message)
            time.sleep(interval_1)
            send_message(message)
            time.sleep(interval_2)
    except KeyboardInterrupt:
        print("Stopping the script...")

if __name__ == "__main__":
    main()

