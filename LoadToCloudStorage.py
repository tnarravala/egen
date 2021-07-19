import base64
from google.cloud import storage
import pandas as pd
import json
def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    message = json.loads(pubsub_message)
    df = pd.DataFrame(message)
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('demo-p1')
    blob = bucket.blob('msft.csv')
    blob.upload_from_string(data = df.to_csv(), content_type='csv')