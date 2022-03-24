from django.contrib import admin
from .models        import Receita

# Register your models here.
class ListandoReceitas(admin.ModelAdmin):
  list_display = ('id', 'nome_receita', 'publicada')
  list_display_links = ('id', 'nome_receita')

  list_editable = ('publicada',)
  search_fields = ('nome_receita',)
  list_filter = ('categoria',)
  list_per_page = 2

admin.site.register(Receita, ListandoReceitas)