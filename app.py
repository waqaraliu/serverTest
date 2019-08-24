from flask import Flask, Markup, render_template
import time
import datetime
from flask import request
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

labels = [
    'Fair', 'Good', 'Poor', 'Very good',
    'Satisfactory', 'Excellent', 'None'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83
]

colors = [
    "#FDB45C", "#46BFBD", "#F7464A", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC"
]
    
@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)

@app.route('/line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=line_labels, values=line_values)

@app.route('/')
def main3():
    #option = request.form['choice']
    #print(option)
    return render_template('index.html')
@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))

def get_values(values):
    freqA = freqB = freqC = freqD = freqE = freqF = freqG = 0;
    for data in values: 
        if(data=='Fair'):
            freqA = freqA + 1
        elif(data=='Good'):
            freqB = freqB + 1
        elif(data=='Poor'):
            freqC = freqC + 1     
        elif(data=='Very good'):
            freqD = freqD + 1
        elif(data=='Satisfactory'):
            freqE = freqE + 1
        elif(data=='Excellent'):
            freqF = freqF + 1
        elif(data=='None'):
            freqG = freqG + 1
        #print(data) 
    values = [
        freqA, freqB, freqC, freqD,
        freqE, freqF, freqG
    ]
    
    return values

def get_color(option):
    color = ""
    currOption = ""
    data = option
    if(data=='choice1'):
            color = "#FDB45C"
            currOption = "option 1"
            choiceValue = 'Fair'
    elif(data=='choice2'):
            color = "#46BFBD"
            currOption = "option 2"
            choiceValue = 'Good'
    elif(data=='choice3'):
            color = "#F7464A"
            currOption = "option 3"
            choiceValue = 'Poor'
    elif(data=='choice4'):
            color = "#FEDCBA"
            currOption = "option 4"
            choiceValue = 'Very good'
    elif(data=='choice5'):
            color = "#ABCDEF"
            currOption = "option 5"
            choiceValue = 'Satisfactory'
    elif(data=='choice6'):
            color = "#DDDDDD"
            currOption = "option 6"
            choiceValue = 'Excellent'
    elif(data=='choice7'):
            color = "#ABCABC"
            currOption = "option 7"
            choiceValue = 'None'
        #print(data) 
    
    return [color, currOption, choiceValue]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1935)
