import pandas as pd
import numpy as np

df = pd.read_csv("temp0001.txt",header=None,
                 names=['Тикер', 'Цена', 'Див. доход', 'Прогн. доход', 'Флаг див.', 'Валюта', 'Кумм. коэф.', 'Отрасль'],
                 skipfooter=0, dtype={'Тикер': str, 'Цена': float, 'Див. доход': float, 'Прогн. доход': float, 'Флаг див.': str, 'Валюта': str, 'Кумм. коэф.': int, 'Отрасль': str})

div_yield_std = np.std(df['Див. доход'])
div_yield_mean = np.mean(df['Див. доход'])
pred_yield_std = np.std(df['Прогн. доход'])
pred_yield_mean = np.mean(df['Прогн. доход'])

def highlight_plus1sigma_div_yield(data):
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

def highlight_plus1sigma_pred_yield(data):
    color = 'yellow' if data > pred_yield_mean + 1 else ''
    return 'background-color: %s' %color

def highlight_plus2sigma_pred_yield(data):
    color = 'lightgreen' if data > pred_yield_mean + 2*pred_yield_std else ''
    return 'background-color: %s' %color

def highlight_plus3sigma_pred_yield(data):
    color = 'green' if data > pred_yield_mean + 3*pred_yield_std else ''
    return 'background-color: %s' %color

def highlight_mean_pred_yield(data):
    color = 'pink' if data < pred_yield_mean-1 else ''
    return 'background-color: %s' %color

def highlight_minus1sigma_pred_yield(data):
    color = 'red' if data < pred_yield_mean - pred_yield_std else ''
    return 'background-color: %s' %color

def highlight_is_often_div(data):
    color = 'lightgreen' if int(data) >= 4 else ''
    return 'background-color: %s' %color
def highlight_is_futur_div(data):
    color = 'green' if data.find('+') != -1 and int(data) >= 4 else ''
    return 'background-color: %s' %color

def highlight_is_rub(data):
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
        .applymap(highlight_minus1sigma_pred_yield, subset=['Прогн. доход'])
        .applymap(highlight_is_often_div, subset=['Флаг див.'])
        .applymap(highlight_is_futur_div, subset=['Флаг див.'])
        .applymap(highlight_is_rub, subset=['Валюта'])
     )
print('Для ОТОБРАДЖЕНИЯ ПОДСВЕТКИ ячеек нажмите кнопук \"Run\" два раза\n')
print('Если щелкнуть на поле \"Out[2]\" - поле отображения таблицы развернется полностью\n')
print('\n')
print('Пояснения к подсветке ячеек:\n')
print('\n')
print('Для полей \"Див. доход\" и \"Прогн. доход\"\n')
print('ЗЕЛЕНЫЙ - для полей больших чем среднее арифм. + 3 стандартных отклонения\n')
print('СВЕТЛО-ЗЕЛЕНЫЙ - для полей больших чем среднее арифм. + 2 стандартных отклонения\n')
print('ЖЕЛТЫЙ - для полей больших чем среднее арифм. + 1 стандартное отклонение\n')
print('РОЗОВЫЙ - для полей МЕНЬШИХ чем среднее арифм.\n')
print('КРАСНЫЙ - для полей меньших чем среднее арифм. - 1 стандартное отклонение\n')
print('\n')
print('Для поля \"Флаг див.\"\n')
print('ЗЕЛЕНЫЙ - с объявленными в БУДУЩЕМ дивидендами и с оплатой дивидендов более 4 раз в 2019 году\n')
print('СВЕТЛО-ЗЕЛЕНЫЙ - для полей с оплатой дивидендов более 4 раз в 2019 году\n')
print('\n')
print('Для поля \"Валюта"\n')
print('СВЕТЛО-ГОЛУБОЙ - для рублевых инструментов\n')