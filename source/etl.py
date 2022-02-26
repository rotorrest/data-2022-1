import os
import requests
import pandas as pd

from source.plot import GeneratePlot
from tqdm import tqdm

class ETL:
    
    @staticmethod
    def extract(update=False)->pd.DataFrame:
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
    def transform(df:pd.DataFrame)->pd.DataFrame:
        pivot = pd.pivot_table(df, 
                index=["FECHA_RESULTADO"],
                columns=['DEPARTAMENTO'],
                aggfunc=['size'],
                fill_value=0)
        
        departamentos = ['AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTIN','TACNA','TUMBES','UCAYALI']
        #departamentos = load_form_yaml("departamentos")
        
        for departamento in tqdm(departamentos, ncols=50):
            
            series = pivot["size"][departamento]
            
            GeneratePlot.compute(series, departamento)
            

        
        """
        pivot["size"]["LIMA"]
        pivot["size"]["AREQUIPA"]
        ...
        ...
        ...
        """
    
    @staticmethod
    def load():
        return True