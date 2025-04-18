import pandas as pd
import polars as pl
import dask.dataframe as dd

# Pandas
df = pd.read_csv("/Users/monikaturkowska/Desktop/Biblioteki python/data.csv")
print("Pandas describe():")
print(df.describe())

# Polars
df_polars = pl.read_csv("/Users/monikaturkowska/Desktop/Biblioteki python/data.csv")
print("\nPolars describe():")
print(df_polars.describe())

# Dask
df_dask = dd.read_csv("/Users/monikaturkowska/Desktop/Biblioteki python/data.csv")

# Wybierzmy tylko kolumny numeryczne – aby uniknąć błędu
numeric_df_dask = df_dask.select_dtypes(include='number')
print("\nDask mean (tylko kolumny numeryczne):")
print(numeric_df_dask.mean().compute())
