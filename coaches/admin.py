from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Coach Email', {'fields':['email_address']}),
    ('School', {'fields':['school_name']}),
    ('Sport',{'fields':['sport']}),
    ('Total Kredit', {'fields':['kredit']}),
  ]

  list_display = ('school_name','email_address','sport')

  list_filter = ['sport']

  search_fields = ['school_name']


admin.site.register(Coach, CoachAdmin)
