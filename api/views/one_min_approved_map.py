from flask import Blueprint, render_template
import psycopg2
import os

from pymongo import MongoClient

one_min_approved_map = Blueprint('one_min_approved_map', __name__,template_folder="../../templates")

@one_min_approved_map.route('/1min_approved_map_postgres')
def count_one_min_approved_map_postgres():

    db_conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'], 
                               port=os.environ['POSTGRES_PORT'], 
                               dbname=os.environ['POSTGRES_DB'], 
                               user=os.environ['POSTGRES_USER'], 
                               password=os.environ['POSTGRES_PASSWORD'])
    
    db_cursor = db_conn.cursor()
    s = "SELECT * FROM c1_fraud_1min_map ORDER BY c1_fraud_1min_map.created_time;"
    db_cursor.execute(s)
    
    list_clients = db_cursor.fetchall()

 
    context = {
        "list_clients": list_clients,
        "title": "Citibanamex"
    }
      
    return render_template('1min_approved_map.html', context=context)



@one_min_approved_map.route('/1min_approved_map_mongo_db')
def count_one_min_approved_map_mongo_db():
    
    client = MongoClient(host="localhost",port=27017)
    db = client['first_ivan_db']

    collection = db['citibanamex_credit_card_1_map']
    
    
    list_clients = list()
    
    for document in collection.find({},{"_id":0}).sort("created_time"):
        list_clients.append([document['mexican_state'], document["approved_credit_c1_status"],document["no_approved_credit_c1_status"]])
        

          
    context = {
        "list_clients": list_clients,
        "title": "Citibanamex"
    }
      
    return render_template('1min_approved_map_mongodb.html', context=context)


