from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.timezone import datetime


def get_pic_location(instance, filename):
    date = datetime.now()
    date_str = date.strftime('%Y%m%d%H%M%S')
    pic_path = 'post_images/{0}/{1}_{2}'.format(instance.category.id, date_str, filename)
    return pic_path


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return self.post_set.count()

    class Meta:
        verbose_name = verbose_name_plural = 'Tags'


class Category(models.Model):
    name = models.CharField('分类名称', max_length=120, unique=True)
    timestamp = models.DateTimeField('创建时间', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('更新时间', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:list_of_category', kwargs={'cate_id': self.id, 'cate_name': self.name})

    class Meta:
        verbose_name_plural = verbose_name = '分类'


class Post(models.Model):
    DRAFT = 0
    PUBLISHED = 1
    POST_STATUS = (
        (DRAFT, 'draft'),
        (PUBLISHED, 'published')
    )

    category = models.ForeignKey('Category', verbose_name='分类', blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField('标题', max_length=120, db_index=True)
    slug = models.SlugField('友好的链接', max_length=100, allow_unicode=True)
    summary = models.CharField('摘要', max_length=400, null=True, blank=True)
    pic = models.ImageField('图片', blank=True, null=True, upload_to=get_pic_location)
    content = models.TextField('内容', )

    click = models.PositiveIntegerField('点击量', default=0, editable=False)
    commend = models.PositiveIntegerField('赞', default=0, editable=False)
    is_public = models.BooleanField('公开', default=True)
    is_top = models.BooleanField('置顶', default=False)

    updated = models.DateTimeField('更新时间', auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField('创建时间', auto_now=False, auto_now_add=True)
    publish_time = models.DateField('发表时间', null=True, blank=True)

    status = models.IntegerField('状态', default=PUBLISHED, choices=POST_STATUS)
    tag = models.ManyToManyField(Tag, verbose_name='标签', through='PTRelations')
    author = models.ForeignKey(User, verbose_name='作者', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('post:detail', args=(self.pk, self.slug,))

    class Meta:
        ordering = ['-timestamp', ]
        verbose_name = verbose_name_plural = '文章'


class PTRelations(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.title + ' - ' + self.tag.name
