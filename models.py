from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Professor(db.Model):
    __tablename__ = 'professor'

    id_professor = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(300), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    celular = db.Column(db.String(30), nullable=False)
    endereco = db.Column(db.String(300), nullable=False)
    cpf = db.Column(db.String(30), unique=True, nullable=False)
    bio = db.Column(db.String(300))
    foto_perfil = db.Column(db.String(300))
    email = db.Column(db.String(300), unique=True, nullable=False)
    senha = db.Column(db.String(300), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)