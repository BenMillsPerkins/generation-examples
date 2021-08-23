import csv

sales_data = []

with open('sales_data.csv', 'r') as file:
    csvDictReader = csv.DictReader(file, fieldnames=['customer_id','purchase_date','purchase_amount','product_id'])
    next(csvDictReader)
    
    for row in csvDictReader:
        if '' in row.values():
            continue
        sales_data.append(row)

customer_spend = {}

for sale in sales_data:
    customer_id = sale['customer_id']
    if customer_spend.get(customer_id):
        customer_spend[customer_id] += float(sale['purchase_amount'])
    else:
        customer_spend[customer_id] = float(sale['purchase_amount'])
    
print(customer_spend)