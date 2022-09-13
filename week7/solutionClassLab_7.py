import os

#lists
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

answer = "y"

while answer == "y":

    print("ROW        SEATA     SEATB    SEATC    SEATD")
    for i in range(0, 7):

        print("{}\t{}\t{}\t{}\t{}".format(i + 1, seatA[i], seatB[i], seatC[i], seatD[i]))

    row = int(input("Enter row [1 - 7] #: "))
    seat = input("Enter seat [A - D]: ").upper()


    if seat == "A":
        if seatA[row - 1] == "A":
            seatA[row - 1] = "X"
        else: 
            print("\t\t\tSeat's Taken!")

    elif seat == "B":
        if seatB[row - 1] == "B":
            seatB[row - 1] = "X"
        else: 
            print("\t\t\tSeat's Taken!")

    elif seat == "C":
        if seatC[row - 1] == "C":
            seatC[row - 1] = "X"
        else: 
            print("\t\t\tSeat's Taken!")

    elif seat == "D":
        if seatA[row - 1] == "A":
            seatA[row - 1] = "X"
        else: 
            print("\t\t\tSeat's Taken!")

    else:
        print("booooo not a seat choice!")

    #clear seats and reprint before moving to next seat option
    print("ROW        SEATA     SEATB    SEATC    SEATD")
    for i in range(0, 7):

        print("{}\t{}\t{}\t{}\t{}".format(i + 1, seatA[i], seatB[i], seatC[i], seatD[i]))


    print("You want to sit in: ", row, seat)




    answer = input("Again? [y/n]: ")