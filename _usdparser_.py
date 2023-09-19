import requests
import time
import csv
import os



def get_liq_BTC_sber():
    min_1 = float()
    min_5 = float()
    min_15 = float()
    min_30 = float()
    hour_1 = float()
    day_1 = float()

    sber_list = []

    with open(f"/main/templates/csv/liquidation_data_BTC.csv") as fil:
        reader = csv.reader(fil)
        for i in reader:
            if i[4] == "RosBank":
                sber_list.append(i)

    for i in sber_list:
        if int(i[5]) > int(time.time()) - 60:
            min_1 = min_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 300:
            min_5 = min_5 + float(i[1])

        elif int(i[5]) > int(time.time()) - 900:
            min_15 = min_15 + float(i[1])

        elif int(i[5]) > int(time.time()) - 1800:
            min_30 = min_30 + float(i[1])

        elif int(i[5]) > int(time.time()) - 3600:
            hour_1 = hour_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 86400:
            day_1 = day_1 + float(i[1])

    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    url = key + "BTCUSDT"
    data = requests.get(url)
    data = data.json()
    prise = int(float(data['price']))

    data = {
        'day': day_1 * prise / 1440,
        'hour': hour_1 * prise / 60,
        'm30': min_30 * prise / 30,
        'm15': min_15 * prise / 15,
        'm5': min_5 * prise / 5,
        'm1': min_1 * prise / 1

    }
    return data



def get_liq_BTC_tink():
    min_1 = float()
    min_5 = float()
    min_15 = float()
    min_30 = float()
    hour_1 = float()
    day_1 = float()

    sber_list = []

    with open(f"/main/templates/csv/liquidation_data_BTC.csv") as fil:
        reader = csv.reader(fil)
        for i in reader:
            if i[4] == "Tinkoff":
                sber_list.append(i)

    for i in sber_list:
        if int(i[5]) > int(time.time()) - 60:
            min_1 = min_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 300:
            min_5 = min_5 + float(i[1])

        elif int(i[5]) > int(time.time()) - 900:
            min_15 = min_15 + float(i[1])

        elif int(i[5]) > int(time.time()) - 1800:
            min_30 = min_30 + float(i[1])

        elif int(i[5]) > int(time.time()) - 3600:
            hour_1 = hour_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 86400:
            day_1 = day_1 + float(i[1])

    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    url = key + "BTCUSDT"
    data = requests.get(url)
    data = data.json()
    prise = int(float(data['price']))

    data = {
        'day': day_1 * prise / 1440,
        'hour': hour_1 * prise / 60,
        'm30': min_30 * prise / 30,
        'm15': min_15 * prise / 15,
        'm5': min_5 * prise / 5,
        'm1': min_1 * prise / 1

    }
    return data


def get_liq_BTC_raif():
    min_1 = float()
    min_5 = float()
    min_15 = float()
    min_30 = float()
    hour_1 = float()
    day_1 = float()

    sber_list = []

    with open(f"/main/templates/csv/liquidation_data_BTC.csv") as fil:
        reader = csv.reader(fil)
        for i in reader:
            if i[4] == "Raiffeisenbank":
                sber_list.append(i)

    for i in sber_list:
        if int(i[5]) > int(time.time()) - 60:
            min_1 = min_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 300:
            min_5 = min_5 + float(i[1])

        elif int(i[5]) > int(time.time()) - 900:
            min_15 = min_15 + float(i[1])

        elif int(i[5]) > int(time.time()) - 1800:
            min_30 = min_30 + float(i[1])

        elif int(i[5]) > int(time.time()) - 3600:
            hour_1 = hour_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 86400:
            day_1 = day_1 + float(i[1])

    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    url = key + "BTCUSDT"
    data = requests.get(url)
    data = data.json()
    prise = int(float(data['price']))

    data = {
        'day': day_1 * prise / 1440,
        'hour': hour_1 * prise / 60,
        'm30': min_30 * prise / 30,
        'm15': min_15 * prise / 15,
        'm5': min_5 * prise / 5,
        'm1': min_1 * prise / 1

    }
    return data


def get_liq_USDT_tink():

    min_1 = float()
    min_5 = float()
    min_15 = float()
    min_30 = float()
    hour_1 = float()
    day_1 = float()

    tink_list = []

    with open('/main/templates/csv/liquidation_data_USDT.csv') as fil:
        reader = csv.reader(fil)
        for i in reader:
            if i[4] == "Tinkoff":
                tink_list.append(i)

    for i in tink_list:
        if int(i[5]) > int(time.time()) - 60:
            min_1 = min_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 300:
            min_5 = min_5 + float(i[1])

        elif int(i[5]) > int(time.time()) - 900:
            min_15 = min_15 + float(i[1])

        elif int(i[5]) > int(time.time()) - 1800:
            min_30 = min_30 + float(i[1])

        elif int(i[5]) > int(time.time()) - 3600:
            hour_1 = hour_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 86400:
            day_1 = day_1 + float(i[1])


    data = {
        'day': day_1 / 1440,
        'hour': hour_1 / 60,
        'm30': min_30 / 30,
        'm15': min_15 / 15,
        'm5': min_5 / 5,
        'm1': min_1 / 1

    }
    return data



def get_liq_USDT_sber():

    min_1 = float()
    min_5 = float()
    min_15 = float()
    min_30 = float()
    hour_1 = float()
    day_1 = float()

    tink_list = []

    with open('/main/templates/csv/liquidation_data_USDT.csv') as fil:
        reader = csv.reader(fil)
        for i in reader:
            if i[4] == "RosBank":
                tink_list.append(i)

    for i in tink_list:
        if int(i[5]) > int(time.time()) - 60:
            min_1 = min_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 300:
            min_5 = min_5 + float(i[1])

        elif int(i[5]) > int(time.time()) - 900:
            min_15 = min_15 + float(i[1])

        elif int(i[5]) > int(time.time()) - 1800:
            min_30 = min_30 + float(i[1])

        elif int(i[5]) > int(time.time()) - 3600:
            hour_1 = hour_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 86400:
            day_1 = day_1 + float(i[1])


    data = {
        'day': day_1 / 1440,
        'hour': hour_1 / 60,
        'm30': min_30 / 30,
        'm15': min_15 / 15,
        'm5': min_5 / 5,
        'm1': min_1 / 1

    }
    return data

def get_liq_USDT_raif():

    min_1 = float()
    min_5 = float()
    min_15 = float()
    min_30 = float()
    hour_1 = float()
    day_1 = float()

    tink_list = []

    with open('/main/templates/csv/liquidation_data_USDT.csv') as fil:
        reader = csv.reader(fil)
        for i in reader:
            if i[4] == "Raiffeisenbank":
                tink_list.append(i)

    for i in tink_list:
        if int(i[5]) > int(time.time()) - 60:
            min_1 = min_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 300:
            min_5 = min_5 + float(i[1])

        elif int(i[5]) > int(time.time()) - 900:
            min_15 = min_15 + float(i[1])

        elif int(i[5]) > int(time.time()) - 1800:
            min_30 = min_30 + float(i[1])

        elif int(i[5]) > int(time.time()) - 3600:
            hour_1 = hour_1 + float(i[1])

        elif int(i[5]) > int(time.time()) - 86400:
            day_1 = day_1 + float(i[1])


    data = {
        'day': day_1 / 1440,
        'hour': hour_1 / 60,
        'm30': min_30 / 30,
        'm15': min_15 / 15,
        'm5': min_5 / 5,
        'm1': min_1 / 1

    }
    return data