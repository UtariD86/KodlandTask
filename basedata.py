from app import db
from models import Question, Choice

def create_base_data():

    if Question.query.count() > 0:
        print("Base data already exists!")
        return

    # Soru 1 - Python'da AI Geliştirme
    q1 = Question(
        is_multiple_choice=True,
        topic='Python\'da AI geliştirme',
        question_text='Python ile AI geliştirmek için hangi kütüphane en yaygın olarak kullanılır?'
    )
    c1_1 = Choice(question=q1, choice_text='TensorFlow', is_correct=True)
    c1_2 = Choice(question=q1, choice_text='React', is_correct=False)
    c1_3 = Choice(question=q1, choice_text='Django', is_correct=False)
    c1_4 = Choice(question=q1, choice_text='Flask', is_correct=False)

    # Soru 2 - Bilgisayar Görüşü
    q2 = Question(
        is_multiple_choice=True,
        topic='Bilgisayar görüşü',
        question_text='Bilgisayar görüşü projelerinde hangi Python kütüphanesi sıklıkla kullanılır?'
    )
    c2_1 = Choice(question=q2, choice_text='OpenCV', is_correct=True)
    c2_2 = Choice(question=q2, choice_text='Numpy', is_correct=False)
    c2_3 = Choice(question=q2, choice_text='Pandas', is_correct=False)
    c2_4 = Choice(question=q2, choice_text='Scikit-learn', is_correct=False)

    # Soru 3 - NLP
    q3 = Question(
        is_multiple_choice=True,
        topic='NLP (Nöro-dilbilim)',
        question_text='Python\'da NLP işlemleri için en çok kullanılan kütüphane hangisidir?'
    )
    c3_1 = Choice(question=q3, choice_text='NLTK', is_correct=True)
    c3_2 = Choice(question=q3, choice_text='Matplotlib', is_correct=False)
    c3_3 = Choice(question=q3, choice_text='Seaborn', is_correct=False)
    c3_4 = Choice(question=q3, choice_text='TensorFlow', is_correct=False)

    # Soru 4 - Python Uygulamalarında AI Modelleri Uygulama
    q4 = Question(
        is_multiple_choice=True,
        topic='Python uygulamalarında AI modelleri uygulama',
        question_text='Python\'da AI modelleri uygulamak için hangi kütüphane yaygın olarak kullanılır?'
    )
    c4_1 = Choice(question=q4, choice_text='Keras', is_correct=True)
    c4_2 = Choice(question=q4, choice_text='Flask', is_correct=False)
    c4_3 = Choice(question=q4, choice_text='Vue.js', is_correct=False)
    c4_4 = Choice(question=q4, choice_text='Bootstrap', is_correct=False)

  # Soru 5 - Açık Uçlu Soru -1
    q5 = Question(
        is_multiple_choice=False,
        topic='Python ve Veri Bilimi',
        question_text='Python kullanarak bir veri bilimi projesine nasıl başlarsınız? Adımlarınızı açıklayın.'
    )

  # Soru 6 - Açık Uçlu Soru - 2
    q6 = Question(
        is_multiple_choice=False,
        topic='Bilgisayar Görüşü',
        question_text='Bilgisayar görüşü projelerinin günümüz sorunlarına ne gibi faydaları olabilir? Örneklerle açıklayınız.'
    )

    # Mevcut soru ve seçenekleri bir araya toplama
    questions_choices = [q1, c1_1, c1_2, c1_3, c1_4,
                         q2, c2_1, c2_2, c2_3, c2_4,
                         q3, c3_1, c3_2, c3_3, c3_4,
                         q4, c4_1, c4_2, c4_3, c4_4,
                         q5,
                         q6]

    db.session.add_all(questions_choices)
    db.session.commit()

if __name__ == '__main__':
    create_base_data()
    print("Base data created!")
