import os
import csv

#assign file path
election_data_csv = os.path.join('Resources', 'election_data.csv')

# open and read the csv
with open(election_data_csv, 'r') as csvfile:

    #skip header
    csv_header = next(csvfile) 

    #set delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #setting lists to capture each vote name
    candidate_list = []
    
    #pull each vote name
    for row in csvreader:
        candidate_list.append(row[2])
                 
    #get Total Votes
    total_votes = len(candidate_list)

    # #check for each unique candidate (commented out after candidates where identified)
    # candidates = set(candidate_list)
    # print (candidates)
        
    #get each cadidates vote count
    khan_vote = candidate_list.count("Khan")
    correy_vote = candidate_list.count("Correy")
    li_vote = candidate_list.count("Li")
    otooley_vote= candidate_list.count("O'Tooley")

    #decide winner
    if khan_vote > correy_vote and khan_vote > li_vote and khan_vote > otooley_vote:
        winner = "Kanh"
    if correy_vote > khan_vote and correy_vote > li_vote and correy_vote > otooley_vote:
        winner = "Correy"
    if li_vote > khan_vote and li_vote > correy_vote and li_vote > otooley_vote:
        winner = "Li"
    if otooley_vote > khan_vote and otooley_vote > correy_vote and otooley_vote > li_vote:
        winner = "O'Tooley"

# #print results to terminal
print ('Election Results')
print ('------------------------------')
print (f'Total Votes: {total_votes}')
print ('------------------------------')
print (f'Khan: {((khan_vote/total_votes)*100):.2f}% ({khan_vote})')
print (f'Correy: {((correy_vote/total_votes)*100):.2f}% ({correy_vote})')
print (f'Li: {((li_vote/total_votes)*100):.2f}% ({li_vote})')
print (f"O'Tooley: {((otooley_vote/total_votes)*100):.2f}% ({otooley_vote})")
print ('------------------------------')
print (f'Winner : {winner}')
print ('------------------------------')

#set output path
analysis_txt = os.path.join('Analysis', 'analysis_summary.txt')

#open edit text file
with open (analysis_txt, 'w') as f:
    f.write ('Election Results')
    f.write('\n')
    f.write ('------------------------------')
    f.write('\n')
    f.write (f'Total Votes: {total_votes}')
    f.write('\n')
    f.write ('------------------------------')
    f.write('\n')
    f.write (f'Khan: {((khan_vote/total_votes)*100):.2f}% ({khan_vote})')
    f.write('\n')
    f.write (f'Correy: {((correy_vote/total_votes)*100):.2f}% ({correy_vote})')
    f.write('\n')
    f.write (f'Li: {((li_vote/total_votes)*100):.2f}% ({li_vote})')
    f.write('\n')
    f.write (f"O'Tooley: {((otooley_vote/total_votes)*100):.2f}% ({otooley_vote})")
    f.write('\n')
    f.write ('------------------------------')
    f.write('\n')
    f.write (f'Winner : {winner}')
    f.write('\n')
    f.write ('------------------------------')    

