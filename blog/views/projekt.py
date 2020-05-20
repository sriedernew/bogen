from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64
import random

def chart_plot(request):
    werte = []
    plt.close("all")
    for i in range(100):
        werte.append(random.randint(1,49)+i)
    plt.plot(werte,'.')
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'blog/projekt_step1.html',{'data':uri})

