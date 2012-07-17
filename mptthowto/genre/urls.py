from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from genre.models import Genre

urlpatterns = patterns('',
    url(r'detail/(?P<pk>\d+)', DetailView.as_view(model=Genre), name="genre_detail",),
    url(r'update/(?P<pk>\d+)', UpdateView.as_view(model=Genre), name="genre_update",),
    url(r'delete/(?P<pk>\d+)', DeleteView.as_view(model=Genre, success_url='list'), name="genre_delete",),
    url(r'create', CreateView.as_view(model=Genre), name="genre_create",),
    url(r'list', ListView.as_view(model=Genre), name="genre_list",),
)
