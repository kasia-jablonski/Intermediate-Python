# practice app to track your studying, you could input the minutes or hours studied, date and content covered as a practice project. 
from models import (Base, session, Study, engine)
import datetime
import time

def menu():
    while True:
        print('''
            \nSTUDYING TRACKER
            \r1) Add studying entry
            \r2) View all entries
            \r3) Search for entry
            \r4) Studying Analysis
            \r5) Exit''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
            \nPlease choose one of the options above. 
            \rA number from 1-5.
            \rPress enter to try again ''')

def submenu():
    while True:
        print('''
            \n1) Search by date
            \r2) Search by content
            \r3) Return to main menu''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3']:
            return choice
        else:
            input('''
            \nPlease choose one of the options above. 
            \rA number from 1-3.
            \rPress enter to try again ''')

def submenu2():
    while True:
        print('''
            \n1) Edit
            \r2) Delete
            \r3) Return to main menu''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3']:
            return choice
        else:
            input('''
            \nPlease choose one of the options above. 
            \rA number from 1-3.
            \rPress enter to try again ''')


def clean_time(time_str):
    try:
        time_int = int(time_str)
    except ValueError:
        input('''
        \n****** TIME ERROR ******
        \rTime should be a number.
        \rPress enter to try again.
        \r************************''')
        return
    else:
        return time_int

def clean_date(date_str):
    split_date = date_str.split('-')
    try:
        day = int(split_date[1])
        month = int(split_date[0])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except:
        input('''
        \n****** DATE ERROR ******
        \rThe date should be in format: MM-DD-YYYY.
        \rEx: 03-20-2021
        \rPress enter to try again.
        \r************************''')
        return
    else:
        return return_date



def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            date_error = True
            while date_error:
                date = input('Date when you studied (Ex: 03-20-2020): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            time_error = True
            while time_error:
                time = input('Total time studied in minutes: ')
                time = clean_time(time)
                if type(time) == int:
                    time_error = False
            content = input('Content covered during studying: ')
            new_study = Study(date=date, time=time, content=content)
            session.add(new_study)
            session.commit()
            print('Studying Entry Added!')
            #time.sleep(1.5)
        elif choice == '2':
            print('  | Date\t| Total Time Studied | Content Covered During Studying')
            for study_entry in session.query(Study):
                print(f'{study_entry.id} | {study_entry.date}\t| {study_entry.time}\t\t     | {study_entry.content}')
            input('\nPress enter to return to the main menu.')
        elif choice == '3':
            search_choice = submenu()
            if search_choice == '1':
                date_error = True
                while date_error:
                    date = input('Date when you studied (Ex: 03-20-2020): ')
                    date = clean_date(date)
                    if type(date) == datetime.date:
                        date_error = False
        
                the_study = session.query(Study).filter(Study.date==date).all()
                if len(the_study) > 0 :
                    print('  | Date\t| Total Time Studied | Content Covered During Studying')
                    for study in the_study:
                        print(f'{study.id} | {study.date}\t| {study.time}\t\t     | {study.content}')
                else:
                    print(f'No studying found on {date}')

            elif search_choice == '2':
                content = input('What you studied? ')
                content_found = session.query(Study).filter(Study.content.like(f'%{content}%')).all()
                if len(content_found) > 0 :
                    print('  | Date\t| Total Time Studied | Content Covered During Studying')
                    for content in content_found:
                        print(f'{content.id} | {content.date}\t| {content.time}\t\t     | {content.content}')
                else:
                    print(f'No studying of {content} found')
        elif choice == '4':
            date_started = session.query(Study).order_by(Study.date).first()
            total_time = 0
            for time in session.query(Study).all():
                total_time += time.time
            print(f'Studying started on {date_started.date}')
            print(f'Total time studied since {date_started.date}: {total_time} minutes')
        else:
            print('GOODBYE')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()