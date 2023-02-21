import folium


def create_map(info_address: dict) -> folium.Map:

    """crea mapa interactivo en base a la informacion proporcionada.

    Introducimos:
        info_address: (dict) {
            'coordinates': [latitud, longitud],
            'address': direccion inicial
        }

    Devuelve:
        folium.Map: mapa hecho usando libreria folium
    """

    # create map
    map = folium.Map(location=info_address['coordinates'], zoom_start=18)

    # Add marker
    folium.Marker(
        location=info_address['coordinates'],
        tooltip=info_address['address']
    ).add_to(map)

    return map