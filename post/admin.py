from django.contrib import admin

from .models import post

class PostAdmin(admin.ModelAdmin):
    list_display = ['baslik','yayin','slug']
    list_display_links = ['yayin']
    list_filter = ['yayin']
    search_fields = ['baslik','metin']
    list_editable = ['baslik']
    class Meta:
        model=post

admin.site.register(post,PostAdmin)
