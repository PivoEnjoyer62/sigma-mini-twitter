from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Ім\'я користувача',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Емейл',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Підтвердити пароль',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зареєструватися')


class LoginForm(FlaskForm):
    email = StringField('Емейл',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запам\'ятати мене')
    submit = SubmitField('Увійти')
