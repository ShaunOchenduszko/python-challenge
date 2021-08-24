import os
import csv

#assign file path
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# open and read the csv
with open(budget_data_csv, 'r') as csvfile:

    #skip header
    csv_header = next(csvfile) 

    #set delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #setting lists and variables
    profit_list = []
    change_list = []
    start_value = 0
    grt_inc = 0
    grt_dec = 0 

    #pull each months profit and change
    for row in csvreader:
        profit_list.append(int(row[1]))
        change_list.append(int(row[1]) - start_value)
        change = (int(row[1]) - start_value)
        start_value = int(row[1])
                
        #loop for getting highest amount
        if change >= grt_inc:
            grt_inc = change
            grt_inc_mnt = row[0]
        #loop for getting lowest amount
        if change <= grt_dec:
            grt_dec = change
            grt_dec_mnt = row[0]

#remove first value from change_list
change_list.pop(0)

#print everything to terminal
print ('Financial Analysis')
print ('------------------------------')
print (f'Total Months: {len(profit_list)}')
print (f'Total: ${sum(profit_list)}')
print (f'Average Change: ${(sum(change_list)/len(change_list)):.2f}')
print (f'Greatest Increase in Profits: {grt_inc_mnt} (${grt_inc})')
print (f'Greatest Decrease in Profits: {grt_dec_mnt} (${grt_dec})')

#set output path
analysis_txt = os.path.join('Analysis', 'analysis_summary.txt')

#open edit text file
with open (analysis_txt, 'w') as f:
    f.write('Financial Analysis')
    f.write('\n')
    f.write('------------------------------')
    f.write('\n')
    f.write(f'Total Months: {len(profit_list)}')
    f.write('\n')
    f.write(f'Total: ${sum(profit_list)}')
    f.write('\n')
    f.write(f'Average Change: ${(sum(change_list)/len(change_list)):.2f}')
    f.write('\n')
    f.write(f'Greatest Increase in Profits: {grt_inc_mnt} (${grt_inc})')
    f.write('\n')
    f.write(f'Greatest Decrease in Profits: {grt_dec_mnt} (${grt_dec})')    

