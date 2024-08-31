from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    is_multiple_choice = db.Column(db.Boolean, nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    question_text = db.Column(db.String(200), nullable=False)
    
    choices = db.relationship('Choice', backref='question', lazy=True)

class Choice(db.Model):
    __tablename__ = 'choices'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    choice_text = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(50), nullable=False)
    user_last_name = db.Column(db.String(50), nullable=False)
    user_ip = db.Column(db.String(45), nullable=False)  # Kullanıcı IP adresini saklamak için
    is_multiple = db.Column(db.Boolean, nullable=False)  # Sorunun çoktan seçmeli olup olmadığını belirtir
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    choice_id = db.Column(db.Integer, nullable=True)  # Çoktan seçmeli cevaplar için
    answer_text = db.Column(db.String(200), nullable=True)  # Metin tabanlı cevaplar için

    question = db.relationship('Question', backref=db.backref('answers', lazy=True))
