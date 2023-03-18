# Edit replace Title
def edittitle(input_habit: dict):
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        old_Title = input_habit["oldtitle"]
        new_Title = input_habit["newtitle"]

        #old_Title = input("\nOLD Habit's name : ")
        #new_Title = input("\nNEW Habit's name : ") or old_Title

        conn.execute('UPDATE habit_db SET Title=? WHERE Title=?', (new_Title, old_Title))
        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite connection is closed')


# Edit period from Weekly to Daily
# Modify today as new Start Date and tomorrow as new Due_Date
# It keep existing Id, Title, Born date, Streak, Max_Streak, and Break

def edittodaily(inputid: int):

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        inp_Id = inputid

        # Change Period from Daily become weekly
        command = (
            f'''UPDATE habit_db SET ("Period") = "Daily" WHERE ("Period") = "Weekly" AND Id = {inp_Id} AND Id IS NOT NULL;''')
        conn.execute(command)
        print("Changed Period to Daily")

        newstartdate = datetime.today().date()
        # Replace New Start_Date become today
        conn.execute('UPDATE habit_db SET (Start_Date)=? WHERE Start_Date = Start_Date AND Id = ?',
                     (newstartdate, inp_Id))
        print("Changed New Start Date")

        # timedelta for Daily period
        time_delta_D = timedelta(days=1)
        newduedate_D = newstartdate + time_delta_D
        conn.execute(
            'UPDATE habit_db SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Daily" AND Id = ?',
            (newduedate_D, inp_Id))

        print("Changed New Due Date")
        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite connection is closed')


# Edit period from daily to Weekly
# Modify today as new Start Date and next week as new Due_Date
# It keep existing Id, Title, Born date, Streak, Max_Streak, and Break

def edittoweekly(inputid: int):
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        inp_Id = inputid

        # Change Period from Daily become weekly
        command = (
            f'''UPDATE habit_db SET ("Period") = "Weekly" WHERE ("Period") = "Daily" AND Id = {inp_Id} AND Id IS NOT NULL;''')
        conn.execute(command)
        print("Changed Period to Weekly")

        newstartdate = datetime.today().date()
        # Replace New Start_Date become today
        conn.execute('UPDATE habit_db SET (Start_Date)=? WHERE Start_Date = Start_Date AND Id = ?',
                     (newstartdate, inp_Id))
        print("Changed New Start Date")

        # timedelta for Weekly period
        time_delta_W = timedelta(days=7)
        newduedate_W = newstartdate + time_delta_W
        conn.execute(
            'UPDATE habit_db SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Weekly" AND Id = ?',
            (newduedate_W, inp_Id))

        print("Changed New Due Date")
        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite connection is closed')
