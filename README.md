# egen

Module 1 P1

Real time data from api is stored in GCS in the csv format using continer and pub/sub is created to recieve the information, cloud function is used to trigger to store the data in GCS when subcription recieves the message.

Module 2 P2

The data from GCS is stored in bigquery using cloud function and cloud composer.

Cloud function is used to trigger the Dag, and cloud composer is used for orchestration.
