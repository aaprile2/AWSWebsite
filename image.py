import filters
from PIL import Image


def filter_image(fil, photopath):
    photo = Image.open('static/' + photopath)
    if fil == 'Gray':
        img = filters.gray(photo)
    elif fil == 'Sepia':
        img = filters.sepia(photo)
    elif fil == 'Poster':
        img = filters.poster(photo)
    elif fil == 'Blur':
        img = filters.blur(photo)
    elif fil == 'Edge':
        img = filters.edge(photo)
    elif fil == 'Solar':
        img = filters.solar(photo)
    # local save
    outputpath = mutate_filename(photopath, fil)
    img.save('static/' + outputpath)
    return outputpath


def mutate_filename(photopath, fil):
    photopath_split = photopath.split('.')
    return photopath_split[0] + '_' + fil + '.' + photopath_split[1]