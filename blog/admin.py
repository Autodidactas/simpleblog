from django.contrib import admin
from models import *

class ArchivosAdminInline(admin.StackedInline):
	model = Archivos
	extra = 1

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("titulo",)}
	date_hierarchy = "fecha"
	fieldsets = (
			(None, {
				'fields': (('fecha','titulo','slug'),'contenido',
					('autor','categoria','tag'))
				}),
		)
	list_display = ['fecha','titulo','autor']
	list_filter = ['categoria','autor']
	search_fields = ('titulo','contenido',)
	inlines = [ArchivosAdminInline]

	class Media:
		js = ('js/tiny_mce/tiny_mce.js',
			  'js/basic_config.js',)

admin.site.register(Categoria)
admin.site.register(Posts, PostAdmin)