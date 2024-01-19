#!/usr/bin/env python
'''
create_name_plot.py
  Author(s): Derek Duong (1186760), Haroon Pehlvi (1186425), Jash Vagadia(1200628), Thien Phu Tran/Aaron Tran(1188546)

  Earlier contributors(s): Andrew Hamilton-Wright, Kassy Raymond

  Project: Lab Assignment 4 Script
  Date of Last Update: Mar 1, 2022.

  Functional Summary
      create_name_plot.py reads a CSV file and saves
      a plot based on the data to a PDF file.

     Commandline Parameters: 2
        sys.argv[0] = name of file to read
        sys.argv[1] = name of graphics file to create
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
#"ticktools"
from matplotlib import ticker as ticktools


def main(argv):
    '''
    Create a plot using ranks
    '''

    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 3:
        print(
            "Usage:",
            "Hospitalization_Vaccination_Extract.py <data file> <graphics file>"
        )
        sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]

    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    #
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file",
              csv_filename,
              ": {}".format(err),
              file=sys.stderr)
        sys.exit(-1)

    # You can always print out a data frame if you want to see what is in it
    # though if it is huge, this is not a good idea)
    #print(csv_df)

    # At this point in the file, we begin to do the plotting

    # We must get the figure before we plot to it, or nothing will show up.
    # The matplotlib "figure" is the data environment that we are drawing
    # our plot into.  The seaborn library will draw onto this figure.
    # We don't see seaborn directly refer to "fig" because it is internally
    # drawing on "the current figure" which is the same one we are
    # referencing on this line.
    fig = plt.figure()

    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    ax = sns.lineplot(x="date",
                      y=" Hospitalizations And Vaccination Numbers (At Least One Dose)",
                      hue=" ID",
                      data=csv_df)

    # Set the number of axis labels to 8 -- this can be handy if
    # you are creating a plot that has so many labels that they
    # press in together
    ax.xaxis.set_major_locator(ticktools.MaxNLocator(8))
    # Rotate the ticks on the x-axis to 45 degrees
    plt.xticks(rotation=45, ha='right')

    #plt.margins(0)

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graphics_filename, bbox_inches="tight")

    # Uncomment this line to show the figure on the screen.  Note
    # that in repl.it, you may not be able to close the figure (it may
    # be too big for your screen) so you will have to press [CTRL]-C
    # in order to stop your program in order to be able to run commands
    # in your shell again.
    #plt.show()

    #
    #   End of Function
    #


# python Hospitalization_Vaccination_Create_Graph.py test1.csv test1.pdf
##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)

#
#   End of Script
#
