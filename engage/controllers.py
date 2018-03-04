# Views go here
from engage import app
from flask import Flask
# Importing mongodb instance solves variable import problem
from engage import mongo
from engage.models import Subscriber, ExtractBills, NewsLetter
from flask import render_template

@app.route('/')
def index():
    v = "Hello World"
    return render_template('mail_card.html')

@app.route('/subscribe')
def subscribe():
    # Have a mechanism for looking if the user is already in the db
    # with unique id or email
    new_cust = Subscriber()
    v = "Unsuccessful"
    # try:
    v = new_cust.create("ssalek14@earlham.edu", "in", "upper", ["gun"], 1)
        # subs = mongo.db.subscribers
        # subs.insertss({'email':'ssalek144@earlham.edu'})
    #v = "Successfully created new subscriber
    #except Exception as e:
    #    return ("error in subscriber creation ", e)
    if v == None:
        print ("v is none")
    else:
        pass
    print("The value of v ", v)
    return render_template('msg.html', msg=v)


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
