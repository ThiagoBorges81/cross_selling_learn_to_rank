import pickle
import pandas as pd
import requests
import json
from flask           import Flask, request, Response
from healthinsurance import HealthInsurance

# Loading model
model = pickle.load( open( 'models/lgbm_model.pkl','rb' ) )

# Initialize API
app = Flask( __name__ )

@app.route( '/healthinsurance', methods = ['POST'] )

def health_insurance_predict():
    
    test_json = request.get_json()
    
    if test_json: # are there data?
        if isinstance( test_json, dict ): # single example
            test_raw = pd.DataFrame( test_json, index = [0] )
            
        else: # multiple examples
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        # Instantiate Health Insurance Class
        pipeline = HealthInsurance()
        
        # Data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # Feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # Data preparation
        df3 = pipeline.data_preparation( df2 )
        
        # Prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
    
    else:
        return Response( '{}', status=200, mimetype='application/json' )
    
if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( host='0.0.0.0', port=port )
            
