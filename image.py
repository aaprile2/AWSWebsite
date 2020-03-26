import test
from PIL import Image

def filter_image(fil, photopath):
    photo = Image.open('static/' + photopath)
    if fil == 'Gray':
        img = test.gray(photo)
    elif fil == 'Sepia':
        img = test.sepia(photo)
    elif fil == 'Poster':
        img = test.poster(photo)
    elif fil == 'Blur':
        img = test.blur(photo)
    elif fil == 'Edge':
        img = test.edge(photo)
    elif fil == 'Solar':
        img = test.solar(photo)
    # local save
    outputpath = mutate_filename(photopath, fil)
    img.save('static/' + outputpath)
    # s3 save
    # TODO
    return outputpath

def mutate_filename(photopath, fil):
    photopath_split = photopath.split('.')
    return photopath_split[0] + '_' + fil + '.' + photopath_split[1]