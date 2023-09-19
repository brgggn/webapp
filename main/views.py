from django.shortcuts import render
import _usdparser_


# Create your views here.







def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['1', '2', '3'],
        'obj': {
            '1': 'one',
            '2': '2',
            '3': '3'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
    #return HttpResponse("<h4>f</h4>")

#BTC by tinkoff
def diagram_1(request):
    data = {
        'day': _usdparser_.get_liq_BTC_tink()['day'],
        'hour': _usdparser_.get_liq_BTC_tink()['hour'],
        'm30': _usdparser_.get_liq_BTC_tink()['m30'],
        'm15': _usdparser_.get_liq_BTC_tink()['m15'],
        'm5': _usdparser_.get_liq_BTC_tink()['m5'],
        'm1': _usdparser_.get_liq_BTC_tink()['m1']

    }
    return render(request, 'main/diagram_1.html', data)

#BTC by Raiffeisen
def diagram_2(request):
    data = {
        'day': _usdparser_.get_liq_BTC_raif()['day'],
        'hour': _usdparser_.get_liq_BTC_raif()['hour'],
        'm30': _usdparser_.get_liq_BTC_raif()['m30'],
        'm15': _usdparser_.get_liq_BTC_raif()['m15'],
        'm5': _usdparser_.get_liq_BTC_raif()['m5'],
        'm1': _usdparser_.get_liq_BTC_raif()['m1']

    }
    return render(request, 'main/diagram_2.html', data)

#BTC by Sber
def diagram_3(request):
    data = {
        'day': _usdparser_.get_liq_BTC_sber()['day'],
        'hour': _usdparser_.get_liq_BTC_sber()['hour'],
        'm30': _usdparser_.get_liq_BTC_sber()['m30'],
        'm15': _usdparser_.get_liq_BTC_sber()['m15'],
        'm5': _usdparser_.get_liq_BTC_sber()['m5'],
        'm1': _usdparser_.get_liq_BTC_sber()['m1']

    }
    return render(request, 'main/diagram_3.html', data)

#USDT by tinkoff
def diagram_4(request):
    data = {
        'day': _usdparser_.get_liq_USDT_tink()['day'],
        'hour': _usdparser_.get_liq_USDT_tink()['hour'],
        'm30': _usdparser_.get_liq_USDT_tink()['m30'],
        'm15': _usdparser_.get_liq_USDT_tink()['m15'],
        'm5': _usdparser_.get_liq_USDT_tink()['m5'],
        'm1': _usdparser_.get_liq_USDT_tink()['m1']

    }
    return render(request, 'main/diagram_4.html', data)

#USDT by Raiffeisen
def diagram_5(request):
    data = {
        'day': _usdparser_.get_liq_USDT_raif()['day'],
        'hour': _usdparser_.get_liq_USDT_raif()['hour'],
        'm30': _usdparser_.get_liq_USDT_raif()['m30'],
        'm15': _usdparser_.get_liq_USDT_raif()['m15'],
        'm5': _usdparser_.get_liq_USDT_raif()['m5'],
        'm1': _usdparser_.get_liq_USDT_raif()['m1']

    }
    return render(request, 'main/diagram_5.html', data)

#USDT by Sber
def diagram_6(request):
    data = {
        'day': _usdparser_.get_liq_USDT_sber()['day'],
        'hour': _usdparser_.get_liq_USDT_sber()['hour'],
        'm30': _usdparser_.get_liq_USDT_sber()['m30'],
        'm15': _usdparser_.get_liq_USDT_sber()['m15'],
        'm5': _usdparser_.get_liq_USDT_sber()['m5'],
        'm1': _usdparser_.get_liq_USDT_sber()['m1'],
        'm1': _usdparser_.get_liq_USDT_sber()['m1']

    }
    return render(request, 'main/diagram_6.html', data)

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""





