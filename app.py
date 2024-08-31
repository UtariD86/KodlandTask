import os
from flask import Flask, render_template, request, flash, redirect, url_for
from models import db, Question, Answer
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import jsonify
import basedata  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kodland.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Flask'ın flash mesajları için gerekli

db.init_app(app)

@app.route('/')
def index():
    multiple_choice_questions = Question.query.filter_by(is_multiple_choice=True).all()
    open_ended_questions = Question.query.filter_by(is_multiple_choice=False).all()
    return render_template('index.html', 
                           multiple_choice_questions=multiple_choice_questions, 
                           open_ended_questions=open_ended_questions)


from flask import jsonify

@app.route('/submit', methods=['POST'])
def submit():
    user_ip = request.remote_addr
    user_first_name = request.form.get('name')
    user_last_name = request.form.get('surname')

    # IP kontrolü
    existing_submission = Answer.query.filter_by(user_ip=user_ip).first()
    if existing_submission:
        return jsonify({'status': 'error', 'message': 'Daha önce testi tamamladığınızı tespit ettik. Yeni cevaplarınız kaydedilmeyecek!'}), 400

    try:
        # Çoktan seçmeli soruların işlenmesi
        multiple_choice_questions = Question.query.filter_by(is_multiple_choice=True).all()
        for question in multiple_choice_questions:
            selected_choice_id = request.form.get(f'question_{question.id}')
            if selected_choice_id:
                answer = Answer(
                    user_first_name=user_first_name,
                    user_last_name=user_last_name,
                    user_ip=user_ip,
                    is_multiple=True,
                    question_id=question.id,
                    choice_id=int(selected_choice_id)
                )
                db.session.add(answer)

        # Açık uçlu soruların işlenmesi
        open_ended_questions = Question.query.filter_by(is_multiple_choice=False).all()
        for question in open_ended_questions:
            answer_text = request.form.get(f'question_{question.id}')
            if answer_text:
                answer = Answer(
                    user_first_name=user_first_name,
                    user_last_name=user_last_name,
                    user_ip=user_ip,
                    is_multiple=False,
                    question_id=question.id,
                    answer_text=answer_text
                )
                db.session.add(answer)

        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Cevaplar başarıyla kaydedildi!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Bir hata oluştu: {str(e)}'}), 500


if __name__ == '__main__':
    with app.app_context():
        # Veritabanı dosyasının mevcut olup olmadığını kontrol et
        db_file = 'kodland.db'
        if not os.path.exists(db_file):
            db.create_all()  # Veritabanını ve tabloları oluştur
            basedata.create_base_data()  # basedata.py'deki fonksiyonu tetikleyerek temel veriyi ekle
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True)
