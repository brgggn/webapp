import requests
import time
import json
import csv
import os
import random
from threading import Thread
from requests.auth import HTTPProxyAuth
from colorama import *


init(autoreset=True)


def get_p2p_page(url, page, rows, asset, fiat, tradeType, rproxy):
    headers = {'content-type': 'application/json'}
    json_data = {
        "page":page,
        "rows":rows,
        "asset":asset,
        "fiat":fiat,
        "tradeType":tradeType
    }



    proxies = {
    'https': f'http://{rproxy}'
    }

    response = requests.post(url, headers=headers, proxies=proxies, json=json_data)
    if response.status_code != 200:
        response.raise_for_status()
    return json.loads(response.text)

    print(response)

url = r'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

                                    # Формат записи 
                                    # proxies = {'http': 'http://username:password@ip:port', 'https': 'http://username:password@ip:port'}
                                    # requests.post(url, proxies=proxies, data=data)
def get_liquidation_buy_BTC_RUB():
    try:
        time.sleep(0.2)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "BTC"
            fiat = "RUB"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@188.130.189.164:1050', 'G8N5m4:x1JfwlGbv4@188.130.185.87:1050', 'G8N5m4:x1JfwlGbv4@188.130.185.87:1050']
            rproxy = proxy_list[random.randint(0,2)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []


            with open('main/templates/csv/all_data_BTC_RUB.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_BTC_RUB.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_BTC.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[31m' +"BTC  RUB Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_BTC_RUB()




def get_liquidation_buy_USDT_RUB():
    try:
        time.sleep(0.3)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "USDT"
            fiat = "RUB"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@45.134.180.241:1050', 'G8N5m4:x1JfwlGbv4@45.142.253.229:1050', 'G8N5m4:x1JfwlGbv4@91.188.244.144:1050']
            rproxy = proxy_list[random.randint(0,2)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []

            with open('main/templates/csv/all_data_USDT_RUB.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_USDT_RUB.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_USDT.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[31m' +"USDT RUB Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(30)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_USDT_RUB()


                 


                                        # Формат записи 
                                        # proxies = {'http': 'http://username:password@ip:port', 'https': 'http://username:password@ip:port'}
                                        # requests.post(url, proxies=proxies, data=data)
def get_liquidation_buy_BTC_UAH():
    try:
        time.sleep(0.4)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "BTC"
            fiat = "UAH"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@176.53.186.112:1050', 'G8N5m4:x1JfwlGbv4@45.139.176.31:1050']
            rproxy = proxy_list[random.randint(0,1)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []


            with open('main/templates/csv/all_data_BTC_UAH.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_BTC_UAH.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_BTC.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[33m' + "BTC  UAH Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_BTC_UAH()


def get_liquidation_buy_USDT_UAH():
    try:
        time.sleep(0.5)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "USDT"
            fiat = "UAH"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@46.8.107.61:1050', 'G8N5m4:x1JfwlGbv4@45.139.177.132:1050']
            rproxy = proxy_list[random.randint(0,1)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []

            with open('main/templates/csv/all_data_USDT_UAH.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_UAH_sell.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_USDT.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[33m' + "USDT UAH Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_USDT_UAH()






















def get_liquidation_buy_BTC_USD():
    try:
        time.sleep(0.6)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "BTC"
            fiat = "USD"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@84.54.53.206:1050', 'G8N5m4:x1JfwlGbv4@109.248.138.34:1050', 'G8N5m4:x1JfwlGbv4@91.188.244.48:1050']
            rproxy = proxy_list[random.randint(0,2)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []


            with open('main/templates/csv/all_data_BTC_USD.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_BTC_USD.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_BTC.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[32m' + "BTC  USD Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_BTC_USD()



def get_liquidation_buy_USDT_USD():
    try:
        time.sleep(0.7)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "USDT"
            fiat = "USDT"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@46.8.10.110:1050', 'G8N5m4:x1JfwlGbv4@45.144.36.124:1050', 'G8N5m4:x1JfwlGbv4@109.248.139.38:1050']
            rproxy = proxy_list[random.randint(0,2)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []

            with open('main/templates/csv/all_data_USDT_USD.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_USDT_USD.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_USDT.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[32m' + "USDT USD Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_USDT_USD()

                 


                                        # Формат записи 
                                        # proxies = {'http': 'http://username:password@ip:port', 'https': 'http://username:password@ip:port'}
                                        # requests.post(url, proxies=proxies, data=data)
def get_liquidation_buy_BTC_EUR():
    try:
        time.sleep(0.8)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "BTC"
            fiat = "EUR"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@2.59.50.152:1050', 'G8N5m4:x1JfwlGbv4@45.87.252.140:1050', 'G8N5m4:x1JfwlGbv4@194.156.123.204:1050']
            rproxy = proxy_list[random.randint(0,2)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []


            with open('main/templates/csv/all_data_BTC_EUR.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_BTC_EUR.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_BTC.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[34m' + "BTC  EUR Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_BTC_EUR()


def get_liquidation_buy_USDT_EUR():
    try:
        time.sleep(0.9)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "USDT"
            fiat = "EUR"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@188.130.186.229:1050', 'G8N5m4:x1JfwlGbv4@77.83.84.47:1050', 'G8N5m4:x1JfwlGbv4@109.248.129.192:1050']
            rproxy = proxy_list[random.randint(0,2)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []

            with open('main/templates/csv/all_data_USDT_EUR.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_USDT_EUR.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_USDT.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print('\033[34m' + "USDT EUR Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_USDT_EUR()

















def get_liquidation_buy_BTC_GBT():
    try:
        time.sleep(1)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "BTC"
            fiat = "GBT"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@45.144.36.187:1050', 'G8N5m4:x1JfwlGbv4@46.8.213.34:1050']
            rproxy = proxy_list[random.randint(0,1)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []


            with open('main/templates/csv/all_data_BTC_GBT.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_BTC_GBT.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_BTC.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print("BTC  GBT Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_BTC_GBT()




def get_liquidation_buy_USDT_GBT():
    try:
        time.sleep(1.1)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "USDT"
            fiat = "GBT"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@188.130.185.42:1050', 'G8N5m4:x1JfwlGbv4@2.59.50.42:1050']
            rproxy = proxy_list[random.randint(0,1)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []

            with open('main/templates/csv/all_data_USDT_GBT.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_USDT_GBT.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_USDT.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print("USDT GBT Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_USDT_GBT()

                 


                                        # Формат записи 
                                        # proxies = {'http': 'http://username:password@ip:port', 'https': 'http://username:password@ip:port'}
                                        # requests.post(url, proxies=proxies, data=data)
def get_liquidation_buy_BTC_CZK():
    try:
        time.sleep(1.2)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "BTC"
            fiat = "CZK"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@45.145.119.128:1050', 'G8N5m4:x1JfwlGbv4@109.248.166.198:1050']
            rproxy = proxy_list[random.randint(0,1)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []


            with open('main/templates/csv/all_data_BTC_CZK.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_BTC_CZK.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_BTC.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print("BTC  CZK Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return 0
        time.sleep(60)
        get_liquidation_buy_BTC_CZK()



def get_liquidation_buy_USDT_CZK():
    try:
        time.sleep(1.3)
        iter_nation = 0
        while True:
            if iter_nation == 0:
                print("Parsing is started")

            iter_nation += 1
            old_rows  = []
            to_liqudation = []
            rows = []
            page = 0
            asset = "USDT"
            fiat = "CZK"
            tradeType = "BUY"
            proxy_list=['G8N5m4:x1JfwlGbv4@194.32.229.180:1050', 'G8N5m4:x1JfwlGbv4@109.248.167.224:1050']
            rproxy = proxy_list[random.randint(0,1)]
            while page < 30:
                page += 1
                r = get_p2p_page(url,page,20,asset,fiat,tradeType,rproxy)
                if r['data'] == []: break
                for i in r['data']:
                    rows.append([
                        i['advertiser']['nickName'],
                        i['adv']['tradableQuantity'],
                        i['adv']['asset'],
                        i['adv']['advNo'],
                        i['adv']['tradeMethods'][0]['tradeMethodName']
                    ])

            order_numbers = []
            rows_fo_cycle_rows=[]
            rows_fo_cycle_oldrows = []

            with open('main/templates/csv/all_data_USDT_CZK.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    old_rows.append(i)

            file = open('main/templates/csv/all_data_USDT_CZK.csv', 'w', errors='ignore', newline='')  #codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
            with file:
                for i in rows:
                    writer = csv.writer(file)
                    writer.writerow(i)

            for i in rows:
                rows_fo_cycle_rows.append(i[3])

            for i in old_rows:
                rows_fo_cycle_oldrows.append(i[3])

            for i in rows_fo_cycle_oldrows:
                if i not in rows_fo_cycle_rows:
                    order_numbers.append(i)

            for i in old_rows:
                if i[3] in order_numbers:
                    i.append(int(time.time()))
                    to_liqudation.append(i)

            file = open('main/templates/csv/liquidation_data_USDT.csv', 'a', errors='ignore', newline='')
            with file:
                for i in to_liqudation:
                    writer = csv.writer(file)
                    writer.writerow(i)

            print("USDT CZK Iteration  ", iter_nation, " :", len(to_liqudation))
            time.sleep(50)
    except:
        return  0
        time.sleep(60)
        get_liquidation_buy_USDT_CZK()





def del_rows_in_CSV_USDT():
    time.sleep(600)
    rows_to_delet = []
    rows_to_write = []
    with open('main/templates/csv/liquidation_data_USDT.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    rows_to_delet.append(i)


    print("Cleaning USDT DataBase... Data now: ", len(rows_to_delet))

    timer = 0

    file = open('main/templates/csv/bufer_for_USDT.csv', 'w', errors='ignore', newline='')
    with file:
        for i in rows_to_delet:
            writer = csv.writer(file)
            if int(i[5]) > int(time.time()) - 84600:
                writer.writerow(i)
                timer += 1

    with open('main/templates/csv/bufer_for_USDT.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    rows_to_write.append(i)

    file_2 = open('main/templates/csv/liquidation_data_USDT.csv', 'w', errors='ignore', newline='')
    with file_2:
        for i in rows_to_write:
            writer = csv.writer(file_2)
            writer.writerow(i)

    print("USDT data after cleaning : ", timer)




def del_rows_in_CSV_BTC():
    time.sleep(600)
    rows_to_delet = []
    rows_to_write = []
    with open('main/templates/csv/liquidation_data_BTC.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    rows_to_delet.append(i)


    print("Cleaning BTC DataBase... Data now: ", len(rows_to_delet))

    timer = 0

    file = open('main/templates/csv/bufer_for_BTC.csv', 'w', errors='ignore', newline='')
    with file:
        for i in rows_to_delet:
            writer = csv.writer(file)
            if int(i[5]) > int(time.time()) - 84600:
                writer.writerow(i)
                timer += 1

    with open('main/templates/csv/bufer_for_BTC.csv', errors='ignore') as f:
                reader = csv.reader(f)
                for i in reader:
                    rows_to_write.append(i)

    file_2 = open('main/templates/csv/liquidation_data_BTC.csv', 'w', errors='ignore', newline='')
    with file_2:
        for i in rows_to_write:
            writer = csv.writer(file_2)
            writer.writerow(i)

    print("BTC data after cleaning : ", timer)






t1 = Thread(target=get_liquidation_buy_BTC_RUB)
t2 = Thread(target=get_liquidation_buy_USDT_RUB)

t3 = Thread(target=get_liquidation_buy_BTC_UAH)
t4 = Thread(target=get_liquidation_buy_USDT_UAH)

t5 = Thread(target=get_liquidation_buy_BTC_USD)
t6 = Thread(target=get_liquidation_buy_USDT_USD) 

t7 = Thread(target=get_liquidation_buy_BTC_EUR)
t8 = Thread(target=get_liquidation_buy_USDT_EUR) 

t9 = Thread(target=get_liquidation_buy_BTC_GBT)
t10 = Thread(target=get_liquidation_buy_USDT_GBT)

t11 = Thread(target=get_liquidation_buy_BTC_CZK)
t12 = Thread(target=get_liquidation_buy_USDT_CZK) 

t13 = Thread(target=del_rows_in_CSV_USDT)
t14 = Thread(target=del_rows_in_CSV_BTC) 


t1.start()
t2.start()

t3.start()
t4.start()

t5.start()
t6.start()

t7.start()
t8.start()

t9.start()
t10.start()

t11.start()
t12.start()

t13.start()
t14.start()



t1.join()
t2.join()

t3.join()
t4.join()

t5.join()
t6.join()

t7.join()
t8.join()

t9.join()
t10.join()

t11.join()
t12.join()

t13.join()
t14.join()



























   # хихихи хвахавха





