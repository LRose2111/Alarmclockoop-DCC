#Alarm Clock Lab
#As a developer, I want to use Python’s proper snake_case for variable names.
#As a developer, I want to create a AlarmClock class.
#As a developer, I want the AlarmClock class to have class instance variables to keep track of the AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).
#As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.
#As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.
#As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.
#As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.
#1. Print the clock’s time to the terminal
#2. Call the alarm clock’s change current time method to change the current time
#3. Toggle the alarm clock’s on off switch


class Alarm:
    def __init__(self):
        self.name = 'Master Alarm 3000'
        self.enter_time = ''
        self.alarm_set = ''
        self.go_off = ''
    
    def set_time(self):
        set_time = self.enter_time
        self.enter_time = input(f'Please enter time (0001 - 2359).    ')
        print(f'The time is {self.enter_time}.')

    def set_up_alarm(self):
        self.go_off  = input(f'Please, set the time you want {self.name} to go off. (0001 - 2359)    ')
        print(f'{self.name} is set for {self.go_off}.')

    def turn_alarm_on_or_off(self):
        self.alarm_set = input(f'Is {self.name} set? (Y,N)  ')
        if self.alarm_set == 'Y':
            print(f'{self.name} is on, and set to wake you up at {self.go_off}.')
        else:
            self.alarm_set == False
            print(f'{self.name} is not turned on!')

        