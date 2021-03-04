# import the goods
import os
import csv

# opening files

# file to load - the module calls thi direct path
# file_to_load = 'resources/election_results.csv'
# make it os independent 
file_to_load = os.path.join("resources","election_results.csv")
# file we are writing results to
file_to_save = os.path.join("analysis","election_analysis.txt")

# open the input file
election_data = open(file_to_load,'r')
# open the output file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # skip dat header!
    next(file_reader)
    for row in file_reader:
       print(row)
        # print the 1st item on each row
        # print(row[0])

#with open(file_to_save,'w') as txt_file:

# some practice code from before...
    # write some data
    # txt_file.write("Hello World")
    # txt_file.write("Counties in the Election\n------------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")
    # to do: Code to perform analysis
    # print (election_results)
