#Import csv module
import csv 

#Start csv file handling
with open('Resources/budget_data.csv') as file: # file = with open(')

    #Specify delimiter and variable that holds contents
    file_reader = csv.reader(file, delimiter=',') 
    header=next(file_reader)

    #Determine the variables:
    #List "months" for the "Date" column
    months=[] 
    
    #List named "profitlosses" for the "Profit/Losses" column
    profitlosses=[] 

    #List of conditions
    total=0
    a_change=0
    m_change=0
    m_count=0
    delta1=0
    delta2=0
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

    #Sort each row of data after the header and write data into assigned lists
    for row in file_reader:
        #Column '0' as month
        month=row[0] 
       
       #Column 1 as profitloss
        profitloss=row[1] #Assign 
        
        #Add next line to list months
        months.append(month) #
        
        #Add next line to list profitlosses  
        profitlosses.append(profitloss) 
    
    #Count the total of months in the "Date" column
    m_count = len(months) 
    #print(m_count)

    #Begin data analysis

#First loop is through list profitlosses (variable loop1 as loop index counter)
for loop1 in range (m_count):

#Calculate total amount   
    total=total+int(profitlosses[loop1]) 


#Second loop is through list profitlosses (variable loop2 as loop index counter)
#To avoid overflow - resitrict the loop (last line +1)
for loop2 in range (m_count-1): 
    a_change=a_change+(float(profitlosses[loop2+1])-float(profitlosses[loop2])) #Calculate sum of changes

#print(a_change/(m_count-1))
    m_change=(float(profitlosses[loop2+1])-float(profitlosses[loop2])) #Calculate monthly change
    
    #Determine greatest increase
    if m_change>delta1: 
        delta1=m_change
        delta_line1=loop2
    else:
        delta1=delta1

#print(delta1)
#print(months[delta_line1+1])

     #Determine greatest decrease
    if m_change<delta2:
        delta2=m_change
        delta_line2=loop2
    else:
        delta2=delta2

#print(delta2)
#print(months[delta_line2+1])

#generate output lines

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

#Output results on screen
print(analysis) 

with open("FinancialAnalysis.txt", "w") as file:
    file.write(analysis)