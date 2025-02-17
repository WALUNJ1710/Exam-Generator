from django.db import models

class Question(models.Model):
    SUBJECT_CHOICES = [
        ('dsa', 'Data Structures and Algorithms'),
        ('os', 'Operating Systems'),
        ('dbms', 'Database Management Systems'),
        ('cn', 'Computer Networks'),
        ('ai', 'Artificial Intelligence'),
        ('ml', 'Machine Learning'),
        ('se', 'Software Engineering'),
        ('coa', 'Computer Organization and Architecture'),
        ('toc', 'Theory of Computation'),
        ('cloud', 'Cloud Computing'),
        ('cybersec', 'Cyber Security'),
        ('iot', 'Internet of Things'),
    ]

    qno = models.IntegerField(default=0, primary_key=True)
    qtext = models.CharField(max_length=500, default='null')
    answer = models.CharField(max_length=500, default='null')
    op1 = models.CharField(max_length=250, default='null')
    op2 = models.CharField(max_length=250, default='null')
    op3 = models.CharField(max_length=250, default='null')
    op4 = models.CharField(max_length=250, default='null')
    subject = models.CharField(
        max_length=50, choices=SUBJECT_CHOICES, default='dsa'
    )

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(
            self.qno, self.qtext, self.answer, self.op1, self.op2, self.op3, self.op4, self.subject
        )

    class Meta:
        db_table = "Question"


class Users(models.Model):
     username=models.CharField(max_length=40,default='',primary_key=True)
     password=models.CharField(max_length=40,default='')
     mobno = models.IntegerField(default=0)
     emailid=models.CharField(max_length=100,default='')

     def __str__(self):
          return "{},{},{},{}".format(self.username,self.password,self.mobno,self.emailid)

     class Meta:
          db_table="users"

class Result(models.Model):

     username=models.CharField(max_length=40,default='',primary_key=True)
     subject=models.CharField(max_length=40,default='null')
     score = models.IntegerField()

     def __str__(self):
          return "{},{},{}".format(self.username,self.subject,self.score)
     
     class Meta:
          db_table="result"

class Admin(models.Model):
     username=models.CharField(max_length=40,default='',primary_key=True)
     password=models.CharField(max_length=40,default='')
     def __str__(self):
          return "{},{},{},{}".format(self.username,self.password)

     class Meta:
          db_table="admin"
