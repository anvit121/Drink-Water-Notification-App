import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "WATER!!!!!",
            message = "Please Drink Water and Stay Hydrated!!!",
            app_icon = "D:\IT\Sem 4\Python\Project\Water Notification\water.ico",
            timeout = 10
        )
        time.sleep(45*60)
