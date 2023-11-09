from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.site_header = "StCom_Admin"
admin.site.site_title = "Administration"
admin.site.index_title = "Administration_Staff"


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status','created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)



