from weather import Weather
from flask import request, make_response, Flask, jsonify

# print(socket.gethostbyname(socket.getfqdn(socket.gethostname())))

app = Flask(__name__)
# run_with_ngrok(app)


@app.route('/today', methods=['GET'])
def get():
  city = request.args.get('city')

  if request.url == '/':
    return make_response(
      jsonify({'message': 'not a recognised endpoint'}),
      404,
    )

  if city == None:
    return make_response(
      jsonify({'message': 'missing value for "city" parameter'}),
      204,
    )

  if isinstance(city, str) == False:
    return make_response(
      jsonify({
        'message':
        f'incorrect data type for "city" parameter. Expected str but got {type(city)}'
      }),
      400,
    )
  today = Weather(city).today()
  forecast = Weather(city).forecast()

  return make_response(jsonify({'today': today, 'forecast': forecast}))


# @app.route('/forecast', methods=['GET'])
# def forecast():
#   city = request.args.get('city')
#   forecast = Weather(city).forecast()
#   return make_response(jsonify({'forecast': forecast}))

if __name__ == '__main__':
  app.run(debug=True)
