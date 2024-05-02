# [START aiplatform_predict_tabular_classification_sample]
from typing import Dict
import os
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
import streamlit as st
from dotenv import load_dotenv


# Load environment variables from the .env file, if it exists
load_dotenv()

# Access the environment variable
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

if credentials_path:
    # Use the credentials path for authentication (specific steps depend on your library)
    print(f"Using credentials from: {credentials_path}")
    # ... (Your authentication logic using the credentials path)
else:
    print("Warning: GOOGLE_APPLICATION_CREDENTIALS environment variable not set.")

def predict_tabular_classification_sample(
    project: str = "650189184672",
    endpoint_id: str = "6351896265847996416",
    instance_dict: Dict = [],
    location: str = "us-east4",
    api_endpoint: str = "us-east4-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(
        client_options=client_options)
    # for more info on the instance schema, please use get_model_sample.py
    # and look at the yaml found in instance_schema_uri
    instance = json_format.ParseDict(instance_dict, Value())
    instances = [instance]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    # print("response")
    # print(" deployed_model_id:", response.deployed_model_id)
    # # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_classification_1.0.0.yaml for the format of the predictions.
    predictions = response.predictions
    # for prediction in predictions:
    #     print(" prediction:", dict(prediction))

    return (predictions[0]['classes'][0]) ,(predictions[0]['scores'][0])    

# ! ONLY CHANGE THIS
predict_tabular_classification_sample(instance_dict={
    "N": "90", # Nitrogen concentration
    "P": "42", # phosphorus concentration
    "K": "43", # potassiunm concentration
    "temperature": "20.87974371", # temperature of the local area
    "humidity": "82.00274423", # humidity of the area
    "ph": "6.502985292000001", # ph level of the soil 
    "rainfall": "202.9355362", # rainfall on average  
})

# [END aiplatform_predict_tabular_classification_sample]


