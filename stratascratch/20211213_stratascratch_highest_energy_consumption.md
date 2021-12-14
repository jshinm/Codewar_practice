# Highest Energy Consumption

Find the date with the highest total energy consumption from the Facebook data centers. Output the date along with the total energy consumption across all data centers.

```
DataFrames: fb_eu_energy, fb_asia_energy, fb_na_energy
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# 1. merge all dfs on date
# 2. calculate total consumption
# 3. find the date associated with highest total energy consump.

df_merge = pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])

df_merge = df_merge.groupby('date').sum().reset_index()

df_top = df_merge[df_merge.consumption == df_merge.consumption.max()]
```