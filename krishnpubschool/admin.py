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
    list_display =["username","email","password",]

class adformAdmin(admin.ModelAdmin):
    list_filter =('firstname','mobile',)
    list_display =["firstname","lastname","fathername","mothername","types","mobile"]

admin.site.register(adform, adformAdmin)
admin.site.register(feedback, feedbackAdmin)
admin.site.register(ragister, ragisterAdmin)
