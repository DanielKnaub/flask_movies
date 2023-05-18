from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[DataRequired(message='Поле не должно быть пустым!')]
    )
    text = TextAreaField(
        'Текст отзыва',
        validators=[DataRequired(message="Поле не должно быть пустым")]
    )
    mark = SelectField('Ваша оценка', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    submit = SubmitField('Добавить')


class MovieForm(FlaskForm):
    title = StringField(
        'Название фильма',
        validators=[DataRequired(message='Поле не должно быть пустым!')]
    )
    memo = TextAreaField(
        'Описание фильма',
        validators=[DataRequired(message='Поле не должно быть пустым!')]
    )
    image = FileField(
        'Постер к фильму',
        validators=[
            FileRequired(message='Поле не должно быть пустым!'),
            FileAllowed(
                ['jpg', 'png', 'jpeg'],
                message='Неверный формат файла!'
            )
        ]
    )
    submit = SubmitField('Добавить')
