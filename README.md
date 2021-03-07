# Election_Analysis

## Project Overview
The Colorado Board of Elections has requested an audit of the results of a recent local congressional election.  In particular, they have requested: 

   1. Calculate and verify the total votes cast.
   2. List all the candidates who received votes and for each candidate:
      1. Calculate their total votes
      2. Calculate the percentage of the total votes won
   3. Determine the winner based on the popular vote

## Resources
  * Input: election_results.csv - provided by the BOE, this is a CSV formatted file containing Ballot ID, County, and Candidate
  * Software: Python 3.7.9, VS Code 1.5.2, Git Bash 4.4.23

## Results
The results of the audit are:   
  * Total votes cast: 369,711  
  * Vote details by County:   
    - Jefferson: 10.5% of the total with 38,855 votes
    - Denver: 82.8% of the total with 306,055 votes
    - Arapahoe: 6.7% of the total with 24,801 votes

  * Denver county had the largest number of votes (306,055)
  * Vote details by Candidate:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
    - Diana DeGette received 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes

  * The election winner is:
    * **Diana DeGette** who received 73.8% of the vote and 272,892 votes

The audit results are also available here:
* [Audit Results](https://github.com/goldbala55/Election_Analysis/blob/main/analysis/election_results.txt)

## Post-Audit Summary
This election audit tool was written for reusability and can be run against any election results using the same feed input format. However, with some additional details in the input feed, further enhancements can be made to provide:
* the results from multiple Congressional districts from one feed (add a district column)
* the results of multiple election contests (add a column describing the contest - Senator, Governor, etc )
* enhanced vote analysis - check for duplicates, compare totals by County to registration totals, etc.