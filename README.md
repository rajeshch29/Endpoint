#Endpoint

The purpose of this project is to storing the data of multiple Linux hosts information which were collected through the http end point.

##Usage of this application
Pass hosts information through http post request from their respective hosts.

curl "http://127.0.0.1:5000/data?host=$(hostname)&utime=$(uptime | awk '{print $3 "-" $4}' | awk -F "," '{print $1}')&kver=$(uname -r)"

Install requirements:
python -m pip install -r requirements.txt
