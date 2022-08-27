#WEEK 6 DAY 1: Sequential Search - 3

#This third version of sequential search utilizes the found variable to display a found/not found message and a print statement in the searching for loop if statement to print as many items as were found in the search. THIS WILL DISPLAY MULTIPLE ITEMS IF MULTIPLES ARE FOUND. 
#BASE PROGRAM CODE--------------------------------------------------------------------

import csv

id = []
name = []
age = []
color = []

records = 0 

with open("C:/Users/KTRUCHON/Desktop/SE126_202240/sequentialSearch/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        id.append(rec[0])
        name.append(rec[1].lower())
        age.append(rec[2])
        color.append(rec[3].lower())

print("Finished processing file. There are {} records".format(records))

for i in range(0, records):
    print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i].title(), age[i], color[i].title()))

print("\n\n\n")

answer = "y"

while answer == "y":

    search_count = 0

    #REQUEST SEARCH PARAMTER(S)
    search = input("Enter the full LAST NAME of the record you are looking for: ").lower()
    found = -1 #found is -1 because this is NOT a valid index
    #SEQUENTIAL SEARCHING LOOP
    for i in range(0, records):

        search_count += 1 #count how many iterations of loop search performs

        #"SEARCH" through list items for requested info
        if search == name[i]:

            #every time above condition is true, we will display to the user all of the info
            #print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

            found = i
            #if wanting to print multiple search meets, use print below and not line 78
            print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

        #else:
            #print("Your search for '", search, "' was NOT FOUND.")
    
    print("\n\nSEQUENTIAL SEARCH COMPLETE.")

    if found != -1:
        print("Your search for '", search, "' was FOUND on INDEX {}.".format(found))

    else:
        print("Your search for '", search, "' was NOT FOUND.")


    print("Search Loop Iterations Performed: {}".format(search_count))

    answer = input("\nEnter 'y' to search again: [y/n] ").lower()

    while answer != "y" and answer != "n":
        print("\t\t**ERROR ERROR** INVALID ENTRY")
        answer = input("\nEnter 'y' to search again: [y/n] ").lower()

print("\n\n\t\tThanks for using my program! Byyyyyyye.")



