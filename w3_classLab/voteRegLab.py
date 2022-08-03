#The Python Pals
#Lab 3
# 08/08/2022
#SE126_202240

#PROGRAM PROMPT
#Construct a program that will analyze potential voters. The program should generate the following totals:

#1) Number of individuals not eligible to register.
#2) Number of individuals who are old enough to vote but have not registered.
#3) Number of individuals who are eligible to vote but did not vote.
#4) Number of individuals who did vote.
#5) Number of records processed.

#VARIABLE DICTIONARY



#---------------------------MAIN PROGRAM-------------------------------------------------------

notElig_reg = 0
notReg = 0
num_vote = 0
didNotVote = 0
total_records = 0


import csv

with open("C:/Users/ghard/Desktop/SE126_202240/w3_classLab/voters_202040.csv") as csvfile:
    
    file = csv.reader(csvfile)
    
    for rec in file:
        
        total_records += 1
        
        idNum = rec[0]
        age = int(rec[1])
        reg_vote = rec[2]
        voted = rec[3]
        
        if age >= 18:
            
            if reg_vote == "Y":
                
                if voted == "Y":
                    num_vote += 1
                    
                elif voted == "N":
                    didNotVote += 1
                    
            elif reg_vote == "N":
                notReg += 1
                
        elif age < 18:
            notElig_reg += 1
                    
    
    print("\n\nNot eligible to register: {0:2}".format(notElig_reg))
    print("  Not registered to vote: {0:2}".format(notReg))
    print("\t    Did not vote: {0:2}".format(didNotVote))
    print("\t    People Voted: {0:2}".format(num_vote))
    print("\n TOTAL RECORDS PROCESSED: {0:2}\n\n".format(total_records))