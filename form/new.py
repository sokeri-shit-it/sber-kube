from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class MainForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    network_main = StringField('Название сети', validators=[DataRequired()])
    org = StringField('Тенант', validators=[DataRequired()])
    vdc = StringField('ВДЦ', validators=[DataRequired()])
    domain = StringField('Доменное имя', validators=[DataRequired()])
    network = StringField('Подсеть ВДЦ', validators=[DataRequired()])
    lb = StringField('Балансиры', validators=[DataRequired()])
    master = StringField('Мастера', validators=[DataRequired()])
    router = StringField('Роутеры', validators=[DataRequired()])
    service_logging = StringField('Сервисы логирования', validators=[DataRequired()])
    service_monitoring = StringField('Сервисы мониторинга', validators=[DataRequired()])
    worker = StringField('Воркеры', validators=[DataRequired()])
    com1 = BooleanField('Компонент 1')
    com2 = BooleanField('Компонент 2')
    com3 = BooleanField('Компонент 3')
    com4 = BooleanField('Компонент 4')
    com5 = BooleanField('Компонент 5')
    submit = SubmitField('Пуск')
