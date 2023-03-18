# New habits creation with len of total row + 1 as new Id number
# (Using len(records) is safe, since after deleted Id it re-indexed and sorted)

def newhabits(input_habit: dict):
    print("User inputs for s creation")
    try:
        # Return list of all currently tracked habits
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        print("Connected to SQLite")

        command = """SELECT * FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ")
        lenrecords = len(records) + 1
        print(lenrecords)

        # print each row
        for row in records:
            print(row)

        # user input new habits
        do_next = True

        inp_Title = input_habit["title"]
        inp_Period = input_habit["input_period"]

        born = datetime.today().date()
        creation_start = datetime.today().date()

        due_date = creation_start + timedelta(days=7)
        if inp_Period == "Daily":
            due_date = creation_start + timedelta(days=1)


        if not input_habit:
            while do_next:
                inp_continue = input("\nCreate New Habit? Y/N: ")

                if inp_continue.upper() == 'Y':
                    inp_Id = lenrecords + 1
                    print(f'New Habit Id is : {inp_Id}')

                    streak = 0

                    inp_Title = input("\nNew HabitName : ")
                    ############ if it's not exist
                    print(inp_Title)
                    print(f'Habit created on : {creation_start}')

                    lenrecords = lenrecords + 1

                    inp_Period = input("\nPeriod is Daily? Y/N : ")

                    # New Daily Habit Creation
                    doing = True
                    while doing:
                        if inp_Period.upper() == 'Y':

                            # daily_habit()
                            inp_Period = 'Daily'
                            print(f'Habit Period : {inp_Period}')

                            due_date = creation_start + timedelta(days=1)
                            print(f'Due date to checkoff : {due_date}')

                            doing = False

                        # New Weekly Habit creation
                        elif inp_Period.upper() == 'N':

                            # weekly_habit()
                            inp_Period = 'Weekly'
                            print(f'Habit Period : {inp_Period}')

                            due_date = creation_start + timedelta(days=7)
                            print(f'Due date to checkoff : {due_date}')

                            doing = False

                        else:
                            print("\nYour input is not Y or N. Try again")
                            inp_Period = input("\nPeriod is Daily? Y/N : ")

                elif inp_continue.upper() == 'N':
                    conn.close()
                    print("Bye-Bye")
                    do_next = False            
                # insert_into_habit_db() ended


                # if "N" then Go to Main Menu
            else:
                print("\nYour input is not Y or N. Try again")
                inp_continue = input("\nCreate New Habit? Y/N: ")

        # insert_into_habit_db
        habits = [
            (lenrecords, inp_Title, inp_Period, born, creation_start, due_date, 0, 0, 0)
        ]

        conn.executemany("INSERT OR REPLACE INTO habit_db VALUES(?,?,?,?,?,?,?,?,?)", habits)
        print("succeed to insert into")

        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print('SQLite connection is closed')
