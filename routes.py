from flask import render_template, request, redirect, send_from_directory, send_file
import image
import forms
import boto3

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'puppies'
app.config['bucket'] = 'aprileproject1'

@app.route('/', methods=['GET'])
def reroute():
    return redirect('/home')
@app.route('/home', methods=['GET', 'POST'])
def upload():
    form = forms.photoUpload()
    if request.method == 'POST':

        if form.validate_on_submit():

            form.photo.data.save('static/' + form.photo.data.filename)
            #s3_client = boto3.client('s3')
            #valid = s3_client.upload_file('static/' + form.photo.data.filename, app.config['bucket'], form.photo.data.filename)
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
            #s3_client = boto3.client('s3')
            #valid = s3_client.upload_file('static/' + outputpath, app.config['bucket'], outputpath)
            return render_template('filter_child.html', form=form, photopath=photopath,
                                   outputpath=outputpath)

    return render_template('filter.html', form=form)


@app.route("/download/<outputpath>", methods=['GET'])
def download(outputpath):
    if request.method == 'GET':
        s3 = boto3.resource('s3')
        fileoutputname = "downloads/" + outputpath
        #s3.Bucket(app.config['bucket']).download_file(outputpath, fileoutputname)
        return send_from_directory('static/', outputpath)
        #return send_file(fileoutputname, as_attachment=True)

if __name__ == '__main__':
    #app.run(host="0.0.0.0", port="80")
    #app.run(host="0.0.0.0", debug=True)
    app.run(debug=True)
