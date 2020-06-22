from django.shortcuts import render
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
import io
import urllib, base64
import random

def chart_plot(request):
    werte = []
    arr_i = []
    plt.close("all")
    for i in range(100):
        werte.append(random.randint(1,49)+i)
        arr_i.append(i)
    slope, intercept, r, p, std_err = stats.linregress(arr_i, werte)
    def myfunc(x):
        return slope * x + intercept
    mymodel = list(map(myfunc, arr_i))
    plt.scatter(arr_i,werte)
    plt.title("Zufalls Werte zwischen 1 und 49 + i")
    plt.plot(arr_i,mymodel)
    plt.legend(["linie","punkte"])
    plt.xlabel('i')
    plt.ylabel('1-49+i')
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'blog/projekt.html',{'data':uri})

