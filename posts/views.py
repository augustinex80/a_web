from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from .models import Post, Tag


def login_req(view):
    view.dispatch = method_decorator(login_required)(view.dispatch)
    return view


def get_pages_list(current_page, num_pages, sep_str='...'):
    if not current_page:
        current_page = 1
    else:
        current_page = int(current_page)
    pages = []
    for i in range(-5, 6):
        if 0 < i + current_page <= num_pages:
            pages.append(current_page + i)

    if 1 not in pages and 2 not in pages:
        pages.insert(0, sep_str)
        pages.insert(0, 1)
    elif 1 not in pages:
        pages.insert(0, 1)

    if num_pages not in pages and num_pages - 1 not in pages:
        pages.append(sep_str)
        pages.append(num_pages)
    elif num_pages not in pages:
        pages.append(num_pages)

    return pages


# @method_decorator(login_required, name='dispatch')
# @login_req
# @method_decorator(cache_page(60 * 1), name='dispatch')
class PostList(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'

    paginate_by = settings.ITEMS_PER_PAGE
    page_kwarg = settings.PAGE_KWARG

    def get_queryset(self):
        # category filter, query filter
        cate_id = self.kwargs.get('cate_id')
        q = self.request.GET.get('q')

        # tag filter
        tid = self.kwargs.get('tid', None)
        tname = self.kwargs.get('tname', None)
        if tid and tname:
            tag = get_object_or_404(Tag, pk=tid, name=tname)
            return tag.post_set.all()
        queryset = Post.objects.all()

        # admin can read every post.
        if not self.request.user.is_staff:
            queryset = queryset.filter(status=1, is_public=True)

        if cate_id:
            queryset = queryset.filter(category_id=cate_id)
        if q:
            queryset = queryset.filter(Q(title__icontains=q)|
                                       Q(summary__icontains=q)|
                                       Q(content__icontains=q)|
                                       Q(category__name__icontains=q)
                                       ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        #
        current_page = self.request.GET.get('p', 0)
        num_pages = context['paginator'].num_pages
        context['pages'] = get_pages_list(current_page, num_pages)
        context['blog'] = 1
        context['top_post'] = self.get_queryset().filter(is_top=True)
        return context


class PostDetail(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('slug', None) != self.get_object().slug:
            raise Http404("Page does not exist!")
        if not self.get_object().is_public and not self.request.user.is_staff:
            raise Http404("Deny to read this post!")
        return super(self.__class__, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        pid = self.kwargs.get('pid', None)
        return get_object_or_404(Post, id=pid)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['blog'] = 1

        return context


