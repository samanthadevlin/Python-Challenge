import os
import csv

#define variables 
totalmonths= []
totalprofits= []
monthlychange=[]
counter = 0
#printStr

budget_data = os.path.join('Resources','budget_data.csv')


#Open and read cvs
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header_row = next(csvreader)
    row = header_row
   
    
    print(header_row)

    #Define Analysis for totalmonths and profitloss
    for row in csvreader:
            counter += 1
            #print(f'[str(csvreader.enumerate(row))]')
            #totalmonths = sum (1 for row in csvreader) + 1
            totalmonths.append(row[0])
            totalprofits.append(int(row[1]))

    #Define Profit and Losses 
    #printStr = f"Average Change: ${round(totalprofits/totalmonths,2):,}\n"



# The difference between the profit values 
diff = [(j-i) for i, j in zip(totalprofits[:-1], totalprofits[1:])]

# average changes
averChanges = round(sum(diff)/len(diff),2)  


# greatest increase 
maxValue = max(diff)
monMax = [i for i, j in enumerate(diff) if j == maxValue]
# maxgreatestimum decrease
minValue = min(diff)
monMin = [i for i, j in enumerate(diff) if j == minValue]






print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {len(totalmonths)}")
print(f"Average changes: {averChanges}")
print(f"Total: ${sum(totalprofits)}")
print(f"greatest increase in profits at {totalmonths[monMax[0]]}, maximum: {maxValue}")
print(f"greatest decrease at: {totalmonths[monMin[0]]}, minimum: {minValue}" )