from google.transit import gtfs_realtime_pb2
import urllib

url1 = 'http://dev.indygo.net/TMGTFSRealTimeWebService/Vehicle/VehiclePositions.pb'
url2 = 'http://dev.indygo.net/TMGTFSRealTimeWebService/TripUpdate/TripUpdates.pb'
url3 = 'http://dev.indygo.net/TMGTFSRealTimeWebService/Alert/Alerts.pb'

feed_VP = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen(url1)
feed_VP.ParseFromString(response.read())

feed_TU = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen(url2)
feed_TU.ParseFromString(response.read())

feed_A = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen(url3)
feed_A.ParseFromString(response.read())



count = 0
for entity in feed_TU.entity:
	if entity.HasField('trip_update'):
		count = count + 1
print count

selected_route = input('Select Route ID: ')

for entity in feed_TU.entity:
	if entity.HasField('trip_update'):
		if entity.trip_update.trip.route_id == str(selected_route):
			print entity.trip_update.trip.route_id + ' ' + entity.trip_update.trip.trip_id + ' ' + entity.trip_update.trip.start_time

for entity in feed_VP.entity:
	print entity.id + '\t' + str(entity.vehicle.trip.trip_id) + '\t' +str(entity.vehicle.position.latitude) + '\t' + str(entity.vehicle.position.longitude)

# for entity in feed_A.entity:
# 	print entity



# for entity in feed.entity:
# 	if entity.HasField('id'):
# 		print entity.id
# for entity in feed.entity:
#   if entity.HasField('trip_update'):
#     print entity.trip_update