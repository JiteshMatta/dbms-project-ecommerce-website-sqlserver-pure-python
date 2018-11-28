from flask import Flask, request, Response
import os
from process import processIncomingData

# print(__name__)

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods = ['GET', 'POST'])
@app.route('/<path:path>/', methods = ['GET', 'POST'])
def handleRequest(path):
	file, content, mimetype = processIncomingData(path)
	if request.method == 'POST':
		print(request.form)
		# if (request.form['request'] == 'login'):
		# 	if (request.form['username'] == request.form['password']):
		# 		return ("Ok!")
		# 	else:
		# 		return ("Wrong!")
		# print(request.form.get("request"))
		try:
			print(request.form['request'].decode("utf-8"))
			print(request.form['username'].decode("utf-8"))
			print(request.form['password'].decode("utf-8"))
		except:
			pass
		return("OK!")
		if (mimetype == "text/html"):
			content = content.decode("utf-8").replace("{user_display}", "Login").replace("{user_page}", "register")
		return Response(content, mimetype=mimetype)
	else:
		if (mimetype == "text/html"):
			content = content.decode("utf-8").replace("{user_display}", "Login").replace("{user_page}", "register")
		return Response(content, mimetype=mimetype)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=9999)