#Week 1 Day - SE116 Review Demo

#FUNCTION------------------------------------------
def capacity():

    cap = int(input("\tEnter the room's Max Capacity: "))

    return cap #REPLACES the function call line!


#MAIN CODE------------------------------------

print("Hello World!")
print("\n\n\tWelcome to the Room Safety Manager!\n\n")

answer = input("\tWould you like to check some rooms? [y/n]: ").lower()

while answer != "y" and answer != "n": #user trap loop

    print("\t\t**ERROR! INVALID ENTRY!**")
    answer = input("\tWould you like to check some rooms? [y/n]: ").lower()

while answer == "y":
    
    roomCapacity = capacity()

    peopleAttending = int(input("\tEnter the number of meeting attendees for the room: "))

    difference = roomCapacity - peopleAttending

    if difference >= 0 : #the meeting can occur (difference is positive, meaning there is room leftover)
        print("\t\tSAFELY UNDER ROOM CAPACITY")
        print("\tYou may add up to {0} people to the meeting.".format(difference))

    else: 
        print("\t\tOH NO! YOU ARE *OVER* ROOM CAPACITY")
        print("\tPlease remove {0} people to the meeting for safety regulations.".format(difference * -1))


    answer = input("\tWould you like to check some rooms? [y/n]: ").lower()

    while answer != "y" and answer != "n": #user trap loop

        print("\t\t**ERROR! INVALID ENTRY!**")
        answer = input("\tWould you like to check some rooms? [y/n]: ").lower()

print("\n\n\tThank you for using my program. Goodbye! :] \n\n")

