#total number of months
#net total amount of profit/losses over entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#As an example, your analysis should look similar to the one below:
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)


#1 read the file
#2 calc the total number of months 
#3 calc the average change
'''

#method #1
import os
import csv

# WHY USE THIS METHOD, AND NOT THE OS.PATH METHOD?********************************
fileToLoad = "/Users/eli/Desktop/Assignments/Week-4_Python1/python-challenge/PyBank-challenge/raw-data/budget_data.csv"
fileToOutput = "/Users/eli/Desktop/Assignments/Week-4_Python1/python-challenge/PyBank-challenge/output/budgetAnalysis_1.txt"
#pybank_csv = os.path.join ("..","python-challenge", "PyBank-challenge","raw-data", "budget_data.csv")

 

#*************************************************
#WHAT IS THE ATTACK PLAN TO GO ABOUT UNDERSTANDING HOW TO BUILD THIS PROGRAM - EX TRACK PARAS
# Tracking revenue parameters
totalMonths = 0
prevRevenue = 0
monthOfChange = []
revenueChangeList = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999999999999]
totalRevenue = 0
#*************************************************
# Read the csv and convert to a list of dictionaries
#BETTER EXPLAIN WITH OPEN
with open(fileToLoad) as revenueData:
    reader = csv.DictReader(revenueData)

    for row in reader:

        # Tracks the totals
        totalMonths = totalMonths + 1
        totalRevenue = totalRevenue + int(row["Profit/Losses"])

        #Tracks the revenue change
        revenueChange = int(row["Profit/Losses"]) - prevRevenue
        prevRevenue = int(row["Profit/Losses"])
        revenueChangeList = revenueChangeList + [revenueChange]
        monthOfChange = monthOfChange + [row["Date"]]

        # Calculate the greatest increase
        if (revenueChange > greatestIncrease[1]):
            greatestIncrease[0] = row["Date"]
            greatestIncrease[1] = revenueChange

            # Calculate the greatest decrease
        if (revenueChange < greatestDecrease[1]):
            greatestDecrease[0] = row["Date"]
            greatestDecrease[1] = revenueChange

# Calculate the average revenue change
revenueAvg = sum(revenueChangeList) / len(revenueChangeList)

# Generate Ouput Summary
output = (
f"\nFinancial Analysis:\n"
f"---------------------------\n"
f"Total Months: {totalMonths}\n"
f"Total Revenue: ${totalRevenue}\n"
f"Average Revenue Change: {revenueAvg}\n"
f"Greatest Increase in Revenue: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
f"Greatest Decrease in Revenue: {greatestDecrease[0]} (${greatestDecrease[1]})\n"
)

# Print the output
print(output)

# Export the results to text file
with open(fileToOutput, "w") as txt_file:
    txt_file.write(output)












             