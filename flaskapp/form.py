# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms import IntegerField, StringField, TextField,\
    PasswordField, validators, SelectMultipleField, widgets,SubmitField

class LoginForm(Form):
    email = EmailField('email', [validators.DataRequired(message=u"Introducir correo")])
    password = PasswordField('Password', [validators.DataRequired(message=u"Introducir contraseña")])

class SignUpForm(Form):
    nombre = StringField('nombre', [validators.DataRequired(message=u"Introducir nombre")])
    apellidos = StringField('apellidos', [validators.DataRequired(message=u"Introducir apellidos")])
    correo = EmailField('correo', [validators.DataRequired(message=u"Introducir correo"),\
                                    validators.Email()])
    curp = StringField('curp', [validators.DataRequired(message=u"Introducir curp")])
    escuela = StringField('escuela', [validators.DataRequired(message=u"Introducir escuela")])
    ciudad = StringField('ciudad', [validators.DataRequired(message=u"Introducir ciudad")])
    edad = IntegerField('edad', [validators.DataRequired(message=u"Introducir edad")])
    concursos = SelectMultipleField(choices=[('Matematicas', 'Matemáticas'.decode("utf8")),\
            ('Fisica', 'Física'.decode("utf8")), ('Pre-selectivo de física'.decode("utf8"), 'Pre-selectivo de física'.decode("utf8"))],\
                option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False), validators=[validators.DataRequired(message=u'Selecciona al menos un concurso')])
    password = PasswordField('password', [validators.DataRequired(message="Introducir contraseña".decode("utf8"))])
    submit = SubmitField('registro')
