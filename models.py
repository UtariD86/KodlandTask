from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    username = db.Column(db.String(50), nullable=False)
    is_multiple = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    choice_id = db.Column(db.Integer, nullable=True)  # Çoktan seçmeli cevaplar için
    answer_text = db.Column(db.String(200), nullable=True)  # Metin tabanlı cevaplar için
    submit_id = db.Column(db.Integer, db.ForeignKey('submits.id'), nullable=False)  # Submit ID referansı

    question = db.relationship('Question', backref=db.backref('answers', lazy=True))
    submit = db.relationship('Submit', backref=db.backref('answers', lazy=True))

class Submit(db.Model):
    __tablename__ = 'submits'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)  # Kullanıcının adı
    correct_answers = db.Column(db.Integer, nullable=False)  # Doğru sayısı
    submit_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Gönderim tarihi
    score = db.Column(db.Float, nullable=False)  # 100 üzerinden puanlama, max 1.0 olacak şekilde

    def __repr__(self):
        return f'<Submit {self.id} - Username: {self.username} - Score: {self.score}>'
