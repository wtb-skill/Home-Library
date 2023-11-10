from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, FileField, HiddenField
from wtforms.validators import DataRequired, Email


class BooksForm(FlaskForm):
    id = HiddenField()
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    description = TextAreaField('Description')
    read_or_not = BooleanField('Read')

    def set_id(self, book_id):
        self.id.data = book_id

