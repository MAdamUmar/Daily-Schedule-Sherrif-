from plyer import notification
import time
import threading

# Function for the first script (fixed time notifications)
def fixed_time_notifications():
    while True:
        # Gym notification at 21:30
        gym_time = '21:30'
        current_time = time.strftime("%H:%M")
        if current_time == gym_time:
            notification.notify(
                title='*** GO TO GYM ***',
                message='GYMMMMM TIME CHAD! TIME TO BREAK APART AND BUILD ANEW!!',
                timeout=3,
                # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
            )
            time.sleep(60)

        # Dinner notification at 19:00
        dinner_time = '19:00'
        current_time = time.strftime("%H:%M")
        if current_time == dinner_time:
            notification.notify(
                title='*** Dinner time! ***',
                message='Hurry and get your last refill before the gym!',
                timeout=3,
                # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
            )
            time.sleep(60)

        # Breakfast notification at 07:00
        break_fast_time = '07:00'
        current_time = time.strftime("%H:%M")
        if current_time == break_fast_time:
            notification.notify(
                title='*** Breakfast time! ***',
                message='Get your first energy refill for the day!',
                timeout=3,
                # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
            )
            time.sleep(60)

        # Lunch notification at 12:00
        lunch_time = '12:00'
        current_time = time.strftime("%H:%M")
        if current_time == lunch_time:
            notification.notify(
                title='*** Lunch Time! ***',
                message='Have a break and recharge your batteries midday!',
                timeout=3,
                # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
            )
            time.sleep(60)

# Function for the second script (interval-based notifications)
def interval_notifications():
    while True:
        # First notification (Work reminder)
        notification.notify(
            title='*** TIME TO WORK ***',
            message='Its time to do what must be done.. work hard chad!',
            timeout=3,
            # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
        )
        time.sleep(1800)  # 30 minutes

        # Second notification (Drink water)
        notification.notify(
            title='*** DRINK WATER ***',
            message='Remember that a hydrated mind is a powerful mind! Time to supercharge your focus!',
            timeout=3,
            # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
        )
        time.sleep(2700)  # 45 minutes

        # Third notification (Have a snack)
        notification.notify(
            title='*** HAVE A SNACK and DRINK WATER ***',
            message='This is your cue to go and gobble down some treats! Dont forget to hydrate again..',
            timeout=3,
            # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
        )
        time.sleep(1800)  # 30 minutes

        # Fourth notification (Take a break)
        notification.notify(
            title='*** HAVE A BREAK ***',
            message='Work is good chad but remember to rest! So go out and refresh King! And drink more water!',
            timeout=3,
            # app_icon = >>ENTER PATH OF IMAGE ON DEVICE<<,
        )
        time.sleep(900)  # 15 minutes


# Start both scripts using threading
if __name__ == '__main__':
    # Create threads for both functions
    fixed_time_thread = threading.Thread(target=fixed_time_notifications)
    interval_thread = threading.Thread(target=interval_notifications)

    # Start the threads
    fixed_time_thread.start()
    interval_thread.start()

    # Keep the main thread alive
    fixed_time_thread.join()
    interval_thread.join()
