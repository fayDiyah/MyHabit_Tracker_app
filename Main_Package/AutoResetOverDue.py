# AUTO Reset Overduedated Streak to Zero, Add Break + 1, replace start date to today and Due_Date to new Due_Date
def autoresetoverdue():
    import sqlite3
    import datetime
    import time
    from datetime import datetime, timedelta

    sqliteConnection = sqlite3.connect('habit_db.sqlite3')
    conn = sqliteConnection.cursor()

    tmdelta = timedelta(days=-1)
    yestday = datetime.today().date() + tmdelta

    newstartdate = datetime.today().date()

    lenperiod_d = 1
    time_delta_daily = timedelta(days=1)
    newduedateday = newstartdate + time_delta_daily

    lenperiod_w = 7
    time_delta_week = timedelta(days=7)
    newduedateweek = newstartdate + time_delta_week

    Break_add = 1  # added to Break id Overduedated

    # Add Break +1 if Break (Overduedated)
    conn.execute('UPDATE habit_db SET Break = Break+? WHERE Break=(Break) AND Due_Date <= ?', (Break_add, yestday))

    # Reset Streak = 0 if Break (Overduedated)
    conn.execute('UPDATE habit_db SET Streak=? WHERE Streak=(Streak) AND Due_Date <= ?', (0, yestday))

    # Replace Start_Date with today newstartdate (for daily or weekly period are the same)
    conn.execute('UPDATE habit_db SET Start_Date=? WHERE Start_Date=(Start_Date) AND Due_Date <= ?',
                 (newstartdate, yestday))
    # Replace Daily Period Due_Date with newduedateday
    conn.execute('UPDATE habit_db SET Due_Date=? WHERE Due_Date=(Due_Date) AND Period=("Daily") AND Due_Date <= ?',
                 (newduedateday, yestday))
    # Replace Weekly Period Due_Date with newduedateweek
    conn.execute('UPDATE habit_db SET Due_Date=? WHERE Streak=(Streak) AND Period=("Weekly") AND Due_Date <= ?',
                 (newduedateweek, yestday))

    sqliteConnection.commit()
    print("Reset Overdue Done")
    time.sleep(1)  # sleep 1 sec