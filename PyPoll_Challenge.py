# import required modules
import os
import csv

# make path locations os independent 
# input file
file_to_load = os.path.join("resources","election_results.csv")
# output file
file_to_save = os.path.join("analysis","election_results.txt")

# initialize counters, candidate and county list, votes dictionary, winning results
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
winning_percentage = 0

county_options = []
county_votes = {}
largest_county = ''
largest_count = 0

# open the input file and count votes
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # skip the header
    headers = next(file_reader)
    # now loop through the votes and get totals per candidate
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        county_name = row[1]
        # get unique candidate names and initialize their count
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # bump the candidate count
        candidate_votes[candidate_name] += 1

        # get unique county names and and initialize their count
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0

        # bump the county count
        county_votes[county_name] += 1

# open the output file for reporting
#   note that writing to files vs terminal requires slightly different format
#   to account for how new lines (\n) are handled 
#   it seems there are some options possible in the csv module to handle this.
#   but outside my scope and time limitations.  TBD
with open(file_to_save, "w") as txt_file:
    # format the results 
    election_results = (
    f"\nElection Resuts\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
)
    # write the results to the screen and file
    print (election_results)
    txt_file.write(election_results)

    # print county section header
    print("County Votes:")
    txt_file.write("\nCounty Votes:\n")

    # Loop through the county votes to calculate percentage and the largest 
    for county_name in county_votes:
        votes = county_votes[county_name]    
        vote_percentage = 100 * county_votes[county_name] / total_votes
        
        # format the county results to print
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})")
        
        # write the county results to the screen and file
        print(county_results)
        txt_file.write(county_results + "\n")

        # determine the largest county vote
        if (votes >largest_count):
            largest_count = votes
            largest_county = county_name
    
    #format and print results
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n"
    )
    
    print(largest_county_summary)
    txt_file.write(largest_county_summary)

    # Loop through the candidate votes to calculate percentage and the winner
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

    # format and print results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)