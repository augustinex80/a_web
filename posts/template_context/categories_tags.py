from ..models import Category, Tag


def get_categories_tags(request):
    tags = Tag.objects.all()
    new_tags = []
    for t in tags:
        new_tags.append({
            'pk': t.pk,
            'name': t.name,
            'posts_count': t.post_set.count()
                         })

    return {'categories': Category.objects.all(),
            'tags': sorted(new_tags, key=lambda d: d['posts_count'], reverse=True),
            }
