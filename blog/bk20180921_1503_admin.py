from django.contrib import admin

### from adminsortable.admin import SortableAdmin  # HBAnaga20180921 1414 足した


from .models import Post

### admin.site.register(Post, SortableAdmin)  # HBAnaga2018091 1415 足した


admin.site.register(Post)


# HBA naga add start

# from .models import Question
# from .models import Choice


#class ChoiceInline(admin.StackedInline):
#   model = Choice
#    extra = 3

#class QuestionAdmin(admin.ModelAdmin):
#    inlines = [ChoiceInline]
#    list_display = ('pk', 'question_text', 'pub_date', 'was_published_recently')
#   list_filter = ['pub_date']
#    search_fields = ['question_text']

# HBA naga add end


