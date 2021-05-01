import json
import os

from flask import Flask
from flask import request
from flask import make_response

#Flask app should start in global layout

app = Flask(__name__)

@app.route('/webhook', method=['POST'])
def webhook():
	req= request.get_json(silent=True,force=True)
	print(json.dumps(req,indent=4))

	res=makeResponse(req)
	res=json.dumps(res, indent=4)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def makeResponse(req):
	result = req.get("result")
	parameters = result.get("parameters")
	city = parameters.get("geo-city")
	date = parameters.get("date")
	r=request.get(http://api.openweathermap.org/data/2.5/forecast?q=+city+&appid=b51422adcff9620e57ee50e8d8326233
)
	json_object= r.json()
	weather = json_object['list']
	for i in len(weather):
		if date in weather[i]['dt_txt']:
			condition = weather[i]['weather'][0]['description']
			break
	speech = "The forecats for " +city+ "for "+date" is " +condition
	return{
	"speech":speech
	"displayText":speech
	"source":"apiai-weather-webhook"
	}


if __name__ == '__main__':
	port= int(os.getenv('PORT',5000))
	print("Starting app on port %d" % port)
	app.run(debug=False, port=port,host='0.0.0.0')