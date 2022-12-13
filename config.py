import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://cotisscosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'kduR0YSBkCnUWZlgIT260pZMhum9uOV51KsPAJMR32lH1uWm8yHcKzoOypfDD7sk0dznR6zJanR0ACDb76IoxA=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'CotissDB'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'CotissFeedBackContainer'),
}