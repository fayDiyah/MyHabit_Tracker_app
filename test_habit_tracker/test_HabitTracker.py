
import os

from Main_Package.Predefined import tablecreation,predefinedhabits
from Main_Package.AutoResetOverDue import autoresetoverdue
from Main_Package.CreateNew import newhabits
from Main_Package.Delete import deletehabits
from Main_Package.Edit import edittodaily,edittoweekly
from Main_Package.Task import completetask
from Main_Package.Analyze import allhabitlist,dailyhabitlist,weeklyhabitlist
from Main_Package.Analyze import longstreakhabits,longstreakdailyhabits,longstreakweeklyhabits
from Main_Package.Analyze import longstreakgivenhabit,shortstreakhabits



import sqlite3
import datetime
import time
from datetime import datetime, timedelta

sqliteConnection = sqlite3.connect('habit_db.sqlite3')
conn = sqliteConnection.cursor()
records = conn.fetchall()
lenrecords = len(records)

def test_tablecreation():
    """test if no row in database"""
    tablecreation()
    assert lenrecords == 0

def test_predefinedhabits():
    predefinedhabits()

    sqliteConnection = sqlite3.connect('habit_db.sqlite3')
    conn = sqliteConnection.cursor()    
    c = conn.execute('SELECT * FROM habit_db')

    assert list(c) == [(1,'No Sugar', 'Daily', '2023-01-01', '2023-02-27', '2023-02-28', 2, 10, 5),
              (2,'Do Sport', 'Daily', '2023-01-01', '2023-02-27', '2023-02-28', 7, 8, 9),
              (3,'Clean House', 'Weekly', '2023-02-01', '2023-02-22', '2023-02-28', 1, 1, 1),
              (4,'Eat Fruit', 'Daily', '2023-01-15', '2023-02-25', '2023-02-26', 4, 4, 2),
              (5,'Help others ', 'Weekly', '2023-02-01', '2023-02-24', '2023-02-31', 0, 0, 2),
              ]

def test_autoresetoverdue():
    autoresetoverdue()
    habit_list = conn.execute('SELECT * FROM habit_db')
    assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 10, 6),
                            (2, 'Do Sport', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                            (3, 'Clean House', 'Weekly', '2023-02-01', '2023-03-12', '2023-03-19', 0, 1, 2),
                            (4, 'Eat Fruit', 'Daily', '2023-01-15', '2023-03-12', '2023-03-13', 0, 4, 3),
                            (5, 'Help others ', 'Weekly', '2023-02-01', '2023-03-12', '2023-03-19', 0, 0, 3)
                            ]

def test_deletehabits():
    deletehabits(3)
    habit_list = conn.execute('SELECT * FROM habit_db')
    assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 10, 6),
                            (2, 'Do Sport', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                            (3, 'Eat Fruit', 'Daily', '2023-01-15', '2021-03-12', '2023-03-13', 0, 4, 3),
                            (4, 'Help others ', 'Weekly', '2023-02-01', '2023-03-12', '2023-03-19', 0, 0, 3)
                            ]

def test_newhabits():
    habit = {
        "title": "Eat Vegetable",
        "input_period": "Daily"
    }
    
    newhabits(habit)
    habit_list = conn.execute('SELECT * FROM habit_db')
    assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 10, 6),
                              (2, 'Do Sport', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2023-01-15', '2021-03-12', '2021-03-13', 0, 4, 3),
                              (4, 'Help others ', 'Weekly', '2023-02-01', '2023-03-12', '2023-03-19', 0, 0, 3),
                              (5, 'Eat Vegetable', 'Daily', '2023-03-12', '2023-03-12', '2023-03-13', 0, 0, 0)
                             ]

def test_edittodaily():
    edittodaily(4)
    habit_list = conn.execute('SELECT * FROM habit_db')
    assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 10, 6),
                               (2, 'Do Sport', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                               (3, 'Eat Fruit', 'Daily', '2023-01-15', '2023-03-12', '2023-03-13', 0, 4, 3),
                               (4, 'Help others ', 'Daily', '2023-02-01', '2023-03-12', '2023-03-13', 0, 0, 3),
                               (5, 'Eat Vegetable', 'Daily', '2023-03-12', '2023-03-12', '2023-03-13', 0, 0, 0)
                               ]

