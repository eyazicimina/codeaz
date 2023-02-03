import pandas as pd
import json
import pickle

path = "/home/mina5/PycharmProjects/codeaz-python/w12/archive(3)/"
df = pd.read_csv(path + "Hotel_details.csv")

# Import the required library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

df['SearchString'] = df['city'].map(str) + ', ' + df['country'].map(str)


city_coordinates = df.groupby(['SearchString']).agg({'latitude': 'mean', 'longitude': 'mean'})
city_coordinates = city_coordinates.reset_index()

city_lat = dict( zip(city_coordinates['SearchString'], city_coordinates['latitude']) )
city_lon = dict( zip(city_coordinates['SearchString'], city_coordinates['longitude']) )


def distanceToCenter( row ) -> float:
	def euclidean_distance(x1, y1, x2, y2):
		return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
	ss = row['SearchString']
	return euclidean_distance( row['latitude'], row['longitude'], city_lat[ss], city_lon[ss] )

df['starrating'] = df['starrating'].astype(int)
df['DistanceToCenter'] = df.apply(lambda row: distanceToCenter( row ), axis = 1)

print(df['DistanceToCenter'].corr(df['starrating']))


df.to_csv(path + "w12Details.csv")
"""

df = df.sample(10)

for city in df['SearchString'].unique():
	location = geolocator.geocode(city)
	city_coordinates[ city ] = [location.latitude, location.longitude]


json.dump(city_coordinates, open(path + "cities.json", 'w') )

print(len(df['SearchString'].unique()))
print(df['SearchString'])

"""