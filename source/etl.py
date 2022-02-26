import os
import requests
import pandas as pd

class ETL:
    
    @staticmethod
    def extract():
        response_positivos = requests.get('https://cloud.minsa.gob.pe/s/AC2adyLkHCKjmfm/download')

        if response_positivos.status_code == 200: #200 es ok

            with open('datos_minsa.csv', 'wb') as csv_file:
                csv_file.write(response_positivos.content)

        else:
            print("fail total, no debio llegar aqui")
            
        df = pd.read_csv('datos_minsa.csv', sep=';')
        os.remove('datos_minsa.csv')
        return df
    
    @staticmethod
    def transform():
        return True
    
    @staticmethod
    def load():
        return True