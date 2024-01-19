'''
resolved.py
  Author(s): Jash Vagadia(1200628)

  Earlier contributors(s): Andrew Hamilton-Wright, Kassy Raymond

  Project: Project KickOff Lab Script (Iteration 0)
  Date of Last Update: Mar 20, 2022

  Functional Summary
      resolved.py takes in a CSV (comma separated version) file
      and prints out several of the fields.

     Commandline Parameters: 1
        argv[0] = File name
        argv[1] = Start date in the format dd-mm-yyyy
        argv[2] = End date in the format dd-mm-yyyy
        argv[3] = Provience for which you need to find the resolved case average
'''

#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn
import csv

# The 'datetime' module gives us lots of tools to store and compare
# time information.  Here we only import the "date" tool from the
# datetime module
from datetime import datetime

#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#

def main():
    args = sys.argv[1:]
    print('Arguments: ', args)
    dateStart = args[1]
    dateEnd = args[2]
    prov=args[3]

    date_time_obj_start = datetime.strptime(dateStart, '%d-%m-%Y')
    date_time_obj_end = datetime.strptime(dateEnd, '%d-%m-%Y')

    date_range= date_time_obj_end - date_time_obj_start
    print("date range: ")
    print(date_range) 


    try:
        recoveredFile_fh = open(
            "recovered_timeseries_prov.csv", encoding="utf-8-sig")
    except IOError as err:
        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        print("Unable to open file fileProcessname'{}' : {}".format(
            "recoveredFile_fh", err),
            file=sys.stderr)
        sys.exit(1)

    recoveredReader = csv.reader(recoveredFile_fh) 
    #splits data inside file
    count = 0
    sum=0
    for row_data_fields in recoveredReader:
        #print(row_data_fields)
        #prints the header on the first line
        if (count == 0):  
          print(row_data_fields[0], end=",")
                        
          print(row_data_fields[1], end=",")
            
          print(row_data_fields[2], end=",")
            
          print(row_data_fields[3], end="")
          print("")
          count+=1   
        elif (count >= 1):
            #takes the date from the first line
            #turns it into a datetime class
            rowProv = row_data_fields[0]
            dateVar = row_data_fields[1]
            dailyCaseCount = int(row_data_fields[2])
            date_time_obj = datetime.strptime(dateVar, '%d-%m-%Y')
            if(rowProv == "Alberta") and (date_time_obj>=date_time_obj_start) and (date_time_obj<=date_time_obj_end):
                sum += dailyCaseCount
            count+=1

    #print('Sum: ', sum)

    avg = sum / (date_range.days)

    print('Resolved case Average for provience {0} is {1}: '.format(prov,avg)) 


if __name__ == "__main__":
  main() 

  #python resolved.py -resolved 12-02-2020 28-02-2021 Alberta   