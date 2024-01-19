#!/usr/bin/env python
'''
extract_cases_to_populution_data.py
  Author(s): Thien Phu Tran/Aaron Tran(1188546)

  Earlier contributors(s): Derek Duong (1186760), Haroon Pehlvi (1186425), Jash Vagadia(1200628), Andrew Hamilton-Wright, Kassy Raymond

  Project: Project KickOff Lab Script
  Date of Last Update: Mar 27, 2022

  Functional Summary
      extract_cases_to_populution_data.py reads country names from a 
      text file and then extracts data from a CSV file, printing out
      select fields. It then turns the data into a 100% stacked bar graph
      

     Commandline Parameters: 3
        argv[1] = the CSV file with information
        argv[2] = the text file with country names
        argv[3] = the name of the graphic file to create
       
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


#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#

import matplotlib.pyplot as plt
def main(argv):

    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 4:
        print("Usage: compare_dates.py <file name>")
        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    #create variables from arguments
    country_info = argv[1]
    country_list = argv[2]
    graphics_filename = argv[3]

    
    try:
        covidStatsFile_fh = open(country_info, encoding="utf-8-sig")
    except IOError as err:
        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        print("Unable to open file fileProcessname'{}' : {}".format(
            covidStatsFile_fh, err),
              file=sys.stderr)
        sys.exit(1)

    covidStatsReader = csv.reader(covidStatsFile_fh)

    #splits data inside file


    #sets up variables
    count = 0
    total = 0
    country_name = []
    name_array = []
    cases_array = []
    population_array = []
    pop_without_cases_array = []
    case_percent = []
    pop_percent = []

    #reads and stores country names from text file
    f = open(country_list, 'r')

    for line in f: 
      country_name.append(line.strip())
      #print(country_name[count])
      total = count + 1
      count+=1
    
      
    #reinitialize variables and arrays
    count = 0
    name_array = [0] * total
    cases_array = [0] * total 
    population_array = [0] * total
    pop_without_cases_array = [0] * total
    case_percent = [0] * total
    pop_percent = [0] * total
  
    for row_data_fields in covidStatsReader:
        
        #prints the header on the first line
        if (count == 0): 

            print(row_data_fields[0], end=",")
            print(row_data_fields[1], end=",")
            print(row_data_fields[2], end="")
          
            print("")
            count+=1     
        #begins storing values to arrays
        for x in range(total):
          if (country_name[x] == row_data_fields[0]): 
  
              name_array[x] = row_data_fields[0]
            
              if (row_data_fields[1] != ''):
                total_cases = int(row_data_fields[1].replace(',',''))
                cases_array[x] = total_cases
                
              if (row_data_fields[2] != ''):
                population = int(row_data_fields[2].replace(',',''))
                population_array[x] = population

              #sets up the percentage elements to be used for the graph
              #sets up population without cases variable to better represent 
              #percentage of cases to population
              
              pop_without_cases_array[x] = population_array[x] - cases_array[x]
              case_percent[x] = cases_array[x] / population_array[x]
              pop_percent[x] = pop_without_cases_array[x] / population_array[x]
            
    #prints values from array
    for i in range(0,total):
      for j in range(0,total):
        if (country_name[i] == name_array[j]):
          print(name_array[j], end=",")
          print(cases_array[j], end=",")
          print(population_array[j], end="")
          print("")
    

  
    
    #sets up graph elements
    fig, ax = plt.subplots()
    
    ax.bar(country_name, case_percent, label='Total Cases %')
    ax.bar(country_name, pop_percent, bottom=case_percent,
           label='Population %')
    
    ax.set_ylabel('Percentage of Cases vs Popululation')
    ax.set_title('Total Cases vs Total Population: 100% Stacked Bar Graph')
    ax.legend()


    #prints the graph to graphics_filename
    fig.savefig(graphics_filename, bbox_inches="tight")
  
    #plt.show()
             
        


## Call our main function, passing the system argv as the parameter
main(sys.argv)

#
#   End of Script
#   Command lines for testing below

#   python Aaron/extract_cases_to_population_data.py Aaron/cases_to_population2022-03-15.csv Aaron/country_names1.txt Aaron/CTP_plot1.pdf

#   python Aaron/extract_cases_to_population_data.py Aaron/cases_to_population2022-03-15.csv Aaron/country_names1.txt Aaron/CTP_plot1.pdf > Aaron/CTP_plot1.csv

#   python Aaron/extract_cases_to_population_data.py Aaron/cases_to_population2022-03-15.csv Aaron/country_names2.txt Aaron/CTP_plot2.pdf

#   python Aaron/extract_cases_to_population_data.py Aaron/cases_to_population2022-03-15.csv Aaron/country_names2.txt Aaron/CTP_plot2.pdf > Aaron/CTP_plot2.csv