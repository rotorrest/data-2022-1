from source.etl import ETL

x = ETL()

df = x.extract()
print(df.head())
#x.transform(df)
#x.load(df)