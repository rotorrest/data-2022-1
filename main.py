from source.etl import ETL

x = ETL()

df = x.extract(True)

x.transform(df)
#x.load(df)
