import requests


API_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
API_KEY = "AIzaSyBCsWQFnT-3NO4z7xfxbDceGgmGRjNDUa4"


def find_address(adress: str) -> dict:
    """esta funcion recibe la ubicacion que recibe de los text edit y
    haciendo uso de la API GEOCODING
    (https://developers.google.com/maps/documentation/geocoding/start?hl=es-419) de google maps
    obtenemos la latitud y longitud de la ubicacion propocionada

    Args:
        adress (str): ubicacion a encontrar

    Returns:
        dict: diccionario con dos claves, [coordinates, address]
    """
    url = f"{API_URL}{adress}&key={API_KEY}"

    response = requests.get(url)

    location = response.json()['results'][0]['geometry']['location']

    latitud = location['lat']
    longitud = location['lng']

    return {
        'coordinates': [latitud, longitud],
        'address': adress
    }