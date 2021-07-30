class Student(object):
    def __init__(self,name,score,age):
        self.name = name
        self.score = score
        self.age = age
    def get_gtade(self):
        if self.score >100 or self.score < 0:
            raise ValueError
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >=80 and self.score <= 100:
            return 'A'
        return 'C'
    def get_age(self):
        if self.age < 0 or self.age > 100:
            raise ValueError
        if self.age <18 and self.age > 0:
            return '未成年'
        if self.age >=18 and self.age < 25:
            return '中学生'
        return '社会人'
