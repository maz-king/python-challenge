import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    votes = 0
    livote = []
    khanvote = []
    otooleyvote = []
    correyvote = []

    for row in csvreader:
        votes += 1
        if row[2] == "Li":
            livote.append(row[2])
        if row[2] == "Khan":
            khanvote.append(row[2])
        if row[2] == "O'Tooley":
            otooleyvote.append(row[2])
        if row[2] == "Correy":
            correyvote.append(row[2])

    print(f"Election Results")
    print(f"----------------")
    print(f"Total Votes: {str(votes)}")
    print(f"----------------")
    print(f"Li: {len(livote)} votes")
    print(f"Khan: {len(khanvote)} votes")
    print(f"O'Tooley: {len(otooleyvote)} votes")
    print(f"Correy: {len(correyvote)} votes")