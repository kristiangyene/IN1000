class Student:
    def __init__(self, navn):
        self._navn = navn
        self._score = 0
        self._antQuiz = 0

    def leggTilQuizScore(self, score):
        self._score += score
        self._antQuiz += 1

    def gjennomsnitt(self):
        return self._score / self._antQuiz

    def skrivUt(self):
        print("Navn:", self._navn)
        print("Score:", self._score)
        print("Antall quizer:", self._antQuiz)

j = Student("Joakim")
k = Student("Kristin")
d = Student("Dag")

j.leggTilQuizScore(20)
k.leggTilQuizScore(10)
d.leggTilQuizScore(20)
j.leggTilQuizScore(5)
k.leggTilQuizScore(60)
d.leggTilQuizScore(50)
j.leggTilQuizScore(20)
k.leggTilQuizScore(10)
d.leggTilQuizScore(70)
j.leggTilQuizScore(60)
k.leggTilQuizScore(60)
d.leggTilQuizScore(15)

j.skrivUt()
k.skrivUt()
d.skrivUt()
