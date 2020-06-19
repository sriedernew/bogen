from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64
import random

def chart_plot(request):
    werte = []
    ar_i = []
    plt.close("all")
    for i in range(100):
        werte.append(random.randint(1,49)+i)
        arr_i.append(i)
    slope, intercept, r, p, std_err = stats.linregress(werte, arr_i)
    mymodel = list(map(myfunc, ar_i))
    plt.title("Zufalls Werte zwischen 1 und 49 + i")
    plt.xlabel('i')
    plt.ylabel('1-49+i')
    plt.plot(werte,'.')
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'blog/projekt.html',{'data':uri})

def myfunc(x):
    return slope * x + intercept

