import time
from datetime import datetime as dt

HOST_PATH = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = 'hosts'
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com",
                "www.youtube.com", "youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")
        with open(HOST_PATH, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website+"\n")
    else:
        with open(HOST_PATH, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print(
            f"Not in Working Hour: {dt.now().year, dt.now().month, dt.now().day}")
    time.sleep(5)
