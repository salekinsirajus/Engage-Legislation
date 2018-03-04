# models go here
from flask import Flask
from flask_pymongo import PyMongo
from engage import app 
from engage import mongo
from engage import mail
from flask_mail import Message
from flask import render_template

import pyopenstates

class NewsLetter(object):
    """Send the prepared newsletter/notification based on the interval
    """
    def __init__(self, interval):
        """
        Args:
            interval: an integer represent how frequently to send emails
        """
        self.interval = interval

    def send(self):
        """Querey on the db to get all the users whose intervals match.
        Extract bills based on that, and send email.
        """
        msg_sent = []
        subs = mongo.db.subscribers
        bill_extractor = ExtractBills()
        
        # Do not need the object ID
        same_interval = subs.find({"interval":self.interval}, {'_id':0})
        
        for each in same_interval:
            email = each['email']
            tags = each['search_tags']
            state = each['state']
            chamber = each['chamber']

            msg_for_rcpnt = bill_extractor.getBill(state, chamber, tags)
            # all_candidates.append((email, msg_for_rcpnt))
            
            try:
                msg_body = "hello world"
                # msg_body = render_template('mail_card.html')
                msg = Message(msg_body,
                                sender="mssshaown@gmail.com",
                                recipients=email)
                mail.send(msg) 
                msg_sent.append((email, "Success"))
            except Exception as e:
                msg_sent.append((email, str(e)))
        return msg_sent
        #return msg_for_rcpnt

class ExtractBills(object):
    def __init__(self):
        # validate API key
        pyopenstates.set_api_key(app.config['OPENSTATES_API_KEY'])
        self.search_window = "term" #only this session

    def getBill(self, state, chamber, tags):
        all_bills = []
        for each in tags:
            bill = pyopenstates.search_bills(state=state, chamber=chamber,q=each)
            all_bills.append(bill)
            all_bills.append(each)

        return all_bills

class Subscriber(object):
    """Represents a subscriper.

    Args:
        email: a string that has the format of a valid email address

        state: a two char string for state, e.g., "in" for Indiana
        chamber: a string that provides upper or lower chamber
        
        Combinationn of state and chamber represents locality    

        search_tags: tag objects that are basically strings
        interval: integers to note how frequently wants update, 1 for everyday
    """

    def __init__(self, uniq_id=None):
        self.uid = uniq_id

    def create(self, email, state, chamber, search_tags, interval):

        self.email = email
        self.state = state
        self.chamber = chamber
        self.search_tags = search_tags
        self.interval = interval

        subs = mongo.db.subscribers

        # If the subscriber is already there
        if subs.find_one({"email": email}) != None:
            return "Subscriber already exists" 

        result = subs.insert({"email": self.email,
                            "state": self.state,
                            "chamber": self.chamber,
                            "search_tags": self.search_tags,
                            "interval": self.interval})
        return result

    def read(self, id_to_search):
        subs = mongo.db.subscribers
        result = subs.find_one(id_to_search)

        if result == None:
            return ("No value found for this subscriber")

        return result

    def get_tags(self, email):
        try:
            subs = mongo.db.subscribers
            all_tags = subs.find_one({"email":email})
        except Exception as e:
            print("Cant get the tags: ", e)
            return []
        
        return all_tags    
    
    def update(self):
        pass

    def delete(self):
        pass
