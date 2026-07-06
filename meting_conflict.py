#11 Meeting Room Booking Conflict Checker

existing_meeting_start = int(input("Enter existing meeting start time: "))
existing_meeting_end = int(input("Enter existing meeting end time: "))

new_meeting_start = int(input("Enter new meeting start time: "))
new_meeting_end = int(input("Enter new meeting end time: "))

if (new_meeting_start < existing_meeting_end) and (new_meeting_end > existing_meeting_start):
    print("Scheduling Conflict!")
else:
    print("No Scheduling Conflict.")