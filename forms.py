from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class filter(FlaskForm):
    fil = RadioField('Filter', choices=[('Gray', 'Gray'), ('Sepia', 'Sepia'), ('Poster', 'Poster'), ('Blur', 'Blur'),
                                        ('Edge', 'Edge'), ('Solar', 'Solar')])
    submit = SubmitField('Apply Filter!')

class photoUpload(FlaskForm):
    photo = FileField()#'Image', validators=[FileRequired(), FileAllowed(UploadSet('images', IMAGES), 'Images only!')])

