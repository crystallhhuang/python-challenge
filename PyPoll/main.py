import csv

total_votes = 0
candidates = {}
winner = ''
most_votes= 0

with open ('election_data.csv','r',newline='')as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1 
        candidates[row[2]] = candidates.get (row[2],0) +1
print ("Election Results")
print (f"Total Votes:{total_votes}")

for name , count in candidates.items():
    vote_pct = count/total_votes
    print ("{}:{:.3%} ({:,})".format(name, vote_pct,count))

    if most_votes < count:
        most_votes = count
        winner = name 

print (f"Winner:{winner}")



    
