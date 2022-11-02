from flask import Flask, request 
import pickle 
import numpy as np 
import json

# version for week 04 MISO
# Student Ivan Dario Penaloza Rojas
app = Flask(__name__)

optimal_light_gbm_rscv_v1 = pickle.load(open('optimal_light_gbm_rscv_v1.pkl','rb'))
optimal_rfcl_est_v1 = pickle.load(open('optimal_rfcl_est_v1.pkl','rb'))
optimal_xgb_rscv_v1 = pickle.load(open('optimal_xgb_rscv_v1.pkl','rb'))
optimal_knn_v1 = pickle.load(open('knn_v1.pkl','rb'))
customer_segmentation_data_v1 = pickle.load(open('customer_segmentation_data_v1.pkl','rb'))
feature_labels_customers_v1 = pickle.load(open('feature_labels_customers_v1.pkl','rb'))

@app.route('/version', methods=['POST', 'GET'])
def version_ml():
    if request.method == 'GET':
        return "version 3.0.0"

@app.route('/random_forest', methods=['POST', 'GET'])
def random_forest_predictor():


    if request.method == 'POST':
        data = request.get_json()
        
        balance  = data['balance']                          
        balance_frequency  = data['balance_frequency']      
        purchases  = data['purchases']                      
        oneoff_purchases = data['oneoff_purchases']         
        installments_purchases  = data['installments_purchases']           
        cash_advance = data['cash_advance']                      
        purchases_frequency = data['purchases_frequency']        
        oneoff_purchases_frequency = data['oneoff_purchases_frequency'] 
        purchases_installments_frequency = data['purchases_installments_frequency'] 
        cash_advance_frequency= data['cash_advance_frequency']             
        cash_advance_trx = data['cash_advance_trx']                 
        purchases_trx  = data['purchases_trx']                     
        credit_limit = data['credit_limit']                      
        payments = data['payments']                           
        minimum_payments = data['minimum_payments']           
        prc_full_payment = data['prc_full_payment']           
        tenure = data['tenure']   


        
        
        input = np.array([[balance,
                           balance_frequency,
                           purchases,
                           oneoff_purchases,
                           installments_purchases,
                           cash_advance,
                           purchases_frequency,
                           oneoff_purchases_frequency,
                           purchases_installments_frequency,
                           cash_advance_frequency,
                           cash_advance_trx,
                           purchases_trx,
                           credit_limit,
                           payments,
                           minimum_payments,
                           prc_full_payment,
                           tenure]])
        
        
        
        prediction = optimal_rfcl_est_v1.predict(input)

        print('post okay')
        
        return str(prediction[0])

    elif request.method == 'GET':
        print("get okay")
        return "get request received successfully"
    
    
@app.route('/xgboost', methods=['POST'])
def xgboost_predictor():
    
    if request.method == 'POST':
        data = request.get_json()
        
        balance  = data['balance']                          
        balance_frequency  = data['balance_frequency']      
        purchases  = data['purchases']                      
        oneoff_purchases = data['oneoff_purchases']         
        installments_purchases  = data['installments_purchases']           
        cash_advance = data['cash_advance']                      
        purchases_frequency = data['purchases_frequency']        
        oneoff_purchases_frequency = data['oneoff_purchases_frequency'] 
        purchases_installments_frequency = data['purchases_installments_frequency'] 
        cash_advance_frequency= data['cash_advance_frequency']             
        cash_advance_trx = data['cash_advance_trx']                 
        purchases_trx  = data['purchases_trx']                     
        credit_limit = data['credit_limit']                      
        payments = data['payments']                           
        minimum_payments = data['minimum_payments']           
        prc_full_payment = data['prc_full_payment']           
        tenure = data['tenure']   


        
        
        input = np.array([[balance,
                           balance_frequency,
                           purchases,
                           oneoff_purchases,
                           installments_purchases,
                           cash_advance,
                           purchases_frequency,
                           oneoff_purchases_frequency,
                           purchases_installments_frequency,
                           cash_advance_frequency,
                           cash_advance_trx,
                           purchases_trx,
                           credit_limit,
                           payments,
                           minimum_payments,
                           prc_full_payment,
                           tenure]])
        
        
        
        prediction = optimal_xgb_rscv_v1.predict(input)
        
        return str(prediction[0])
    
    
