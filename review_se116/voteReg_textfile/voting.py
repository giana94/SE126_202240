import csv

records = 0

too_young = 0 #age < 18
not_reg = 0 #age >=18, reg != "Y"
no_vote = 0 #age >= 18, reg == "Y", voted != "Y"
yes_vote = 0 #age >= 18, reg =="Y", voted == "Y"

print("{0:10} \t {1:10} \t {2} \t {3}".format("ID #", "AGE", "REG", "VOTED"))
print("--------------------------------------------------")


with open("C:/Users/008018155/Desktop/SE126_202240/review_se116/voteReg_textfile/voting.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        #print(rec)

        id = rec[0]
        age = int(rec[1])
        reg = rec[2]
        voted = rec[3]

        if age < 18:

            too_young += 1

        elif reg == "N":

            not_reg += 1

        elif voted != "Y":

            no_vote += 1

        else:

            yes_vote += 1
        

        print("{0:10}| \t {1:10}| \t {2} \t {3}".format(id, age, reg, voted))





print("     TOO YOUNG: ", too_young)
print("NOT REGISTERED: ", not_reg)
print("  DID NOT VOTE: ", no_vote)
print("         VOTED: ", yes_vote)
print(" TOTAL RECORDS: ", records)