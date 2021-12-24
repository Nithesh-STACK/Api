import csv
from os import CLD_EXITED
input_file = csv.DictReader(open('output.csv'))
data = []
for i in input_file:
            data.append(i)
# for i in data:
#             if len(i['Balance']) > 2:
#                 balance = float(i['Balance'].replace(",", ""))
#                 print (balance)
#             if len(i['Txn Date']) > 2:
#                 if len(i['Credit']) > 2:
#                     credit = float(i['Credit'].replace(",", ""))
#                     print ('credit for month', i['Txn Date'], ' :', credit)
#                     debit_int = 0
#                 elif len(i['Debit']) > 2:
#                     debit_int = float(i['Debit'].replace(",", ""))
#                     print ('Debit for month', i['Txn Date'], ' :', debit_int)
#                     credit = 0
#                 else:
#                     print('No Transactions')

#print(data)
credits=0
debits=0
balance=0
for i in data:
    if(len(i['Credit'])>0):
         print(len(i['Credit']))
         credits+=float(i["Credit"])
    if(len(i['Debit'])>0):
         print(len(i['Debit']))
         debits+=float(i["Debit"])

balance=data[-1]["Balence"]
print(credits)
print(debits)
print(balance)
res=[]
res.append(credits)
res.append(debits)
res.append(balance)
