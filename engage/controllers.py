# Views go here
from engage import app
from flask import Flask
# Importing mongodb instance solves variable import problem
from engage import mongo
from engage.models import Subscriber, ExtractBills, NewsLetter
from flask import render_template
from flask import request # for webforms

@app.route('/')
def index():
    v = "Hello World"
    return render_template('landing.html')

@app.route('/sub_form')
def sub_form(): 
    return render_template('subscribe.html')

@app.route('/subscribe', methods=["POST"])
def subscribe():
    new_cust = Subscriber()
    v = "Unsuccessful"
    email = request.form['email']   
    state = request.form['state']
    state = state.lower()
    interval = request.form['interval']
    chamber = request.form['chamber'] 
    tags = request.form['tags']

    v = new_cust.create(email, state, chamber, tags, interval)
    if v == None:
        return "Form submission failed"
    else:
        pass
    print (v)    
 
    return "Thank you!"
    #return render_template('subscribe.html', msg=v)


@app.route('/show')
def show():
    # old_cust = Subscriber()
    # data_old_cust = old_cust.read({"email":"a@b.com"})
    try:
        news = ExtractBills()
        data_old_cust = news.getBill("in", "upper", ["gun", "housing"])
    except Exception as e:
        data_old_cust = e
     
    return render_template('msg.html', msg=data_old_cust)

@app.route('/sendUpdate')
def sendUpdate():
    daily = NewsLetter(1)
    candidates = daily.send()
 
    return render_template('mail_card.html', bill=candidates)
