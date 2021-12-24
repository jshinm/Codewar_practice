# Customer Revenue In March

Calculate the total revenue from each customer in March 2019. 

Output the revenue along with the customer id and sort the results based on the revenue in descending order.

```
DataFrame: orders
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
orders.head()

# total revenue, each costumer, 3/2019
# output revenue and the id
# sort revenue descending order

# 1. filter for 03/2019
# 2. groupby cust_id, then sum(total_order_cost)

orders = orders[orders['order_date'].apply(lambda x:x.year) == 2019]

orders = orders[orders['order_date'].apply(lambda x:x.month) == 3]

orders = orders.groupby('cust_id').sum()
orders = orders.sort_values('total_order_cost', ascending=False).reset_index()

orders[['cust_id', 'total_order_cost']]
```