def test_edittoweekly():
    edittoweekly(1)
    habit_list = conn.execute('SELECT * FROM habit_db')
    for row in records:
        print(row)
    assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Weekly', '2023-01-01', '2023-03-12', '2023-03-19', 0, 10, 6),
                                (2, 'Do Sport', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                               (3, 'Eat Fruit', 'Daily', '2023-01-15', '2023-013-12', '2023-03-13', 0, 4, 3),
                               (4, 'Help others ', 'Daily', '2023-08-01', '2023-03-12', '2023-03-13', 0, 0, 3),
                               (5, 'Eat Vegetable', 'Daily', '2023-03-12', '2023-03-12', '2023-03-13', 0, 0, 0)
                               ]
def test_completetask():
    completetask(5)
    habit_list = conn.execute('SELECT * FROM habit_db')
    assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Weekly', '2023-01-01', '2023-03-12', '2023-03-19', 0, 10, 6),
                       (2, 'Do Sport', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                       (3, 'Eat Fruit', 'Daily', '2023-01-15', '2023-03-12', '2023-03-13', 0, 4, 3),
                       (4, 'Help others ', 'Daily', '2023-02-01', '2023-03-12', '2023-03-13', 0, 0, 3),
                       (5, 'Eat Vegetable', 'Daily', '2023-03-12', '2023-03-13', '2023-03-14', 1, 1, 0)
                       ]

def test_allhabitlist():
     """Display all habits"""
     allhabitlist()
     habit_list = conn.execute('SELECT * FROM habit_db')
     assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Weekly', '2023-01-01', '2023-03-12', '2023-03-19', 0, 10, 6),
                     (2, 'Exercise', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                     (3, 'Eat Fruit', 'Daily', '2023-01-15', '2023-03-12', '2023-03-13', 0, 4, 3),
                     (4, 'Help others ', 'Daily', '2023-02-01', '2023-03-12', '2023-03-13', 0, 0, 3),
                     (5, 'Eat Vegetable', 'Daily', '2023-03-12', '2023-03-13', '2023-03-14', 1, 1, 0)
                     ]

def test_dailyhabitlist():
    """Display all daily habits"""
    dailyhabitlist()
    habit_list = conn.execute('SELECT * FROM habit_db WHERE Period = "Daily"')
    assert list(habit_list.fetchall()) == [(2, 'Do Sport', 'Daily', '2023-01-01', '2023-03-12', '2023-03-13', 0, 8, 10),
                       (3, 'Eat Fruit', 'Daily', '2023-01-15', '2023-03-12', '2023-03-13', 0, 4, 3),
                       (4, 'Help others ', 'Daily', '2023-02-01', '2023-03-12', '2023-03-13', 0, 0, 3),
                       (5, 'Eat Vegetable', 'Daily', '2023-03-12', '2023-03-13', '2023-03-14', 1, 1, 0)
                       ]

def test_weeklyhabitlist():
     """Display all weekly habits"""
     weeklyhabitlist()
     habit_list = conn.execute('SELECT * FROM habit_db WHERE Period = "Weekly"')
     assert list(habit_list.fetchall()) == [(1, 'No Sugar', 'Weekly', '2023-01-01', '2023-03-12', '2023-03-19', 0, 10, 6)]

def test_longstreakhabits():
     """Display longest streak habits"""
     longstreakhabits()
     habit_list = conn.execute('SELECT Title, MAX(Max_Streak) FROM habit_db')
     assert list(habit_list.fetchall()) == [('No Sugar',10)]

def test_longstreakdailyhabits():
    """Display longest streak Daily habits"""
    longstreakdailyhabits()
    habit_list = conn.execute('SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Period = "Daily"')
    assert list(habit_list.fetchall()) == [('Do Sport',8)]

def test_longstreakweeklyhabits():
     """Display longest streak Weekly habits"""
     longstreakweeklyhabits()
     habit_list = conn.execute('SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Period = "Weekly"')
     assert list(habit_list.fetchall()) == [('No Sugar', 10)]

def test_longstreakgivenhabit():
    """Display longest streak of given habit"""
    #inp_Id = 2
    longstreakgivenhabit(2)
    habit_list = conn.execute('SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Id = 2')
    assert list(habit_list.fetchall()) == [('Do Sport',8)]

def test_shortstreakhabits():
    """Display shortest streak from all habits"""
    shortstreakhabits()
    habit_list = conn.execute('SELECT Title, MIN(Max_Streak) FROM habit_db')
    assert list(habit_list.fetchall()) == [('Help others ',0)]

