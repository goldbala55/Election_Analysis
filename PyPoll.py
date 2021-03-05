# import the goods
import os
import csv

# make it os independent 
# input file
file_to_load = os.path.join("resources","election_results.csv")
# output file
file_to_save = os.path.join("analysis","election_analysis.txt")

# initialize the counter, candidate list, votes dictionary, winning results
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# open the input file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # get the header
    headers = next(file_reader)
    # now loop through the votes and get totals per candidate
    for row in file_reader:
       total_votes += 1
       candidate_name = row[2]
       # get unique candidate names and set their vote count to zero
       if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0
        
       candidate_votes[candidate_name] += 1

# open the output file
with open(file_to_save, "w") as txt_file:
    # format the results 
    election_results = (
    f"\nElection Resuts\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
)
    # write the results to the screen and file
    print (election_results, end="")
    txt_file.write(election_results)

    # Loop through the vote to calculate percentage and the winner
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]    
        vote_percentage = 100 * candidate_votes[candidate_name] / total_votes
        
        # format the candidate results to print
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}) \n")
        
        # write the candidate results to the screen and file
        print(candidate_results)
        txt_file.write(candidate_results)

        # determine the winner based on votes and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

