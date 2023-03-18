#Delete then re-index, sort Id
def deletehabits(input_id: int):
    try:
        import sqlite3
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        inp_delete = input_id

        while True:

            # in case of empty input, will delete unexist row
            try:
                if not input_id:
                    input_delete = input("\nDELETE Habit's ID number : ") or lenrecords + 100000000000000000000
                    inp_delete = int(input_delete)
                if inp_delete > lenrecords:
                    print("\nYour input is not in the list. Try again")                    
            except ValueError:
                print("It's not a valid Id. Try again.")
            else:
                break


        # Delete Id if Id exist
        command = (f'''DELETE FROM habit_db WHERE Id = {inp_delete} AND Id IS NOT NULL;''')
        conn.execute(command)

        # Sort Id after deleted Id
        command = (f'''UPDATE habit_db SET ('Id') = (Id)-1  WHERE Id > {inp_delete} ;''')
        conn.execute(command)
        sqliteConnection.commit()
        conn.close()
        print("Succeed to Delete Habit")

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite connection is closed')
