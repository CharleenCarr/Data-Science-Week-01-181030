import os
import csv

pybankstarter_csv = os.path.join("..", "PyBank", "budget_data.csv")

# lists to store data
month = 0
total_months = 0
total_revenue = 0
prev_revenue = 0
revenuechange_list = []
greatest_rev_inc = 0
greatest_rev_dec = 0
rev_change_mon = ""
greatest_rev_inc_mon = ""
greatest_rev_dec_mon = ""

with open(pybankstarter_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_months += 1
        total_revenue = total_revenue + int(row[1])
        revenue_change = int(row[1]) - prev_revenue
        rev_change_mon = row[0]
        revenuechange_list.append(revenue_change)
        prev_revenue = int(row[1])
        if revenue_change > greatest_rev_inc:
            greatest_rev_inc = revenue_change
            greatest_rev_inc_mon = rev_change_mon
        if revenue_change < greatest_rev_dec:
            greatest_rev_dec = revenue_change
            greatest_rev_dec_mon = rev_change_mon

    revenuechange_list = revenuechange_list[1:]

    avg_revenue_change = sum(revenuechange_list) / len(revenuechange_list)
    avg_revenue_round = round(avg_revenue_change, 2)

    print("```text")
    print("Financial Analysis")
    print("--------------------------------------------------")
    print("Total Months:  ", total_months)
    print("Total:  ", '$' + str(total_revenue))
    print("Average Change:  ", '$' + str(avg_revenue_round))
    print("Greatest Increase in Profits:  ", greatest_rev_inc_mon, "(" + '$' + str(greatest_rev_inc) + ")")
    print("Greatest Decrease in Profits:  ", greatest_rev_dec_mon, "(" + '$' + str(greatest_rev_dec) + ")")
    print("```")

output_file = os.path.join("pybankfinal.txt")

with open(output_file, "w", newline="")as datafile:
    datafile.write('```text' + '\n')
    datafile.write('Financial Analysis' + '\n')
    datafile.write("--------------------------------------------------" + '\n')
    datafile.write('Total Months:  {}'.format(total_months) + '\n')
    datafile.write('Total:  ''${}'.format(total_revenue) + '\n')
    datafile.write('Average Change:  ''${}' .format(avg_revenue_round) + '\n')
    datafile.write('Greatest Increase in Profits:  ' + greatest_rev_inc_mon)
    datafile.write("  " + '(${})'.format(greatest_rev_inc) + '\n')
    datafile.write('Greatest Decrease in Profits:  ' + greatest_rev_dec_mon)
    datafile.write("  " + '(${})'.format(greatest_rev_dec) + '\n')
    datafile.write('```')