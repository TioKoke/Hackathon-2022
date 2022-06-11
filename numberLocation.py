from cgitb import html
import phonenumbers
import folium
from phonenumbers import geocoder

key = '2fca60db6ac54b0fb3612236e0a1debb'
number='+56920095440'
sanNumber= phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber,"es")
print(yourLocation)

#obtener el provedor servicio
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"es"))

#obtener latitud y longtidud 

from opencage.geocoder import OpenCageGeocode
def ubicacion(): 
    geocoder = OpenCageGeocode(key)
    query = str(yourLocation)
    results= geocoder.geocode(query)
    #print(results)
    lat= results[0]['geometry']['lat']
    lng= results[1]['geometry']['lng']

    print(lat,lng)

    myMap = folium.Map(location=[lat,lng],zoom_start=9)

    folium.Marker([lat,lng],popvp=yourLocation).add_to((myMap))
    myMap.save("myLocation.html")
