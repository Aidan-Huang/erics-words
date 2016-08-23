from django.contrib import admin

# Register your models here.


from .models import WordTest, WordRecord, Word


class WordRecordInline(admin.TabularInline):
    model = WordRecord
    extra = 10


class WordRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('word_record', 'is_correct', 'correct_word')

    list_display = ('word_record', 'is_correct', 'correct_word')


class WordTestAdmin(admin.ModelAdmin):
    fields = ['count']

    inlines = [WordRecordInline]

    list_display = ('test_date', 'count')


class WordAdmin(admin.ModelAdmin):
    model = Word

    list_display = ('id', 'word')


admin.site.register(Word, WordAdmin)
admin.site.register(WordTest, WordTestAdmin)
admin.site.register(WordRecord, WordRecordAdmin)

