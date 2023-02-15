# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# The function to write the CSV file

def save_csv(fpath, data):
    """Writes the CSV file to the given path.
    Args:
        fpath (Path): The csv file path.
        data (list): The list of data.
    """
    with open(fpath, "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        for row in data:
            csvwriter.writerow(row)
