from datetime import datetime

user_input = input("Enter your goal with deadline seperated by colon --\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

Deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
Today_date = datetime.today()
time_till = Deadline_date - Today_date

#print(f"Dear user ! Time remaining for your goal : {goal} is {time_till}")

hours_till = int(time_till.total_seconds()/60 /60)
print(f"Dear user ! Time remaining for your goal : {goal} is {hours_till} hours")
