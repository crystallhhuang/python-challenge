import csv 

total_month = 0
total_profit = 0
date_max_increase =''
date_max_decrease =''
greatest_increase = 0
greatest_decrease = 0



with open ('budget_data.csv','r',newline='')as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    next(csv_reader)

    for row in csv_reader:
        total_month += 1 
        total_profit += int(row[1])
        average_change = total_profit / total_month

        if (greatest_increase < int(row[1])):
            greatest_increase = int (row[1])
            date_max_increase = (row[0])

        if (greatest_decrease > int(row[1])):
            greatest_decrease = int (row[1])
            date_max_decrease = (row[0]) 

print (f"Total Months:{total_month}")
print (f"Total: ${total_profit}")
print (f"average_change: ${average_change}")
print (f"Greatest Increase in Profits:{date_max_increase}${(greatest_increase)}")
print (f"Greatest decrease in Profits:{date_max_decrease}${(greatest_decrease)}")