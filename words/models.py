# -*- coding: utf-8 -*-
from django.db import models

'''
单词表中的一个单词


'''


class Word(models.Model):

    word = models.CharField("word", max_length=128)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'word'
        verbose_name_plural = 'words'

'''
单词测试

测试日期
测试数量
'''


class WordTest(models.Model):

    test_date = models.DateTimeField('testdate', auto_now_add=True)
    count = models.DecimalField('count', max_digits=3, decimal_places=0, default=50)

    class Meta:
        verbose_name = "WordTest"
        verbose_name_plural = "WordTests"
        ordering = ['test_date']

    def __str__(self):
        return "Word Test at: " + str(self.test_date)


'''
单词测试中一个默写的单词

单词测试
单词表中的记录
是否正确
订正单词
'''


class WordRecord(models.Model):

    wordTest = models.ForeignKey(WordTest, on_delete=models.CASCADE)

    word = models.ForeignKey(Word, blank=True, null=True)

    word_record = models.CharField("word", max_length=128)
    is_correct = models.BooleanField("iscorrect", default=True)
    correct_word = models.CharField("correct", max_length=128, blank=True)

    def __str__(self):
        return self.word_record + " tested at: " + str(self.wordTest.test_date)

    class Meta:
        verbose_name = "wordRecord"
        verbose_name_plural = "wordRecords"
