import requests
import re
import html

def decode_escape_sequences(string):
    return re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), string)

def generate_metacritic_url(game_name):
    formatted_name = game_name.lower().replace(' ', '-')
    formatted_name = formatted_name.replace(':', '')
    return f"https://www.metacritic.com/game/{formatted_name}/user-reviews/?platform=playstation-4"

def scrape_game_reviews(url):
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        html_content = response.content
        html_content_str = html_content.decode("utf-8")
        pattern = r'quote:"([^"]*)"'
        matches = re.findall(pattern, html_content_str)
        decoded_reviews = [html.unescape(match) for match in matches]
        decoded_reviews = [review.replace('\\n', ' ') for review in decoded_reviews]
        decoded_reviews = [decode_escape_sequences(review) for review in decoded_reviews]
        return decoded_reviews
    return []
