from django.contrib import admin
from .models import Post, Category, Tag, PTRelations


class PTRelationInline(admin.TabularInline):
    model = PTRelations
    extra = 1
# TODO: 在admin显示得更人性化, 一个输入框, 逗号分格, 若不存在则增加


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'timestamp', 'updated']
    prepopulated_fields = {'slug': ('title', )}
    inlines = (PTRelationInline, )

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)
