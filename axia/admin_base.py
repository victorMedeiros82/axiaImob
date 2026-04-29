from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
        js = ('admin/js/custom.js',)

class CustoAdmin(BaseAdmin):
    fieldsets = (
        ('Informações principais', {
            'fields': (
                ('imovel', 'tipo'),
                ('valor_mensal',),
                ('data_inicio', 'data_fim'),
            ),
        }),
    )

