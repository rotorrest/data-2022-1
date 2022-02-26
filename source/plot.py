import time
import pandas as pd

class GeneratePlot:
    
    def compute(series:pd.Series, departamento:str)->True:
        print("calculando grafico de {}".format(departamento))
        time.sleep(0.5)
 