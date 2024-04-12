import time
import requests

channel_id = input("Enter the channel ID (Right-click on the channel you want to post in and select 'Copy channel ID'): ")
auth_token = input("Enter you Discord token, you can find it by doing a network capture of your Discord session: ")
url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
headers = {
    "Authorization": auth_token
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
        print("Message sent successfully, press ctrl-c to abort")

# Extract the message ID from your request
        message_id = res.json().get('id')
    else:
        print("Failed to send message, press ctrl-c to abort")

# Delete your message to make the farming invisible to admin eyes
    if message_id != None:
        delete_url = f"{url}/{message_id}"
        res = requests.delete(delete_url, headers=headers)
        if res.status_code == 204:
            print(f"Message {message_id} deleted successfully")
        else:
            print(f"Failed to delete message {message_id}")

def main():

    message_counter = 0
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
            message_counter += 1
            time.sleep(interval_2)
            send_message(message)
            message_counter += 1
            time.sleep(interval_2)
    except KeyboardInterrupt:
        print("Stopping the script...")
        print(f"{message_counter} message(s) sent")

if __name__ == "__main__":
    main()

