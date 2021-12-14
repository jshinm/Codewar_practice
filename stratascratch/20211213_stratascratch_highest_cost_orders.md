# Highest Cost Orders

Find the customer with the highest total order cost between 2019-02-01 to 2019-05-01. If customer had more than one order on a certain day, sum the order costs on daily basis. Output their first name, total cost of their items, and the date.
 
For simplicity, you can assume that every first name in the dataset is unique.

```
DataFrames: customers, orders
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
customers.head() #id, first_name
orders.head() #cust_id, order_date, total_order_cost

# highest order cost between 2/1/19-5/1/19
# sum if multiple orders per day
# output first_name, total_cost, date

# 1. filter out dates outside of 2/1 and 5/1 from `orders` table
# 1-2. group `orders` table by cust_id and order_date, then sum total_order_cost
# 2. merge customers and orders on cust_id
# 3. group by cust_id
# 4. output columns of interest

df_order = orders[orders['order_date'] >= '02/01/2019']
df_order = df_order[df_order['order_date'] <= '05/01/2019']

df_order = df_order.groupby(['cust_id', 'order_date']).sum().reset_index()

df_merge = pd.merge(customers, df_order, how='left', left_on=['id'], right_on=['cust_id'])

df_out = df_merge[df_merge.total_order_cost == df_merge.total_order_cost.max()]

df_out.order_date = df_out.order_date.apply(lambda x: x.date()) #solution requires date format
df_out = df_out[['first_name', 'order_date', 'total_order_cost']]

```