mimetypes = {
		"css": "text/css",
		"html": "text/html",
		"js": "application/javascript",
		"jpg": "image/jpeg",
		"png": "image/png",
		"ico": "image/x-icon",
	}

templates = [
	"index.html",
	"cart.html",
	"checkout.html",
	"contact.html",
	"product.htmls",
	"product_detail.html",
	"register.html",
	"profile",
	]

def processIncomingData(path):
	url = path
	if (url == "/" or url == ""):
		url = "index.html"
	else:
		pass
	while ((url[-1] < 'a' or url[-1] > 'z') and (url[-1] < 'A' or url[-1] > 'Z') and len(url) > 1):
		url = url[:-1]

	file = url.split('/')[-1]

	try:
		f = open(url, "rb")
		content = f.read()
	except:
		content = ""

	try:
		ext = url.split('.')[-1]
	except:
		ext = ""
	while (len(ext) > 1 and ext[-1] == '/'):
		ext = ext[:-1]

	mimetype = mimetypes.get(ext, "text/html")
	return file, content, mimetype