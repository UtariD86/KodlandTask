from app import db
from models import Question, Choice

def create_base_data():

    if Question.query.count() > 0:
        print("Base data already exists!")
        return

    # Soru 1
    q1 = Question(
        is_multiple_choice=True,
        topic='Python',
        question_text='Python dilinin hangi gelişmiş özelliği, fonksiyonların kısa ve öz bir şekilde tanımlanmasını sağlar?'
    )
    c1_1 = Choice(question=q1, choice_text='Sınıflar', is_correct=False)
    c1_2 = Choice(question=q1, choice_text='Lambda fonksiyonları', is_correct=True)
    c1_3 = Choice(question=q1, choice_text='İstisnalar', is_correct=False)
    c1_4 = Choice(question=q1, choice_text='Yöntemler', is_correct=False)

    # Soru 2
    q2 = Question(
        is_multiple_choice=True,
        topic='Python',
        question_text='Python\'da dosya işleme yaparken hangi yapı kullanılır?'
    )
    c2_1 = Choice(question=q2, choice_text='try-except', is_correct=True)
    c2_2 = Choice(question=q2, choice_text='for döngüsü', is_correct=False)
    c2_3 = Choice(question=q2, choice_text='lambda', is_correct=False)
    c2_4 = Choice(question=q2, choice_text='if-else', is_correct=False)

    # Soru 3
    q3 = Question(
        is_multiple_choice=True,
        topic='OOP',
        question_text='OOP kavramlarından hangisi Python\'da sınıf ve nesne oluşturulmasında kullanılır?'
    )
    c3_1 = Choice(question=q3, choice_text='Fonksiyonlar', is_correct=False)
    c3_2 = Choice(question=q3, choice_text='Yöntemler', is_correct=False)
    c3_3 = Choice(question=q3, choice_text='Sınıflar ve nesneler', is_correct=True)
    c3_4 = Choice(question=q3, choice_text='API\'ler', is_correct=False)

    # Soru 4
    q4 = Question(
        is_multiple_choice=True,
        topic='GitHub',
        question_text='GitHub kullanarak proje yönetiminde hangi komut, projedeki değişiklikleri kaydetmek için kullanılır?'
    )
    c4_1 = Choice(question=q4, choice_text='commit', is_correct=True)
    c4_2 = Choice(question=q4, choice_text='push', is_correct=False)
    c4_3 = Choice(question=q4, choice_text='pull', is_correct=False)
    c4_4 = Choice(question=q4, choice_text='fetch', is_correct=False)

    # Soru 5
    q5 = Question(
        is_multiple_choice=True,
        topic='Web Geliştirme',
        question_text='Web geliştirme sürecinde HTML ve CSS ne için kullanılır?'
    )
    c5_1 = Choice(question=q5, choice_text='Veritabanı yönetimi', is_correct=False)
    c5_2 = Choice(question=q5, choice_text='Web sitesi düzeni ve tasarımı', is_correct=True)
    c5_3 = Choice(question=q5, choice_text='Yapay zeka modelleri', is_correct=False)
    c5_4 = Choice(question=q5, choice_text='Hata ayıklama', is_correct=False)

    # Soru 6
    q6 = Question(
        is_multiple_choice=True,
        topic='Flask',
        question_text='Flask ile geliştirilen web projelerinde hangi süreç kullanılır?'
    )
    c6_1 = Choice(question=q6, choice_text='Makine öğrenimi eğitimi', is_correct=False)
    c6_2 = Choice(question=q6, choice_text='Şablon motorları ile web sitelerinin çok sayfalı yapısının oluşturulması', is_correct=True)
    c6_3 = Choice(question=q6, choice_text='Bot entegrasyonu', is_correct=False)
    c6_4 = Choice(question=q6, choice_text='Grafik tasarım', is_correct=False)

    # Soru 7
    q7 = Question(
        is_multiple_choice=True,
        topic='API',
        question_text='Python’da bir API ile çalışma neden önemlidir?'
    )
    c7_1 = Choice(question=q7, choice_text='Daha fazla bellek kullanmak için', is_correct=False)
    c7_2 = Choice(question=q7, choice_text='Uygulamaları harici kaynaklarla entegre etmek için', is_correct=True)
    c7_3 = Choice(question=q7, choice_text='Yalnızca veri depolamak için', is_correct=False)
    c7_4 = Choice(question=q7, choice_text='Grafiksel kullanıcı arayüzü oluşturmak için', is_correct=False)

    # Soru 8
    q8 = Question(
        is_multiple_choice=True,
        topic='Makine Öğrenimi',
        question_text='Makine öğrenimi projelerinde başarıyı artıran en önemli faktör nedir?'
    )
    c8_1 = Choice(question=q8, choice_text='Hızlı algoritmalar', is_correct=False)
    c8_2 = Choice(question=q8, choice_text='Verilerin doğru ve etkili şekilde temizlenmesi', is_correct=True)
    c8_3 = Choice(question=q8, choice_text='Karmaşık kütüphaneler', is_correct=False)
    c8_4 = Choice(question=q8, choice_text='Uzun süreli eğitim', is_correct=False)

    # Soru 9
    q9 = Question(
        is_multiple_choice=True,
        topic='Lambda Fonksiyonları',
        question_text='Lambda fonksiyonları Python’da nasıl tanımlanır?'
    )
    c9_1 = Choice(question=q9, choice_text='def anahtar kelimesi ile', is_correct=False)
    c9_2 = Choice(question=q9, choice_text='lambda anahtar kelimesi ile', is_correct=True)
    c9_3 = Choice(question=q9, choice_text='class anahtar kelimesi ile', is_correct=False)
    c9_4 = Choice(question=q9, choice_text='try anahtar kelimesi ile', is_correct=False)

    # Soru 10
    q10 = Question(
        is_multiple_choice=True,
        topic='Hata Ayıklama',
        question_text='Hata ayıklama ve kod optimizasyonu sürecinde hangi araçlar kullanılır?'
    )
    c10_1 = Choice(question=q10, choice_text='Yalnızca web tarayıcıları', is_correct=False)
    c10_2 = Choice(question=q10, choice_text='IDE’ler ve Git', is_correct=True)
    c10_3 = Choice(question=q10, choice_text='Tek başına Python', is_correct=False)
    c10_4 = Choice(question=q10, choice_text='Sadece manuel işlemler', is_correct=False)

    # Soru 11
    q11 = Question(
        is_multiple_choice=True,
        topic='OOP',
        question_text='OOP prensiplerinden biri olan encapsulation neyi ifade eder?'
    )
    c11_1 = Choice(question=q11, choice_text='Veriyi dışarıya açmadan sınıf içinde saklama', is_correct=True)
    c11_2 = Choice(question=q11, choice_text='Fonksiyonların hızlı çalıştırılması', is_correct=False)
    c11_3 = Choice(question=q11, choice_text='Kütüphane yüklemeleri', is_correct=False)
    c11_4 = Choice(question=q11, choice_text='Dosya işleme', is_correct=False)

    # Soru 12
    q12 = Question(
        is_multiple_choice=True,
        topic='Veri Madenciliği',
        question_text='Veri madenciliğinde veriler nasıl görselleştirilir?'
    )
    c12_1 = Choice(question=q12, choice_text='Kodlama ile', is_correct=False)
    c12_2 = Choice(question=q12, choice_text='Şablon motorları ile', is_correct=False)
    c12_3 = Choice(question=q12, choice_text='Grafik ve görselleştirme kütüphaneleri ile', is_correct=True)
    c12_4 = Choice(question=q12, choice_text='Lambda fonksiyonları ile', is_correct=False)

    # Soru 13
    q13 = Question(
        is_multiple_choice=True,
        topic='Makine Öğrenimi',
        question_text='Bir makine öğrenimi projesinin son aşaması nedir?'
    )
    c13_1 = Choice(question=q13, choice_text='Eğitim verilerini toplamak', is_correct=False)
    c13_2 = Choice(question=q13, choice_text='Modeli test etmek ve doğruluğunu kontrol etmek', is_correct=True)
    c13_3 = Choice(question=q13, choice_text='Yeni kütüphaneler eklemek', is_correct=False)
    c13_4 = Choice(question=q13, choice_text='Verileri temizlemek', is_correct=False)

    # Soru 14 - Açık Uçlu Soru 1
    q14 = Question(
        is_multiple_choice=False,
        topic='Python ve Veri Bilimi',
        question_text='Python kullanarak bir veri bilimi projesine nasıl başlarsınız? Adımlarınızı açıklayın.'
    )

    # Soru 15 - Açık Uçlu Soru 2
    q15 = Question(
        is_multiple_choice=False,
        topic='Bilgisayar Görüşü',
        question_text='Bilgisayar görüşü projelerinin günümüz sorunlarına ne gibi faydaları olabilir? Örneklerle açıklayınız.'
    )

    # Mevcut soru ve seçenekleri bir araya toplama
    questions_choices = [
        q1, c1_1, c1_2, c1_3, c1_4,
        q2, c2_1, c2_2, c2_3, c2_4,
        q3, c3_1, c3_2, c3_3, c3_4,
        q4, c4_1, c4_2, c4_3, c4_4,
        q5, c5_1, c5_2, c5_3, c5_4,
        q6, c6_1, c6_2, c6_3, c6_4,
        q7, c7_1, c7_2, c7_3, c7_4,
        q8, c8_1, c8_2, c8_3, c8_4,
        q9, c9_1, c9_2, c9_3, c9_4,
        q10, c10_1, c10_2, c10_3, c10_4,
        q11, c11_1, c11_2, c11_3, c11_4,
        q12, c12_1, c12_2, c12_3, c12_4,
        q13, c13_1, c13_2, c13_3, c13_4,
        q14, q15
    ]

    db.session.add_all(questions_choices)
    db.session.commit()

if __name__ == '__main__':
    create_base_data()
    print("Base data created!")
