import schedule
import time

def job():
    print("I'm working...")

# Schedule the job to run every 1 minute
schedule.every(1).minutes.do(job)

# Alternatively, schedule the job to run every day at a specific time
# schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
