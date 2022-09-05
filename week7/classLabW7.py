#The Python Pals
#SE126_202240
#Class Lab Week 7
#9/5/2022

#---------------Program Prompt--------------- 
#Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this:
#After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.
#You must use functions that allows the user to enter the row and seat number.  The row should be asked for separately from the seat number (two inputs)
#You must use a function that asks the user in they want to continue or stop. The function should only accept an uppercase or lowercase y or n

#---------------Variable Dictionary---------------
#seatA - D              list index for seats
#seat                   seatPick() function allows user to select Row and Seat letter
#seatTaken              True or False - will not allow seat option to be picked if already X and True
#answer                 = "y" to stay in program






#Functions:
def seatPick():
    #asks the user for the row and seat and returns it
    r = int(input("\n\tPlease select a seat Row [1 - 7]: "))
    while r < 1 or r > 7:
        r = int(input("\n\t**INVALID INPUT** \nPlease select a seat Row [1 - 7]: "))

    s = str(input("\tPlease select the seat you would like [A - D]: ")).upper()
    while s != "A" and s != "B" and s != "C" and s != "D":
        s = str(input("\t**INVALID INPUT** \nPlease select the seat you would like [A - D]: ")).upper()

    return [(r - 1), s]

def again():
    answer = input("\nWould you like to enter another seat [y/n]: ").lower()
    while answer != "n" and answer != "y":
        print("\t\t **ERROR** Invalid Entry")
        answer = input("\nWould you like to enter another seat [y/n]: ").lower()
    return answer
#---------------MAIN CODE---------------
import os

#lists
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

print("ROW")
for i in range(0, (len(seatA))):
    #displays original seating chart
    print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

answer = "y"
while answer == "y":
    seatTaken = "False"
    seat = seatPick()
    os.system('cls')   #system clear

    if seatA[seat[0]] == 'X':
            if seat[1] == 'A':
                seatTaken = "True"
    if seatB[seat[0]] == 'X':
            if seat[1] == 'B':
                seatTaken = "True"
    if seatC[seat[0]] == 'X':
            if seat[1] == 'C':
                seatTaken = "True"
    if seatD[seat[0]] == 'X':
            if seat[1] == 'D':
                seatTaken = "True"

    for i in range(0, (len(seatA))):
        if seatTaken == "False":
            #checks the input from user against this if/else tree
            if seatA[seat[0]] != 'X':
                if seat[1] == 'A':
                    seatA[seat[0]] = 'X'
            if seatB[seat[0]] != 'X':
                if seat[1] == 'B':
                    seatB[seat[0]] = 'X'
            if seatC[seat[0]] != 'X':
                if seat[1] == 'C':
                    seatC[seat[0]] = 'X'
            if seatD[seat[0]] != 'X':
                if seat[1] == 'D':
                    seatD[seat[0]] = 'X'

            #prints updated seating chart
            print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

    if seatTaken == "True":
        print("\n{}\t\t{}\t{}\t{}\t{}\t".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))
        print("\nThis seat is already taken. Please choose another.")

    answer = again()

print("\n\n\t\t\tThank you for using our program! Goodbyeeeeee!")