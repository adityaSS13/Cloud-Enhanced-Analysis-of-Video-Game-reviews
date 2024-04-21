import requests
import urllib.request
import xml.etree.ElementTree as ET

def get_cover_art_url(game_name, api_key):
    # Construct the API endpoint URL

    url = f'https://www.giantbomb.com/api/games/?api_key={api_key}&format=xml&query={game_name}&resources=game&field_list=game,image&limit=1'
    response = urllib.request.urlopen(url)

    # Parse the XML response
    root = ET.fromstring(response.read())

    # Navigate to the original_url of the image for the first game
    original_url = root.find('.//game/image/original_url').text
    return original_url
