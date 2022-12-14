import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://cotisscosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'INSERT YOUR MASTER KEY FOR YOUR COSMOS DATABASE HERE!'),
    'database_id': os.environ.get('COSMOS_DATABASE', 'CotissDB'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'CotissFeedBackContainer'),
}