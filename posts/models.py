from django.db import models
from django.core.urlresolvers import reverse
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
    name = models.CharField(max_length=120, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:list_of_category', kwargs={'cate_id': self.id})

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    DRAFT = 0
    PUBLISHED = 1
    POST_STATUS = (
        (DRAFT, 'draft'),
        (PUBLISHED, 'published')
    )

    category = models.ForeignKey('Category',blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, allow_unicode=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    pic = models.ImageField(blank=True, null=True, upload_to=get_pic_location)
    click = models.PositiveIntegerField(default=0)
    commend = models.PositiveIntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.IntegerField(default=PUBLISHED, choices=POST_STATUS)
    tag = models.ManyToManyField(Tag, through='PTRelations')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('post:detail', args=(self.pk, self.slug,))

    class Meta:
        ordering = ['-timestamp', ]


class PTRelations(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.title + ' - ' + self.tag.name
