from google.cloud import pubsub_v1
import os
from alpha_vantage.timeseries import TimeSeries
project_id = "optimum-courier-320218"
topic_id = "stream-api"
credential_path = "/Users/thejeswarreddynarravala/Downloads/optimum-courier-320218-0ab712e75656.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

#for n in range(1,3):


    #data = f"Message number {n} test"
    # Data must be a bytestring
    #data = data.encode("utf-8")
    # Add two attributes, origin and username, to the message
    #future = publisher.publish(
     #   topic_path, data, origin="python-sample", username="gcp"
    #)
    #print(future.result())

api_key = 'QRY4X064BD8EQTV7'
ts = TimeSeries(key=api_key, output_format='pandas')
data, metadata = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
data = data.head(10)
data = data.to_json()
data = data.encode("utf-8")
future = publisher.publish(
        topic_path, data, origin="MSFT-data", username="gcp"
    )
print(future.result())

print(f"Published messages with custom attributes to {topic_path}.")
