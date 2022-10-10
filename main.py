from weather import Weather
from flask import request, make_response, Flask, jsonify

# print(socket.gethostbyname(socket.getfqdn(socket.gethostname())))

app = Flask(__name__)
# run_with_ngrok(app)

@app.route('/')
def landing():
  return make_response(jsonify({'message': "This is the landing page for our weather app. To get today's weather info use the endpoint '/today?city={city}'. To get the 7 day forecast go to '/forecast?city={city}"}))

@app.route('/today', methods=['GET'])
def today():
  city = request.args.get('city')
  today = Weather(city).today()
  return make_response(jsonify({'today': today}))

@app.route('/forecast', methods=['GET'])
def forecast():
  city = request.args.get('city')
  forecast = Weather(city).forecast()
  return make_response(jsonify({'forecast': forecast}))

if __name__ == '__main__':
  app.run(debug=True)