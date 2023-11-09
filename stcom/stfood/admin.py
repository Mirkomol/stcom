from django.contrib import admin
from .models import Item




# class ModifyAdmin(admin.ModelAdmin):
#
#     def change_category_to_default(self,request,queryset):
#         queryset.update(item_price = 10)
#
#     # change_category_to_default.short_decription = "Default_Price"
#     #
#     search_fields = ('item_name','item_price')
#     # actions = ('change_category_to_default',)
#     # #fields = ('name',) # hide
#     # list_editable = ('item_price',)


admin.site.register(Item)