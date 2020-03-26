from flask import render_template, request, redirect, send_from_directory
import image
import forms
#from werkzeug import secure_filename

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'puppies'


@app.route('/', methods=['GET', 'POST'])
def upload():
    form = forms.photoUpload()
    if request.method == 'POST':

        if form.validate_on_submit():

            #filename = secure_filename(form.photo.data.filename)
            form.photo.data.save('static/' + form.photo.data.filename)
            photo = form.photo.data
            return redirect("/filter/" + form.photo.data.filename)
    return render_template('upload.html', form=form)


@app.route('/filter/<photopath>', methods=['GET', 'POST'])
def render_filter_page(photopath):
    form = forms.filter()
    return render_template('filter.html', form=form, photopath=photopath)


@app.route("/filter/<photopath>/process", methods=['POST'])
def filter(photopath):
    form = forms.filter()
    if request.method == 'POST':
        if form.submit.data:
            fil = form.fil.data
            outputpath = image.filter_image(fil, photopath)

            return render_template('filter_child.html', form=form, photopath=photopath,
                                   outputpath=outputpath)

    return render_template('filter.html', form=form)


@app.route("/download/<outputpath>", methods=['GET'])
def download(outputpath):
    if request.method == 'GET':
        return send_from_directory('static/', outputpath)


if __name__ == '__main__':
    app.run(debug=True)
