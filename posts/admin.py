from django.contrib import admin
from .models import Post, Category, Tag, PTRelations


class PTRelationInline(admin.TabularInline):
    model = PTRelations
    extra = 1


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'timestamp', 'updated']
    prepopulated_fields = {'slug': ('title', )}
    inlines = (PTRelationInline, )

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)
