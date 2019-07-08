from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    """
    Class for users to write their own pitches
    """

    title = StringField('Blog title',validators=[Required()])
    blog = TextAreaField('Write a new blog')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    """
    Class to update our profile
    """
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')