#WEEK 6 DAY 1: Sequential Search

#This fourth and final version of sequential search utilizes the found variable but turns it into a list which will hold multiple index locations of multiple search results when found. It allows for a finding of multiple items matching the search. IT WILL WORK FOR MULTIPLE FOUND ITEMS.


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
    found = [] #found is an empty list which will hold all index positions of found searched-for items
    #SEQUENTIAL SEARCHING LOOP
    for i in range(0, records):

        search_count += 1 #count how many iterations of loop search performs

        #"SEARCH" through list items for requested info
        if search == name[i]:

            #every time above condition is true, we will display to the user all of the info
            #print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

            found.append(i)
            #if wanting to print multiple search meets, use print below and not line 78
            #print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

        #else:
            #print("Your search for '", search, "' was NOT FOUND.")
    
    print("\n\nSEQUENTIAL SEARCH COMPLETE.")

    if len(found) > 0:
        print("Your search for '", search, "' was FOUND on INDEX {}.".format(found))
        #print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(found, id[found], name[found], age[found], color[found]))
        for i in range(0, len(found)):
            #found[i] is just an index number from original searched-through list
            print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(found[i], id[found[i]], name[found[i]], age[found[i]], color[found[i]]))
    else:
        print("Your search for '", search, "' was NOT FOUND.")


    print("Search Loop Iterations Performed: {}".format(search_count))

    answer = input("\nEnter 'y' to search again: [y/n] ").lower()

    while answer != "y" and answer != "n":
        print("\t\t**ERROR ERROR** INVALID ENTRY")
        answer = input("\nEnter 'y' to search again: [y/n] ").lower()

print("\n\n\t\tThanks for using my program! Byyyyyyye.")



