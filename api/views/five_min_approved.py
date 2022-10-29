from flask import Blueprint, render_template
import psycopg2
import os

from pymongo import MongoClient

five_min_approved = Blueprint('five_min_approved', __name__,template_folder="../../templates")


@five_min_approved.route('/5min_approved_postgres')
def count_five_min_approved_postgres():

    db_conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'], 
                               port=os.environ['POSTGRES_PORT'], 
                               dbname=os.environ['POSTGRES_DB'], 
                               user=os.environ['POSTGRES_USER'], 
                               password=os.environ['POSTGRES_PASSWORD'])
    
    db_cursor = db_conn.cursor()
    s = "SELECT * FROM c1_fraud_5min ORDER BY c1_fraud_5min.end;"
    db_cursor.execute(s)
    
    list_users = db_cursor.fetchall()
    print(list_users)
    no_fraud_list = []
    
    for item in list_users:
      y = item[2]
     
      date = item[1].strftime("%Y-%m-%d %H:%M:%S")
      
      # Highcharts timestamp values include miliseconds and are 5 hours ahead
      date_to_timestamp = int(item[1].timestamp()- 5*60*60 ) *1000
    
      no_fraud_list.append({"x":date_to_timestamp,"y":y,"date":date})
      
    print(no_fraud_list)
    
    
    context = {
        "no_fraud_list": no_fraud_list ,
        "title": "Citibanamex"
    }
      
    return render_template('5min_approved.html', context=context)

@five_min_approved.route('/5min_approved_mongo_db')
def count_five_min_approved_mongo_db():
    
    client = MongoClient(host="localhost",port=27017)
    db = client['first_ivan_db']

    collection = db['citibanamex_credit_card_1_5min']
    
    
    no_fraud_list = list()
    
    for document in collection.find({},{"_id":0,"start":1,"end":1,"total_approved_c1":1,"total_no_approved_c1":1}).sort("end"):
        y = document['total_approved_c1']
        
        date = document['end'].strftime("%Y-%m-%d %H:%M:%S")
        
        # Highcharts timestamp values include miliseconds and are 5 hours ahead
        date_to_timestamp = int(document['end'].timestamp()- 5*60*60 ) *1000
        
        no_fraud_list.append({"x":date_to_timestamp,"y":y,"date":date})
        
    print(no_fraud_list)

          
    context = {
        "no_fraud_list": no_fraud_list ,
        "title": "Citibanamex"
    }
      
    return render_template('5min_approved.html', context=context)