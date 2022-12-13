import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import random

import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

def count_Feedback():
    count = list(container.query_items("SELECT VALUE COUNT(1) FROM c", enable_cross_partition_query=True))
    return int(count[0])

def add_Feedback(count):    

    feedback = {
                'id' : str(count+1),
                'feedbacktext':'the third of much positive feedback',
                'datetime': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            }
    
    container.create_item(body=feedback)

    print("feedback placed")

def retrieve_Feedback():
    randnum = random.randint(1,count)
    feedback = container.query_items("SELECT c.feedbacktext FROM c OFFSET " + str(randnum-1) + " LIMIT 1", enable_cross_partition_query=True)
    for f in feedback:
        print(f)


if __name__ == '__main__':
    
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
    db = client.get_database_client(DATABASE_ID)
    container = db.get_container_client(CONTAINER_ID)

    count = count_Feedback()
    retrieve_Feedback()
    #add_Feedback(count)
