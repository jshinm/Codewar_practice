# Order Details

Find order details made by Jill and Eva.
Consider the Jill and Eva as first names of customers.
Output the order date, details and cost along with the first name.
Order records based on the customer id in ascending order.

```
DataFrames: customers, orders
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
customers.head()

# order details by Jill and Eva (first name)
# output - order_date, details, cost, firstname
# order by cust_id in ascending order

# 1. find the user from `customers`
# 2. select col of interest
# 3. join cust and orders
# 4. order by cust_id

dfc = customers[['id', 'first_name']]
dfo = orders[['cust_id', 'order_date', 'order_details', 'total_order_cost']]


dfc = dfc[dfc.apply(lambda x: x.first_name in ['Jill', 'Eva'], axis=1)]

df = pd.merge(dfc, dfo, left_on=['id'], right_on=['cust_id'])

df[['order_date', 'order_details', 'total_order_cost', 'first_name']]
```