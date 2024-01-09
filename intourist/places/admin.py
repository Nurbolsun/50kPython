from django.contrib import admin
from .models import Place, Feedback
# Register your models here.

admin.site.register(Place)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user','place', 'text_back']
    list_editable = ['place']
    search_fields = ['text_back']

admin.site.register(Feedback, FeedbackAdmin)
