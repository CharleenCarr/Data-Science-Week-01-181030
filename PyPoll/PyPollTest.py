import os
import csv

pypollstarter_csv = os.path.join("..", "PyPoll", "election_data.csv")

# List to store data
total_votes = 0
candidate_names = []
total_candidate_votes = {}
total_percentage_votes = {}
total_percentage_candidate_votes = {}
total_percentage_candidate_round = {}
winner_candidate = ""
winner_count = 0

with open(pypollstarter_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            total_candidate_votes[candidate_name] = 0
        total_candidate_votes[candidate_name] += 1
        # elif candidate_name in candidate_names[0]:
        #     total_candidate_votes[0] += 1
        # elif candidate_name in candidate_names[1]:
        #     total_candidate_votes[1] += 1
        # elif candidate_name in candidate_names[2]:
        #     total_candidate_votes[2] += 1
        # elif candidate_name in candidate_names[3]:
        #     total_candidate_votes[3] += 1

    total_percentage_candidate_votes[candidate_name] = (total_candidate_votes[candidate_name] / total_votes) * 100
    total_percentage_candidate_round[candidate_name] = round(total_percentage_candidate_votes[candidate_name],3)

    #print(total_candidate_votes)
    #print(total_percentage_candidate_votes)
    print("Election Results")
    print("------------------------------------------")
    print("Total Votes:  ", total_votes)
    print("------------------------------------------")
    print(candidate_name, total_percentage_candidate_round[candidate_name], total_candidate_votes[candidate_name])


    # print(str(total_percentage_candidate_votes) + str(total_candidate_votes[candidate_name]))
#     print("Correy:  ", '$' + str(avg_revenue_round))
#     print("Li:  ", greatest_rev_inc_mon, '$' + str(greatest_rev_inc))
#     print("O'Tooley:  ", greatest_rev_dec_mon, '$' + str(greatest_rev_dec))
#         #if candidates == candidatelist.index(candidates):
#         #total_candidatelist.append(candidatelist)

output_file = os.path.join("pypollfinal.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results' + '\n')
    datafile.write("--------------------------------------------------" + '\n')
    datafile.write('Total Votes:  {}'.format(total_votes) + '\n')
    datafile.write('--------------------------------------------------' + '\n')
    datafile.write('Khan:  '.format(total_percentage_candidate_round) .format(total_candidate_votes[candidate_name]) + '\n')
    datafile.write('Correy:  '.format(total_percentage_candidate_round) .format(total_candidate_votes[candidate_name]) + '\n')
    datafile.write('Li:  '.format(total_percentage_candidate_round) .format(total_candidate_votes[candidate_name]) + '\n')
    datafile.write("O'Tooley:  ".format(total_percentage_candidate_round) .format(total_candidate_votes[candidate_name]) + '\n')
    datafile.write('--------------------------------------------------' + '\n')
    datafile.write('Winner:  Khan'.format(winner_candidate) + '\n')
    datafile.write('--------------------------------------------------' + '\n')
