#!/usr/bin/env python
'''
compare_dates.py
  Author(s): Derek Duong (1186760), Haroon Pehlvi (1186425), Jash Vagadia(1200628), Thien Phu Tran/Aaron Tran(1188546)

  Earlier contributors(s): Andrew Hamilton-Wright, Kassy Raymond

  Project: Project KickOff Lab Script (Iteration 0)
  Date of Last Update: Mar 1, 2022

  Functional Summary
      compare_dates.py takes in a CSV (comma separated version) file
      and prints out several of the fields.

     Commandline Parameters: 1
        argv[1] = the starting year to read from
        argv[2] = the starting month to read from
        argv[3] = the starting day to read from
        argv[4] = the ending year to read from
        argv[5] = the ending month to read from
        argv[6] = the ending day to read from
        argv[7] = the name of the file to read hospitalizations
        argv[8] = name of the input file containing the data for vaccines
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
from datetime import date

#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#


def main(argv):

    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 9:
        print("Usage: compare_dates.py <file name>")
        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    #create variables from arguments
    yearStart = int(argv[1])
    monthStart = int(argv[2])
    dayStart = int(argv[3])
    yearEnd = int(argv[4])
    monthEnd = int(argv[5])
    dayEnd = int(argv[6])
    fileProcessNameHospitalizations = argv[7]
    fileProcessNameVaccine = argv[8]

    try:
        hospitalStatsFile_fh = open(fileProcessNameHospitalizations,
                                    encoding="utf-8-sig")
    except IOError as err:
        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        print("Unable to open file fileProcessname'{}' : {}".format(
            hospitalStatsFile_fh, err),
              file=sys.stderr)
        sys.exit(1)

    #Tries to open vaccine file
    try:
        vaccineStatsFile_fh = open(fileProcessNameVaccine,
                                   encoding="utf-8-sig")
    except IOError as err:
        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        print("Unable to open file fileProcessname'{}' : {}".format(
            vaccineStatsFile_fh, err),
              file=sys.stderr)
        sys.exit(1)

    #hospital and vaccine csv readers
    hospitalStatsReader = csv.reader(hospitalStatsFile_fh)
    vaccineStatsReader = csv.reader(vaccineStatsFile_fh)

    #list to store hospitalization dates and their numbers
    hospitalDates = list()
    hospitalNumbers = list()

    #lists to store culmative vaccination rates and their dates
    vaccineNumbers = list()

    #find start dates from text file for hospitalizations
    rowOneReadHosp = 0
    bool = 0
    for row_data_fields in hospitalStatsReader:

        if (rowOneReadHosp == 0):
            #Prints out the headers for "date" and "hospitalizations"
            print(row_data_fields[0], end=", ")
            print("Hospitalizations And Vaccination Numbers (At Least One Dose)", end=", ")
            rowOneReadHosp = 1

        elif rowOneReadHosp == 1:
            ##take the date from the file and compare with input
            dateVar = row_data_fields[0]
            dateObject = date.fromisoformat(dateVar)

            #check if dateOject dates match the required dates (BEGINNING)
            if (dateObject.year == yearStart and dateObject.month == monthStart
                    and dateObject.day == dayStart):

                bool = 1

            if (bool == 1):
                #Take the date and store it into date list
                hospitalDates.append(row_data_fields[0])

                #take the hospitalization number and store it into list
                hospitalNumbers.append(row_data_fields[4])
                #print("{},{}".format(row_data_fields[0], row_data_fields[4]))

                if (dateObject.year == yearEnd and dateObject.month == monthEnd
                        and dateObject.day == dayEnd):
                    #breaks out of loop if end date is reached
                    break

    ##############
    #VACCINE DATA#
    ##############
    rowOneReadVacc = 0
    bool = 0

    index = -1
    for row_data_fields_vacc in vaccineStatsReader:

        if (rowOneReadVacc == 0):
            #Prints out the headers for At least one dose_cumulative and ID
            print("ID")
            rowOneReadVacc = 1

        elif rowOneReadVacc == 1:
            ##take the date from the file and compare with input

            dateVarVacc = row_data_fields_vacc[0]
            dateObjectVacc = date.fromisoformat(dateVarVacc)

            #check if dateOject dates match the required dates (BEGINNING)
            if (dateObjectVacc.year == yearStart
                    and dateObjectVacc.month == monthStart
                    and dateObjectVacc.day == dayStart):
                bool = 1

            if (bool == 1):

                if (row_data_fields_vacc[1] == "12-17yrs"):
                    #take the hospitalization number and store it into lis
                    #print("APPENDED: %d" % (int)(row_data_fields_vacc[3]))
                    vaccineNumbers.append((int)(row_data_fields_vacc[2]))
                    index += 1
                else:
                    #Take the date and store it into date list
                    vaccineNumbers[index] = (int)(
                        vaccineNumbers[index]) + (int)(row_data_fields_vacc[2])
                    #print("ADDED: %d" % (int)(row_data_fields_vacc[3]))

                if (dateObjectVacc.year == yearEnd
                        and dateObjectVacc.month == monthEnd
                        and dateObjectVacc.day == dayEnd and
                        row_data_fields_vacc[1] == "Undisclosed_or_missing"):
                    #breaks out of loop if end date is reached
                    break

    #iterates through lists
    i = 0
    while i < len(hospitalDates):
        print(hospitalDates[i], end=", ")
        print("%d" % (int(hospitalNumbers[i]) * 10000), end=", ")
        print("Hospitalizations(Scaled up x10 000)")
        print(hospitalDates[i], end=", ")
        print(vaccineNumbers[i], end=", ")
        print("Vaccinations")
        i = i + 1

        #Run data
        # python Derek/Hospitalization_Vaccination_Extract.py 2021 4 4 2022 1 3 Derek/hospital.csv Derek/vaccines_by_age.csv


## Call our main function, passing the system argv as the parameter
main(sys.argv)

#
#   End of Script
#

#creates datetime variable of the current date
# stores string with format "year-month-day"
#dateVar = row_data_fields[0]

#prints out header
#if count == 0:
# print(row_data_fields[0], end = ",")
# print(r
