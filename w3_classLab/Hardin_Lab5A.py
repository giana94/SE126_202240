#Giana Hardin
#Lab 5A
#05/15/2022
#Program Essentials with Python, 202230_SE116.01

#VARIABLE DICTIONARY

#notElig_reg        underage person
#notElig_vote       of age but arent registered
#num_voted          number of people who voted
#didNotVote         registered but did not vote
#processRec         number of records processed
#answer             yes or no input answers
#id_num             input ID number of potential voter
#age                input answer persons age
#reg                input answer to being registered
#voted              input answer did they vote

#Program prompt - Construct a program that will analyze potential voters. Program should generate the following totals: 1) # of individuals not eligible to register; 2)# of individuals who arent registered; 3) # of individuals who are eligible to vote but did not vote; 4) # of individuals who did vote; 5) # of records processed. 

#-------MAIN CODE--------
notElig_reg = 0
notElig_vote = 0
num_vote = 0
didNotVote = 0
processRec = notElig_reg + notElig_vote + didNotVote + num_vote 

print("\n\t\tWelcome!")
answer = input("\n\nDo you have any potential voters? [y/n]: ")

while answer == "y" or answer == "Y":
  id_num = str(input("\nWhat is their ID Number?: "))
  age = int(input("What is their age?: "))
  
  if age >= 18 :
    reg = input("Are they registered to vote? [y/n]: ")
    
    if reg == "y" or reg == "Y":
      voted = input("Did they vote? [y/n]: ")
      if voted == "y" or voted == "Y":
        num_vote += 1 

      elif voted == "n" or voted == "N":
        didNotVote += 1
        
        
    elif reg == "n" or reg == "N":
      notElig_vote = notElig_vote + 1 
      print("\n\tPerson is Not Eligible to vote")
    
  
  elif age < 18 :
    print("\n\tPerson is not Eligible to Register")
    notElig_reg = notElig_reg + 1

    
  answer = input("\n\nDo you have any more potential voters? [y/n]: ")

processRec = notElig_reg + notElig_vote + didNotVote + num_vote 
print("\n\n\t\t\t\tSUMMARY")
print("\n# of individuals not Eligible to register: ", (notElig_reg))
print("# of individuals not Eligible to Vote: ",(notElig_vote))
print("# of individuals who are Eligible but did not vote: ",(didNotVote))
print("# of individuals who did Vote: ",(num_vote))
print("# of records processed:",(processRec))

print("\n\t\t\t\tThank you!")

