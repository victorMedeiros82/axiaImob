# from django.contrib.admin import AdminSite
# from django.db.models import Sum
# from imoveis.models import Imovel


# class MyAdminSite(AdminSite):
#     index_template = "admin/index.html"

#     def each_context(self, request):
#         context = super().each_context(request)
#         context["total_imoveis"] = Imovel.objects.count()
#         return context
