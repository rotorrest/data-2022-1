import os
import requests
import pandas as pd
from source.graph import Graph

from tqdm import tqdm

class ETL:
    
    @staticmethod
    def extract(flag_update=False)->pd.DataFrame:
        if flag_update:
            response_positivos = requests.get('https://cloud.minsa.gob.pe/s/AC2adyLkHCKjmfm/download')

            if response_positivos.status_code == 200: #200 es ok #esta
                with open('datos_minsa.csv', 'wb') as csv_file:
                    csv_file.write(response_positivos.content)
                df= pd.read_csv('datos_minsa.csv', sep=';')
                os.remove('datos_minsa.csv')
                return df
            else:
                print("status != 200", "status: " + str(response_positivos.status_code))
        
        elif flag_update == False:
            if os.path.isfile('datos_minsa.csv'):
                return pd.read_csv('datos_minsa.csv', sep=';')
            else:
                print("no existe el archivo os.path.isfile es ", False)
                exit()
    
    @staticmethod
    def transform(df:pd.DataFrame)->pd.DataFrame:
        pivot = pd.pivot_table(df, 
                index=["FECHA_RESULTADO"],
                columns=['DEPARTAMENTO'],
                aggfunc=['size'],
                fill_value=0)
        
        departamentos = ['AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTIN','TACNA','TUMBES','UCAYALI']
        lista_de_fechas = pd.to_datetime(list(pivot.index), format='%Y%m%d') 

        g=Graph(pivot, lista_de_fechas)

        for departamento in tqdm(departamentos, ncols=50):            
            g.compute(departamento)

    @staticmethod
    def load():
        return True