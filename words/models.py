from django.db import models


class WordTest(models.Model):
    test_date = models.DateTimeField('testdate', auto_now_add=True)
    count = models.DecimalField('count', max_digits=3, decimal_places=0, default=50)

    class Meta(object):
        verbose_name = "Test"
        verbose_name_plural = "Tests"
        ordering = ['test_date']

    def __str__(self):
        return "test at: " + str(self.test_date)


class Word(models.Model):

    test = models.ForeignKey(WordTest)

    word = models.CharField("word", max_length=128)
    is_correct = models.BooleanField("iscorrect", default=True)
    correct_word = models.CharField("correct", max_length=128, blank=True)

    def __str__(self):
        return self.word

    class Meta(object):
        verbose_name = 'word'
        verbose_name_plural = 'words'
