import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = 'Please Drink Water now !!',
            message = "Drinking a lot of water increases the amount of water in your blood. This water can dilute the electrolytes in your blood, especially sodium. ... ",
            app_icon = "icon.ico",
            timeout = 10
        )
        time.sleep(60*60)