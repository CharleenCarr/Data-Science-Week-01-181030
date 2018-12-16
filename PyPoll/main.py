import os
import csv

pypollstarter_csv = os.path.join("..", "PyPoll", "election_data.csv")

# List to store data
total_votes = 0
candidate_name = []
candidate_names = []
candidate_list = []
total_candidate_list = []
total_percentage_votes = {}
total_candidate_votes = {}
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
        else:
            total_candidate_votes[candidate_name] += 1

    for name, votes in total_candidate_votes.items():

        total_percentage_candidate_round[name] = round((total_candidate_votes[name]/total_votes)*100,3)

output_file = os.path.join("pypollfinal.txt")

with open(output_file, "w", newline="") as datafile:

    print("```text")
    print("Election Results")
    print("------------------------------------------")
    print("Total Votes:  ", total_votes)
    print("------------------------------------------")

    datafile.write('```text'+ '\n')
    datafile.write('Election Results' + '\n')
    datafile.write("---------------------------------------------" + '\n')
    datafile.write('Total Votes:  {}'.format(total_votes) + '\n')
    datafile.write("---------------------------------------------" + '\n')

    max = 0

    for key, value in total_percentage_candidate_round.items():

        if value > max:

            max = value
            winner = key

        string = str(key) + ": " + str(value) + "% (" + str(total_candidate_votes[key]) + ")"

        print(string)

        string = str(key) + ": " + str(value) + "% (" + str(total_candidate_votes[key]) + ")\n"
        datafile.write(string)

    print("------------------------------------------")
    print("Winner:  " + winner)
    print("------------------------------------------")
    print("```")

    datafile.write("---------------------------------------------" + '\n')
    datafile.write("Winner:  " + winner + '\n')
    datafile.write("---------------------------------------------" + '\n')
    datafile.write("```")