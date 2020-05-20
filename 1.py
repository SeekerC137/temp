import pandas as pd
import numpy as np

df = pd.read_csv("temp0001.txt",header=None,
                 names=['Тикер', 'Цена', 'Див. доход', 'Прогн. доход', 'P/E', 'Флаг див.', 'Валюта', 'Кумм. коэф.', 'Отрасль'],
                 skipfooter=0, dtype={'Тикер': str, 'Цена': float, 'Див. доход': float, 'Прогн. доход': float, 'P/E': float, 'Флаг див.': str, 'Валюта': str, 'Кумм. коэф.': int, 'Отрасль': str})

#div_yield_std = np.std(df['Див. доход'])
#div_yield_mean = np.mean(df['Див. доход'])
#pred_yield_std = np.std(df['Прогн. доход'])
#pred_yield_mean = np.mean(df['Прогн. доход'])

pe_usd_std = np.std(df.loc[df['Валюта'] == 'USD']['P/E'])
pe_usd_mean = np.mean(df.loc[df['Валюта'] == 'USD']['P/E'])
pe_rub_std = np.std(df.loc[df['Валюта'] == 'RUB']['P/E'])
pe_rub_mean = np.mean(df.loc[df['Валюта'] == 'RUB']['P/E'])

print(pe_usd_mean)