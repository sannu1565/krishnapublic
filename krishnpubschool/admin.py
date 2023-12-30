from django.contrib import admin
from krishnpubschool.models import feedback
from krishnpubschool.models import adform
from krishnpubschool.models import ragister
# # Register your models here.
# class enquiryForm(admin.ModelAdmin):
#     list_display = ('firstname','lastname','mobile_no','type','comment',)
class feedbackAdmin(admin.ModelAdmin):

    list_display =["firstname","lastname","mobile_no","type","textcomment"]
    list_filter = ('firstname','lastname','type')
class ragisterAdmin(admin.ModelAdmin):
    list_filter =('email',)
    
class adformAdmin(admin.ModelAdmin):
    list_filter =('firstname','mobile',)

admin.site.register(adform, adformAdmin)
admin.site.register(feedback, feedbackAdmin)
admin.site.register(ragister, ragisterAdmin)
