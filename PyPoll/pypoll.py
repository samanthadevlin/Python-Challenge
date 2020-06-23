import os
import csv 

# Define Variables 
total_votes = 0
candidates_1_vote = 0
candidates_2_vote = 0
candidates_3_vote = 0
candidates_4_vote = 0
candidates_1_percentage = 0
candidates_2_percentage = 0
candidates_3_percentage = 0
candidates_4_percentage = 0
winner = 0 

election_data = os.path.join('..','Resources','election_data.csv')

# Open and read cvs
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header_row = next(csvreader)
    row = header_row
    
    print(header_row)
# Find Total Vote for Each Person
    for row in csvreader:
        if row[2] == "Khan":
            candidates_1_vote += 1
        if row[2] == "Correy":
            candidates_2_vote += 1
        if row[2] == "Li":
            candidates_3_vote += 1
        if row[2] == "O'Tooley":
            candidates_4_vote += 1





        total_votes += 1

        
# Find Total Percentage of Each Person         
    candidates_1_percentage = round((candidates_1_vote / total_votes)*100,2)
    candidates_2_percentage = round((candidates_2_vote / total_votes)*100,2)
    candidates_3_percentage = round((candidates_3_vote / total_votes)*100,2)
    candidates_4_percentage = round((candidates_4_vote / total_votes)*100,2)

#Print
print(total_votes)
print(candidates_1_vote)
print(candidates_2_vote)
print(candidates_3_vote)
print(candidates_4_vote)
print(candidates_1_percentage)
print(candidates_2_percentage)
print(candidates_3_percentage)
print(candidates_4_percentage)

#if total votes is > [0] than 
#= "winner"


