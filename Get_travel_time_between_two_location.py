
apiKey = ''#enter the google map api key
from datetime import datetime
import googlemaps
import json
import urllib
gmaps = googlemaps.Client(key=apiKey)

print("Enter the address where you want to go")
FROM_ADDRESS = input("From address :")
TO_ADDRESS = input("To address :")
Mode = input("enter the travelling mode : driving,walking,bicycling :")
now = datetime.now()
directions_result = gmaps.directions(FROM_ADDRESS,TO_ADDRESS,mode=Mode,departure_time=now)
if Mode=='walking':
	time_to_home =  directions_result[0]['legs'][0]['duration']['text']
	print("time take to tarvel between two distance is")
	print(time_to_home)	

if Mode=='driving':
	time_to_home =  directions_result[0]['legs'][0]['duration_in_traffic']['text']
	print("time take to tarvel between two distance is")
	print(time_to_home)