# import the goods
import os
import csv

# opening files

# make it os independent 
# input file
file_to_load = os.path.join("resources","election_results.csv")
# file we are writing results to
file_to_save = os.path.join("analysis","election_analysis.txt")

# initialize the counter, candidate list, votes dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

# open the input file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # get the header
    headers = next(file_reader)
    for row in file_reader:
       total_votes += 1
       candidate_name = row[2]
       # get unique candidate names and set their vote count to zero
       if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0
        
       candidate_votes[candidate_name] += 1

#for thief in candidate_options:
for thief in candidate_votes:
    print (f"{thief}: received {(candidate_votes[thief] / total_votes):.1%} of the vote.")  

# print(total_votes)
# print(candidate_options)
# print(candidate_votes)
# with open(file_to_save,'w') as txt_file:
# some practice code from before...
    # write some data
    # txt_file.write("Hello World")
    # txt_file.write("Counties in the Election\n------------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")
