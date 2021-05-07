import matplotlib.pyplot as pyplot
from pywaffle import Waffle
import random
from ApiCalls import postdata
import matplotlib as mat
import math
mat.pyplot.switch_backend('Agg')
def Piechart(sizes=[], labels=[]):
    fig1, ax1 = pyplot.subplots()

    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    name =str(random.random()*1000000)+".png"

    pyplot.savefig(name)
    return postdata(filename="./"+name)



def twobarchart(values=[], labels=[]):
    fig, ax = pyplot.subplots()

    ax.bar(labels, values)
    ax.set_xticklabels(labels)
    name =str(random.random()*1000000)+".png"
    pyplot.savefig(name)
    return postdata(filename="./"+name)


def pictogram(data={}, nameofgraph=""):
    fig = pyplot.figure(
        FigureClass=Waffle,
        rows=5,
        values=data,
        colors=("#983D3D", "#232066"),
        title={
            'label': nameofgraph, 'loc': 'left'},
        labels=[f"{k} ({v}%)" for k, v in data.items()],
        legend={'loc': 'lower left', 'bbox_to_anchor': (
            0, -0.4), 'ncol': len(data), 'framealpha': 0},
        starting_location='NW',
        block_arranging_style='snake',
        tight=False,
        figsize=(9, 6)
    )
    name =str(random.random()*1000000)+".png"
    pyplot.savefig(name)
    return postdata(filename="./"+name)


def GetAllCharts(data):
    linkone = Piechart([data['recovered'],data['confirmed']],["Recovered cases","Confirmed cases"])
    linktwo = twobarchart(values=[data['active'],data['deaths']],labels=["Active cases","Deaths"])
    percentFatality=math.floor( data["fatality_rate"]*100)
    percentSurvival= 100-percentFatality
    values = {'Fatality Rate':percentFatality,'Survival Rate':percentSurvival}
    linkthree= pictogram(data=values,nameofgraph="")
    return [linkone,linktwo,linkthree]
