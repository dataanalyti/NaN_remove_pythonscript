import csv
import pandas 

pd = pandas.read_csv('training datset_csv_NaN.csv')
nanremover = pd.dropna()
print(type(nanremover))

with open('training dataset_csv_nanremoved.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(nanremover[2])
    print("done")
print(pd)
print(nanremover)

