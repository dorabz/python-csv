import pandas


def make_file1(merged):

    merged.to_csv("file1.csv", index=False, columns=["MDN","Resale Plan","Sprint Plan","SOCs"])


def make_file2(merged):

    lte_soc = []
    for row in merged['SOCs']:
        if 'DSMLTESOC' in str(row):
            lte_soc.append('Y')
        else:           
            lte_soc.append('N')

    merged['LTE SOC'] = lte_soc
    merged.to_csv("file2.csv", index=False, columns=["MDN","Resale Plan","Sprint Plan","LTE SOC"])


def make_file3(merged):

    merged_group = merged.groupby(['Resale Plan'])['Resale Plan'].count().reset_index(name="Number of Devices")
    merged_group.to_csv("file3.csv", index=False, columns=["Resale Plan", "Number of Devices"])


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


