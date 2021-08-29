from flask import Flask, render_template
import data
from random import randint

app = Flask(__name__)


@app.route('/')
def render_main():
    header = dict(title=data.title,
                  departures=data.departures)
    main = dict(subtitle=data.subtitle,
                desc=data.description)
    tours = dict()
    key = 1
    while key <= 6:
        number = randint(1, 16)
        if number not in tours:
            tours[number] = dict(title=data.tours[number]['title'],
                                 desc=data.tours[number]['description'],
                                 pic=data.tours[number]['picture'])
            key += 1

    main['tours'] = tours
    return render_template('index.html', header=header, main=main)


@app.route('/departures/<departure>/')
def render_departure(departure):
    header = dict(title=data.title,
                  departures=data.departures)
    departures = dict(place_departure=data.departures[departure])
    prices, nights = list(), list()
    tours = dict()
    for tour_id, tour in data.tours.items():
        if departure == tour['departure']:
            prices.append(tour['price'])
            nights.append(tour['nights'])
            tour = dict(desc=tour['description'],
                        title=tour['title'],
                        pic=tour['picture'])
            tours[tour_id] = tour
    departures['tours'] = tours
    print(departures)
    return render_template('departure.html', header=header, departures=departures, prices=prices, nights=nights)


@app.route('/tours/<int:tour_id>/')
def render_tour(tour_id):
    header = dict(title=data.title,
                  departures=data.departures)
    return render_template('tour.html', header=header)


if __name__ == "__main__":
    app.run(debug=True)