@app.route('/light_gbm', methods=['POST'])
def light_gbm_predictor():
    
    if request.method == 'POST':
        data = request.get_json()
        
        balance  = data['balance']                          
        balance_frequency  = data['balance_frequency']      
        purchases  = data['purchases']                      
        oneoff_purchases = data['oneoff_purchases']         
        installments_purchases  = data['installments_purchases']           
        cash_advance = data['cash_advance']                      
        purchases_frequency = data['purchases_frequency']        
        oneoff_purchases_frequency = data['oneoff_purchases_frequency'] 
        purchases_installments_frequency = data['purchases_installments_frequency'] 
        cash_advance_frequency= data['cash_advance_frequency']             
        cash_advance_trx = data['cash_advance_trx']                 
        purchases_trx  = data['purchases_trx']                     
        credit_limit = data['credit_limit']                      
        payments = data['payments']                           
        minimum_payments = data['minimum_payments']           
        prc_full_payment = data['prc_full_payment']           
        tenure = data['tenure']   


        
        
        input = np.array([[balance,
                           balance_frequency,
                           purchases,
                           oneoff_purchases,
                           installments_purchases,
                           cash_advance,
                           purchases_frequency,
                           oneoff_purchases_frequency,
                           purchases_installments_frequency,
                           cash_advance_frequency,
                           cash_advance_trx,
                           purchases_trx,
                           credit_limit,
                           payments,
                           minimum_payments,
                           prc_full_payment,
                           tenure]])
        
        
        
        prediction = optimal_xgb_rscv_v1.predict(input)
        
        if prediction[0] >= .5:
            prediction[0] = 1
        else:
            prediction[0] = 0
        
        return str(prediction[0])
    
@app.route('/knn', methods=['POST'])
def knn_predictor():
    
    if request.method == 'POST':
        data = request.get_json()
        
        balance  = data['balance']                          
        balance_frequency  = data['balance_frequency']      
        purchases  = data['purchases']                      
        oneoff_purchases = data['oneoff_purchases']         
        installments_purchases  = data['installments_purchases']           
        cash_advance = data['cash_advance']                      
        purchases_frequency = data['purchases_frequency']        
        oneoff_purchases_frequency = data['oneoff_purchases_frequency'] 
        purchases_installments_frequency = data['purchases_installments_frequency'] 
        cash_advance_frequency= data['cash_advance_frequency']             
        cash_advance_trx = data['cash_advance_trx']                 
        purchases_trx  = data['purchases_trx']                     
        credit_limit = data['credit_limit']                      
        payments = data['payments']                           
        minimum_payments = data['minimum_payments']           
        prc_full_payment = data['prc_full_payment']           
        tenure = data['tenure']   


        
        
        input = np.array([[balance,
                           balance_frequency,
                           purchases,
                           oneoff_purchases,
                           installments_purchases,
                           cash_advance,
                           purchases_frequency,
                           oneoff_purchases_frequency,
                           purchases_installments_frequency,
                           cash_advance_frequency,
                           cash_advance_trx,
                           purchases_trx,
                           credit_limit,
                           payments,
                           minimum_payments,
                           prc_full_payment,
                           tenure]])
        
        
        
        prediction = optimal_knn_v1.predict(input)
        
        return str(prediction[0])
    
    
@app.route('/customer_segmentation', methods=['GET'])
def customer_segmentation():
    
    if request.method == 'GET':
        
        customer_segmentation = dict()
        customer_segmentation['data'] = customer_segmentation_data_v1
        customer_segmentation['labels'] = feature_labels_customers_v1
        print(customer_segmentation)
        
        print(json.dumps(customer_segmentation))
        
        return json.dumps(customer_segmentation)
        # return "get request received successfully"

        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)