# Customer Details

Find the details of each customer regardless of whether the customer made an order. Output the customer's first name, last name, and the city along with the order details.

You may have duplicate rows in your results due to a customer ordering several of the same items. Sort records based on the customer's first name and the order details in ascending order.

```
DataFrames: customers, orders
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
customers.head()

# find detials of all cutomer
# output - first_name, last_name, city, order_details

# 1. filter orders table for all cutomer who has order_detials
# 2. filter cutomers table
# 3. join two table
# 4. sort by first_name and order_detials ascending=True

# this filtering is not really needed
df_order = orders[~orders['order_details'].isna()][['cust_id', 'order_details']]

df_customer = customers[['id', 'first_name', 'last_name', 'city']]

# join w.r.t. customer table to get the comprehensive list of the customer
# regardless of whether they made an order or not
df_out = pd.merge(df_order, df_customer, how='right', left_on='cust_id', right_on='id')

df_out = df_out[['first_name', 'last_name', 'city', 'order_details']]

df_out = df_out.sort_values(['first_name', 'order_details'], ascending=True)
```