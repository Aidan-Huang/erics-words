from django.contrib import admin

# Register your models here.


from .models import WordTest, Word


class WordInline(admin.TabularInline):
    model = Word
    extra = 50


class WordAdmin(admin.ModelAdmin):
    readonly_fields = ('word', 'is_correct', 'correct_word')

    list_display = ('word', 'is_correct', 'correct_word')


class TestAdmin(admin.ModelAdmin):
    fields = ['count']

    inlines = [WordInline]

    list_display = ('test_date', 'count')


class MyWord(Word):
    class Meta(object):
        proxy = True



class MyWordAdmin(admin.ModelAdmin):


    list_display = ('word', 'is_correct')

admin.site.register(WordTest, TestAdmin)

admin.site.register(Word, WordAdmin)

admin.site.register(MyWord, MyWordAdmin)


