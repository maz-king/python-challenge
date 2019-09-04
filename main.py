import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    profloss = []
    date = []
    difference = []

    for row in csvreader:

        date.append(row[0])
        profloss.append(int(row[1]))
 
    for i in range(len(profloss)-1):
        difference.append(profloss[i+1]-profloss[i])
        total = sum(profloss)
        average = sum(difference)/len(difference)
        gincrease = max(difference)
        gdecrease = min(difference)
        maxdatediff = str(date[difference.index(gincrease)])
        mindatediff = str(date[difference.index(gdecrease)])

    print(f"total months: {len(date)}")
    print(f"total: ${total}")
    print(f"average change: {int(average)}")
    print(f"greatest increase: {maxdatediff} ${gincrease}")
    print(f"greatest decrease: {mindatediff} ${gdecrease}")

    f = open('analysis.txt', 'w')
    print("Financial Analysis", file=f)
    print("-----------------------------------", file=f)
    print(f'Total Months: {len(date)}', file=f)
    print(f'Total: ${total}',file=f)
    print(f'Avereage Change: ${int(average)}',file=f)
    print(f'Greatest Increase in Profits: {maxdatediff} (${gincrease})', file=f)
    print(f'Greatest Decrease in Profits: {mindatediff} (${gdecrease})',file=f)
    f.close()
