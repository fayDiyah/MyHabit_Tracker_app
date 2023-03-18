def allhabitlist():
    # Display All Habits
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        command = """SELECT * FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ", len(records))
        print("\n")

        # print each row
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite connection is closed')


def dailyhabitlist():
    # Return list of all habits with the same periodicity : Daily
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        command = """SELECT * FROM habit_db WHERE Period = 'Daily'"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ", len(records))
        print("\n")

        # print each row
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")
            # print('SQLite connection is closed')


def weeklyhabitlist():
    # Return list of all habits with the same periodicity : Weekly

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        command = """SELECT * FROM habit_db WHERE Period = 'Weekly'"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ")

        # print each row
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")
            # print('SQLite connection is closed')


def longstreakhabits():
    # Return the longest run streak of all defined habits

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        command = """SELECT Title, MAX(Max_Streak) FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()

        # print each row
        for row in records:
            print(f"The longest run streak among all habits is : {row} ")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")
            # print('SQLite connection is closed')


def longstreakdailyhabits():
    # Return the longest run streak of all daily habits

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        command = """SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Period = 'Daily'"""
        conn.execute(command)
        records = conn.fetchall()

        # print each row
        for row in records:
            print(f"The longest run streak among all habits is : {row} ")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")
            # print('SQLite connection is closed')


def longstreakweeklyhabits():
    # Return the longest run streak of all weekly habits

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        command = """SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Period = 'Weekly'"""
        conn.execute(command)
        records = conn.fetchall()

        # print each row
        for row in records:
            print(f"The longest run streak among all habits is : {row} ")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")
            # print('SQLite connection is closed')

def longstreakgivenhabit(inputid: int):
    """Return the longest run streak for a given habit"""

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        command = """SELECT * FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ")

        # print each row
        for row in records:
            print(row)

        # Input habit title while habitId is exist
        lenrecords = int(len(records))

        inp_Id = inputid

        command = (f'''SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Id = {inp_Id} ;''')
        conn.execute(command)
        records = conn.fetchall()

        # print each row
        for row in records:
            print(f"The longest run streak of given habits is : {row} ")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")
            # print('SQLite connection is closed')


def shortstreakhabits():
    # Return the longest run streak of all defined habits

    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        # print("Connected to SQLite")

        command = """SELECT Title, MIN(Max_Streak) FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()

        # print each row
        for row in records:
            print(f"Habit you struggled the most is : {row} ")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")
            # print('SQLite connection is closed')