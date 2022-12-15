'''
Script that processes a CSV file containing information about mobile phone plans and generates three new CSV files as output.
The script uses the pandas library to read and manipulate the data.
'''

import pandas

'''
function takes in a pandas DataFrame called merged and exports it as a CSV file called "file1.csv",
with only the columns "MDN", "Resale Plan", "Sprint Plan", and "SOCs"
'''
def make_file1(merged):

    merged.to_csv("file1.csv", index=False, columns=["MDN","Resale Plan","Sprint Plan","SOCs"])

'''
function takes in the same merged DataFrame and creates a new column called "LTE SOC", 
which indicates whether the device has an LTE SOC (a type of hardware component) based on the values in the "SOCs" column
It then exports the resulting DataFrame as a CSV file called "file2.csv".
'''
def make_file2(merged):

    lte_soc = []
    for row in merged['SOCs']:
        if 'DSMLTESOC' in str(row):
            lte_soc.append('Y')
        else:           
            lte_soc.append('N')

    merged['LTE SOC'] = lte_soc
    merged.to_csv("file2.csv", index=False, columns=["MDN","Resale Plan","Sprint Plan","LTE SOC"])

'''
function takes in the merged DataFrame, groups the data by the "Resale Plan" column, and counts the number of devices for each plan
It exports the resulting DataFrame as a CSV file called "file3.csv".
'''
def make_file3(merged):

    merged_group = merged.groupby(['Resale Plan'])['Resale Plan'].count().reset_index(name="Number of Devices")
    merged_group.to_csv("file3.csv", index=False, columns=["Resale Plan", "Number of Devices"])

'''
function reads in the input CSV files using pandas, merges them into a single DataFrame, and renames some of the columns.
It then calls the three previously described functions to generate the output CSV files
'''
def main():

    carrier = pandas.read_csv("carrier-plans.csv")
    resale  = pandas.read_csv("resale-plans.csv")
    merged = pandas.merge(resale, carrier, on='mdn', how='left')
    merged.rename(columns={'mdn': 'MDN', 'resale_plan': 'Resale Plan', 'sprint_plan': 'Sprint Plan', 'socs': 'SOCs'}, inplace=True)
    make_file1(merged)
    make_file2(merged)
    make_file3(merged)


if __name__ == "__main__":
    main()


