# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join ("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1 Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

candidate_votes = {}

with open(file_to_load) as election_data:

    #TO do: REad and analyze the data here. 
    file_reader = csv.reader(election_data)

    # REad the header row
    
    headers = next(file_reader)
   

    # Print each row in the CSV file.
    for row in file_reader:

        #2. Add to the total vote count. 
        total_votes += 1

        #4 Print the candidate name from each row
        candidate_name = row[2]
    
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1


print(candidate_votes)



