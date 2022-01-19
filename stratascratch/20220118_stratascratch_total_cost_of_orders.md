# Total Cost Of Orders

Find the total cost of each customer's orders. Output customer's id, first name, and the total order cost. Order records by customer's first name alphabetically.

```
DataFrames: customers, orders
Expected Output Type: pandas.Series
```

```python
# Import your libraries
import pandas as pd

# Start writing code
customers.head()

# total cost of each customer's orders
# output - id, first name, total cost
# order by first name

# 1. group by cust_id - agg(sum(total_order_cost))
# 2. join two tables
# 3. filter cols

df1 = orders.groupby('cust_id').sum().reset_index()
df1 = df1[['cust_id', 'total_order_cost']]
df2 = customers

df_out = pd.merge(df1, df2, left_on='cust_id', right_on='id')
df_out = df_out[['id', 'first_name', 'total_order_cost']]
df_out = df_out.sort_values('first_name')
```