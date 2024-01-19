#!/usr/bin/env python

'''
create_name_plot.py
  Author(s): Derek Duong (1186760), Haroon Pehlvi (1186425), Jash Vagadia(1200628), Thien Phu Tran/Aaron Tran(1188546)

  Earlier contributors(s): Andrew Hamilton-Wright, Kassy Raymond

  Project: Lab Assignment 4 Script
  Date of Last Update: Mar 1, 2022.

  Functional Summary
      creates graph for resolved cases for each provience
      
	  Commandline Parameters: 2
        sys.argv[0] = name of file to read
        sys.argv[1] = name of the  graph file to create
'''

#
#   Packages and modules
#
import sys

# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns

from matplotlib import pyplot as plt

# this imports tools for "ticks" along the x and y-axes and calls them
# "ticktools"
from matplotlib import ticker as ticktools


def main():
    # Create a plot using ranks
    # Create a plot using ranks
    # Check that we have been given the right number of parameters,
    # and store the single command line argument in a variable with
    # a better name
    args = sys.argv
    if len(args) != 3:
        print("Usage:", "death.py <data file> <graph file>")

    csv_filename = args[1]
    graph_filename = args[2]

    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
              ": {}".format(err), file=sys.stderr)
        sys.exit(-1)


        # # We will get the figure before we plot to it, or nothing will show up.
        # The matplotlib "figure" is the data environment that we are drawing
        # our plot into.  The seaborn library will draw onto this figure.
        # We don't see seaborn directly refer to "fig" because it is internally
        # drawing on "the current figure" which is the same one we are
        # referencing on this line.
    fig = plt.figure()

    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    ax = sns.lineplot(x="date_death_report", y="deaths", hue= "province",  data=csv_df)

    # Set the number of axis labels to 8 -- this can be handy if
    # you are creating a plot that has so many labels that they
    # press in together
    ax.xaxis.set_major_locator(ticktools.MaxNLocator(10))

    # Rotate the ticks on the x-axis to 45 degrees
    plt.xticks(rotation=45, ha='right')

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graph_filename, bbox_inches="tight")

    #
    #   End of Function
    #

if __name__ == "__main__":
    main()
#
#   End of Script
