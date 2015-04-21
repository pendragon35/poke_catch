from django.contrib import admin

# Register your models here.
from .models import Rates

class RatesAdmin(admin.ModelAdmin):
  list_display = ('poke_num','poke_name','dp_rate','bw_rate','xy_rate')
  search_fields = ['poke_name']

admin.site.register(Rates, RatesAdmin)