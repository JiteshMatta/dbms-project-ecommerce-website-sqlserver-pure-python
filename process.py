def processIncomingData(path, reqdata):
	url = path
	if (url == "/"):
		url = "index.html"
	else:
		pass
	while (url[-1] == "/" and len(url) > 1):
		url = url[:-1]
	# print(url)
	try:
		f = open(url, "rb")
		content = f.read()
	except:
		# print("Error")
		content = ""
	try:
		ext = url.split('.')[-1]
	except:
		ext = ""
	while (len(ext) > 1 and ext[-1] == '/'):
		ext = ext[:-1]
	mimetypes = {
		"css": "text/css",
		"html": "text/html",
		"js": "application/javascript",
		"jpg": "image/jpeg",
		"png": "image/png",
		"ico": "image/x-icon",
	}
	mimetype = mimetypes.get(ext, "text/html")
	data = reqdata.decode("utf-8").split(" ")
	# print(mimetype)
	return content, mimetype, data