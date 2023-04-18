from flask import Flask, render_template, request
import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/flights', methods=['POST'])
def flights():

    flight_data = pd.read_csv('flight_data.csv')


    origin = request.form['origin']
    destination = request.form['destination']
    departure_date = request.form['departure_date']


    filtered_data = flight_data[(flight_data['origin'] == origin) & (flight_data['destination'] == destination) & (flight_data['departure_date'] == departure_date)]


    flights = filtered_data.to_dict('records')


    return render_template('flights.html', flights=flights)



@app.route('/book/<flight_number>', methods=['GET', 'POST'])
def book(flight_number):

        with open('flight_data.json') as f:
            flight_data = json.load(f)


        flight = next(flight for flight in flight_data if flight['flight_number'] == flight_number)

        if request.method == 'POST':


            return redirect('/confirmation')

        return render_template('book.html', flight=flight)


    origin = request.form['origin']
    destination = request.form['destination']
    departure_date = request.form['departure_date']


    filtered_data = [flight for flight in flight_data if flight['origin'] == origin and flight['destination'] == destination and flight['departure_date'] == departure_date]

return render_template('flights.html', flights=filtered_data)


if __name__ == '__main__':
    app.run(debug=True)
