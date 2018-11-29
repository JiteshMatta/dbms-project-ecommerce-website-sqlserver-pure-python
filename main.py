from flask import Flask, request, Response
import os
from process import processIncomingData

# print(__name__)

app = Flask(__name__)

@app.route('/', defaults={'path': '/'}, methods = ['GET', 'POST'])
@app.route('/<path:path>/', methods = ['GET', 'POST'])
def handleRequest(path):
	content, mimetype, data = processIncomingData(path, request.data)
	if request.method == 'POST':
		if (data[0] == "login"):
			return ("Success ahihi")
	else:
		if (mimetype == "text/html"):
			content = content.decode("utf-8").replace("{user_display}", "login").replace("{user_link}", "register.html")
		return Response(content, mimetype=mimetype)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=9999)