import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from models import db, Question, Answer, Submit, Choice
from werkzeug.middleware.proxy_fix import ProxyFix
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kodland.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

questionCount = 3

@app.route('/')
def index():
    username = request.cookies.get('username', '')

    multiple_choice_questions = Question.query.filter_by(is_multiple_choice=True).all()
    selected_questions = random.sample(multiple_choice_questions, questionCount) if len(multiple_choice_questions) > questionCount else multiple_choice_questions
    open_ended_questions = Question.query.filter_by(is_multiple_choice=False).all()

    if username:
        submit_records = Submit.query.filter_by(username=username).order_by(Submit.submit_date.desc()).all()
        highest_score = max(submit.score for submit in submit_records) if submit_records else 0
        last_score = submit_records[0].score if submit_records else 0
    else:
        highest_score, last_score = 0, 0

    highest_score = int(highest_score) if highest_score == 100 else round(highest_score, 2)
    last_score = int(last_score) if last_score == 100 else round(last_score, 2)

    return render_template('index.html', multiple_choice_questions=selected_questions, open_ended_questions=open_ended_questions, highest_score=highest_score, last_score=last_score, username=username)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    response = make_response()
    response.set_cookie('username', username)

    try:
        submit = Submit(username=username, correct_answers=0, score=0.0)
        db.session.add(submit)
        db.session.commit()

        correct_answers_count = 0
        multiple_choice_questions = Question.query.filter_by(is_multiple_choice=True).all()

        for i in range(len(multiple_choice_questions)):
            selected_choice_id = request.form.get(f'question_{i}')
            if selected_choice_id:
                answer = Answer(username=username, is_multiple=True, question_id=i, choice_id=int(selected_choice_id), submit_id=submit.id)
                db.session.add(answer)

                correct_choice = Choice.query.filter_by(id=int(selected_choice_id), is_correct=True).first()
                if correct_choice:
                    correct_answers_count += 1

        open_ended_questions = Question.query.filter_by(is_multiple_choice=False).all()
        for question in open_ended_questions:
            answer_text = request.form.get(f'question_{question.id}')
            if answer_text:
                answer = Answer(username=username, is_multiple=False, question_id=question.id, answer_text=answer_text, submit_id=submit.id)
                db.session.add(answer)

        score_percentage = (correct_answers_count / questionCount) * 100 if questionCount > 0 else 0
        submit.score = round(score_percentage, 2)
        submit.correct_answers = correct_answers_count
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Cevaplar başarıyla kaydedildi! Skorunuz: %' + str(submit.score)}), 200, response.headers
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Bir hata oluştu: {str(e)}'}), 500

if __name__ == '__main__':
    with app.app_context():
        db_file = 'kodland.db'
        if not os.path.exists(db_file):
            db.create_all()
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True)
