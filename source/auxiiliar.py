import pandas as pd
class Aux:
    @staticmethod
    def MA(list_MA:list, num_days:int)->list:
        numbers_series = pd.Series(list_MA)
        moving_averages = round(numbers_series.ewm(
            alpha=0.5, adjust=False).mean(), num_days)
        return moving_averages.tolist()