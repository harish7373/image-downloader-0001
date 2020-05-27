from flask import *
from id import Downloader

app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def download():
	listi=list()
	if request.method == "POST":
		text = request.form['hello']
		print(text)
		images = Downloader.download(text)
		print(len(images))
		for image in images:
			if 'error' not in image:
				try:
					listi.append(image['src'])
				except KeyError:
					print("")
				try:
					listi.append(image['data-src'])
				except KeyError:
					print("")

		return render_template("link.html", text="Downladed Succesfully", listi=listi)
	else:
   		return render_template("link.html")



if __name__ == '__main__':
   app.run(debug = True)  