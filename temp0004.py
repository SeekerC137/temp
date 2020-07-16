import pandas as pd
import numpy as np

df = pd.read_csv("temp0004.txt",header=None,
                 names=['Тикер', 'Цена', 'Див. доход', 'Прогн. доход', 'P/E', 'Флаг див.', 'Валюта', 'Кумм. коэф.', 'Отрасль'],
                 skipfooter=0, dtype={'Тикер': str, 'Цена': float, 'Див. доход': float, 'Прогн. доход': float, 'P/E': float, 'Флаг див.': str, 'Валюта': str, 'Кумм. коэф.': int, 'Отрасль': str})

div_yield_std = np.std(df['Див. доход'])
div_yield_mean = np.mean(df['Див. доход'])

PP = []

for i in df['Прогн. доход']:                                # Отбираю только прогнозный доход < 100% и > -100%
    if i < 100 and i > -100:
        PP.append(i)

pred_yield_std = np.std(PP)
pred_yield_mean = np.mean(PP])

PE = []
count=0
summ=0
for i in df['P/E']:
    if i <100:
        count+=1
        summ+=i
        PE.append(i)
pe_mean = summ/count
pe_std = np.std(PE)


def highlight_plus1sigma_div_yield(data):                                          # Подсветка колонки дивидендов
    color = 'yellow' if data > div_yield_mean + div_yield_std else ''
    return 'background-color: %s' %color

def highlight_plus2sigma_div_yield(data):
    color = 'lightgreen' if data > div_yield_mean + 2*div_yield_std else ''
    return 'background-color: %s' %color

def highlight_plus3sigma_div_yield(data):
    color = 'green' if data > div_yield_mean + 3*div_yield_std else ''
    return 'background-color: %s' %color

def highlight_mean_div_yield(data):
    color = 'pink' if data < div_yield_mean else ''
    return 'background-color: %s' %color

def highlight_minus1sigma_div_yield(data):
    color = 'red' if data < div_yield_mean - div_yield_std else ''
    return 'background-color: %s' %color


def highlight_plus1sigma_pred_yield(data):                                          # Подсветка колонки прогнозов
    color = 'yellow' if data > pred_yield_mean + 1 else ''
    return 'background-color: %s' %color

def highlight_plus2sigma_pred_yield(data):
    color = 'lightgreen' if data > pred_yield_mean + 2*pred_yield_std else ''
    return 'background-color: %s' %color

def highlight_plus3sigma_pred_yield(data):
    color = 'green' if data > pred_yield_mean + 3*pred_yield_std else ''
    return 'background-color: %s' %color

def highlight_mean_pred_yield(data):
    color = 'pink' if data <= pred_yield_mean - 1 else ''
    return 'background-color: %s' %color

def highlight_minus1sigma_pred_yield(data):
    color = 'red' if data < pred_yield_mean - pred_yield_std else ''
    return 'background-color: %s' %color


def highlight_minus2sigma_pe(data):                                               # Подсветка колонки P/E
    color = 'green' if data < pe_mean-2*pe_std else ''
    return 'background-color: %s' %color

def highlight_minus1sigma_pe(data):
    color = 'lightgreen' if data < pe_mean-1*pe_std else ''
    return 'background-color: %s' %color

def highlight_plusmean_pe(data):
    color = 'pink' if data > pe_mean+0.1 else ''
    return 'background-color: %s' %color

def highlight_plus1sigma_pe(data):
    color = 'red' if data > pe_mean+pe_std else ''
    return 'background-color: %s' %color


def highlight_is_often_div(data):                                                  # Подсветка колонки флага дивидендов
    color = 'lightgreen' if int(data) >= 4 else ''
    return 'background-color: %s' %color
def highlight_is_futur_div(data):
    color = 'green' if data.find('+') != -1 and int(data) >= 4 else ''
    return 'background-color: %s' %color


def highlight_is_rub(data):                                                        # Подсветка рублевых инструментов
    color = 'lightblue' if data == 'RUB' else ''
    return 'background-color: %s' %color

df = (df.style
        .applymap(highlight_plus1sigma_div_yield, subset=['Див. доход'])
        .applymap(highlight_plus2sigma_div_yield, subset=['Див. доход'])
        .applymap(highlight_plus3sigma_div_yield, subset=['Див. доход'])
        .applymap(highlight_mean_div_yield, subset=['Див. доход'])
        .applymap(highlight_minus1sigma_div_yield, subset=['Див. доход'])
        .applymap(highlight_plus1sigma_pred_yield, subset=['Прогн. доход'])
        .applymap(highlight_plus2sigma_pred_yield, subset=['Прогн. доход'])
        .applymap(highlight_plus3sigma_pred_yield, subset=['Прогн. доход'])
        .applymap(highlight_mean_pred_yield, subset=['Прогн. доход'])
        .applymap(highlight_minus2sigma_pe, subset=['P/E'])
        .applymap(highlight_minus1sigma_pe, subset=['P/E'])
        .applymap(highlight_plusmean_pe, subset=['P/E'])
        .applymap(highlight_plus1sigma_pe, subset=['P/E'])
        .applymap(highlight_is_often_div, subset=['Флаг див.'])
        .applymap(highlight_is_futur_div, subset=['Флаг див.'])
        .applymap(highlight_is_rub, subset=['Валюта'])
     )