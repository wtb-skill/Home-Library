from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, HiddenField
from wtforms.validators import DataRequired


class BooksForm(FlaskForm):
    id = HiddenField()
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    description = TextAreaField('Description')
    read = BooleanField('Read')

    def set_id(self, book_id):
        self.id.data = int(book_id)

