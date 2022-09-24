import csv
import gspread
import time
import decimal

MONTH = 'july'

file = f"dsk_{MONTH}.csv"

transactions = []

BILLS_NAMES = {"BGR Sofia ePay Gas  Heating PCI", "BGR Sofia ePay water",
               "BGR Sofia ePay electricity", "BGR Sofia ePay Internet services"}

def dskFin(file, BILLS_NAMES):

    with open(file, encoding="utf8", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[3]
            amount = float(row[9])
            category = 'other'
            if name == "USA 4029357733 PAYPAL  HUMBLEBUNDL HU 16":
                category = "Humble Bundle"
            if name == "BGR PLOVDIV LIDL BALGARIYA EOOD BUL  BAL":
                category = "Food"
            if name == "DEU 4259855734 PAYPAL  STEAM GAMES Rodin":
                category = "Steam"
            if name == "BGR SLIVEN DASKALOVI FARMA EOOD":
                category = "Pharmacy"
            if name == "BGR PLOVDIV ATM R DASKALOV 2 RAIKO DASKA":
                category = "ATM"
            if name in BILLS_NAMES:
                category = "Bills"

            transaction = (date, name, amount, category)
            print(transaction)
            transactions.append(transaction)
        return transactions


sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = dskFin(file, BILLS_NAMES)

for row in rows:
    wks.insert_row([row[0], row[1], row[3], row[2]], 8)
    time.sleep(2)