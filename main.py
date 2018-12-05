from __future__ import print_function
import sys
from flask import Flask, request, Response
import os
from process import processIncomingData

# print(__name__)

app = Flask(__name__)

@app.route('/', defaults={'path': '/'}, methods = ['GET', 'POST'])
@app.route('/<path:path>/', methods = ['GET', 'POST'])
def handleRequest(path):
	print(request.form)
	print(request.method)
	content, mimetype, data = processIncomingData(path, request.data)
	if request.method == 'POST':
		req = ""
		try:
			req = request.form['request']
		except:
			req = ""
		if req == "":
			return "ahihi, do ngoc"
		else:
			return "dung roi, ban gioi qua"
		# if (mimetype == "text/html"):
		# 	content = content.decode("utf-8").replace("{user_display}", "login").replace("{user_link}", "register.html")
		# return Response(content, mimetype=mimetype)
	else:
		if (mimetype == "text/html"):
			content = content.decode("utf-8").replace("{user_display}", "login").replace("{user_link}", "register.html")
		return Response(content, mimetype=mimetype)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=9999)