from source.etl import ETL

x = ETL()

df = x.extract()

x.transform(df)
#x.load(df)