import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import random
from flask import Flask, render_template, request,redirect

import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

app = Flask(__name__)
@app.route('/', methods = ['GET'])

def index():
    feedback = retrieve_Feedback()
    return render_template('index.html', feedback=feedback)

@app.route('/postnew', methods=['GET','POST'])

def postnew():
    container = initCosmos()
    count = count_Feedback(container)
    if request.method =='POST':        
        newfeedback = {
                        'id' : str(count+1),
                        'feedbacktext':request.form['feedbackArea'],
                        'datetime': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                    }    
        container.create_item(body=newfeedback)
        return render_template('postnew.html')

def count_Feedback(container):
    count = list(container.query_items("SELECT VALUE COUNT(1) FROM c", enable_cross_partition_query=True))    
    return int(count[0])

def retrieve_Feedback():
    container = initCosmos()
    count = count_Feedback(container)
    value = "no feedback found"
    if(count > 0):
        randnum = random.randint(1,count)
        iterator = container.query_items("SELECT c.feedbacktext FROM c OFFSET " + str(randnum-1) + " LIMIT 1", enable_cross_partition_query=True)
        value = list(iterator)[0]["feedbacktext"]
    return value

def initCosmos():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
    db = client.get_database_client(DATABASE_ID)
    return db.get_container_client(CONTAINER_ID)

if __name__ == '__main__':   
    app.run(debug=True)
    #empty_container()
