# Habit tracker app

- This habit tracker app is created using python language using database sqlite3 with a simple main loop as Main Page

## Features
> User can choose between two period : Daily or Weekly.
> User can create new habit, edit, delete, or analyse history.

## Tutorial how to use 
In the beginning there is one question appear:  
        
        USE PREDEFINED HABITS? Y/N : 
        
User is free to choose between start from scratch or use predefined habits as examples.

After that, Main Menu will appear :

        [1] Enter 1 to CREATE NEW HABIT.
        [2] Enter 2 to COMPLETE TASKS.
        [3] Enter 3 to MANAGE (EDIT/ DELETE) HABIT.
        [4] Enter 4 to ANALYSE YOUR HABIT.
        [Q] Enter q to quit.
      
User can create habits, checkoff task, manage, or analyse habits.

1. Create New Habit
   For Habit creation, user need to input Habit's Title and Period. There are 2 Period options, between daily or weekly habits.

2. Complete Task
   If user complete task/ checkoff the task before the due date, Streak will be added by 1, as well as Max_Streak.
   Start_Date and Due_date will be renewed.
   
   Streak will be increasing if user checkoff the task within period between Start_Date and Due_Date.
   If user didn't checkoff within period, Streak will be reset to zero, but Max_Streak still remain the same, and Break will be added by 1.
   If Streak > Max_Streak, then Max_Streak will be changed become = Streak.

3. Manage(Edit/Delete) sub menu :

        [1] Enter 1 to DELETE HABIT
        [2] Enter 2 to EDIT HABIT'S TITLE
        [3] Enter 3 to EDIT HABIT'S PERIOD TO DAILY
        [4] Enter 4 to EDIT HABIT'S PERIOD TO WEEKLY
        [X] Enter X to EXIT
   
   If Period change, then Start_Date will be reset to today, and Due_Date will be today + 1 for Daily, and become today + 7 for Weekly.
   Streak, Max_Streak, and Break will remain the same, and will be added or reset according to new Period.
        
4. Analyse sub menu :

        [1] Enter 1 to DISPLAY ALL HABITS
        [2] Enter 2 to DISPLAY ALL DAILY HABITS
        [3] Enter 3 to DISPLAY ALL WEEKLY HABITS.
        [4] Enter 4 to DISPLAY LONGEST STREAK HABITS.
        [5] Enter 5 to DISPLAY LONGEST STREAK OF DAILY HABIT.
        [6] Enter 6 to DISPLAY LONGEST STREAK OF WEEKLY HABIT.
        [7] Enter 7 to DISPLAY LONGEST STREAK OF A GIVEN HABIT.
        [8] Enter 8 to DISPLAY HABIT YOU STRUGGLED THE MOST.
        [X] Enter X to EXIT.

  User can analyse history using this menu.
  User need to input a given/chosen habit to display the longest streak (Max_Streak) of the choice.
