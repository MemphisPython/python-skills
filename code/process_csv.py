import csv
from sys import argv


def read_college_scorecard_data(filename):
    """Read data from a slice of the College scorecard CSV, printing
    the instate and out of state tuition for women-only schools.

    Some of the column names/numbers are listed below.

    3: INSTNM => Alabama A & M University
    4: CITY => Normal
    5: STABBR => AL
    6: ZIP => 35762
    33: MENONLY => 0
    34: WOMENONLY => 0
    378: TUITIONFEE_IN => 9366
    379: TUITIONFEE_OUT => 17136

    """
    with open(filename) as csvfile:
        for row in csv.reader(csvfile):
            try:
                if int(row[34]) == 1:
                    print(row[3])
                    print("{}, {}".format(row[4], row[5]))
                    print("In-State Tuition: ${}".format(row[378]))
                    print("Out of state Tuition: ${}".format(row[379]))
                    print('--------------------------------')
            except ValueError:
                pass  # Skip rows that don't have numeric data for this colum


def create_alaska_report(filename):
    """Read the College Scorecard CSV, and write a CSV containing a small
    portion of data for Alaska schools.

    """
    data = []  # Empty list to store the columns we want.

    # Read from the original CSV
    with open(filename) as csvfile:
        for row in csv.reader(csvfile):
            if row[5] == "AK":
                data.append([row[3], row[4], row[378]])

    # Write to the new CSV.
    with open('Alaska.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header
        writer.writerow(["School", "City", "Tuition"])

        # Write the rest of the data
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    if len(argv) == 2:
        read_college_scorecard_data(argv[1])
        create_alaska_report(argv[1])
    else:
        print("USAGE: python process_csv.py <file>")
