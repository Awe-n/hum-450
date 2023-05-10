import sys
from geopy.geocoders import Nominatim

def correct_city_names(misspelled_cities):
    geolocator = Nominatim(user_agent="geoapiExercises")

    corrected_cities = []
    for city in misspelled_cities:
        location = geolocator.geocode(city)

        if location:
            address = location.address.split(',')
            city_name = None

            for component in address:
                if "city" in geolocator.address_component(component.strip(), "city"):
                    city_name = component.strip()
                    break

            if not city_name:
                city_name = address[0].strip()

            corrected_cities.append(city_name)
        else:
            corrected_cities.append(None)

    return corrected_cities


if __name__ == "__main__":
    misspelled_cities = ['Nw Yrok', 'Pari', 'Lndon', 'Toyko', 'Sdney']
    corrected_cities = correct_city_names(misspelled_cities)
    print(corrected_cities)
