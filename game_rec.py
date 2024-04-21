from flask import Flask, render_template, request, redirect, url_for
from utils.scraper import generate_metacritic_url, scrape_game_reviews
from utils.sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def input_game():
    if request.method == 'POST':
        game_name = request.form['game_name']
        url = generate_metacritic_url(game_name)
        review_data = scrape_game_reviews(url)
        sentiment_label, sentiment_probs = analyze_sentiment(review_data)
        return redirect(url_for('dashboard', game_name=game_name, sentiment_label=sentiment_label, sentiment_probs=sentiment_probs))
    return render_template('input.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    game_name = request.args.get('game_name')
    sentiment_label = request.args.get('sentiment_label')
    sentiment_probs = request.args.get('sentiment_probs')
    if game_name and sentiment_label and sentiment_probs:
        return render_template('dashboard.html', game_name=game_name, sentiment_label=sentiment_label, sentiment_probs=sentiment_probs)
    else:
        return redirect(url_for('input_game'))

if __name__ == '__main__':
    app.run(debug=True)
