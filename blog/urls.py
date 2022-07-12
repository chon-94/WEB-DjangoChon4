from django.urls import path
from .views import blogView,PostListView,PostDetailView,ScriptsListView

app_name="blog"

urlpatterns = [
    path('', blogView.as_view(), name="home"),

    path('post/', PostListView.as_view(), name='list'),
    path('post/<slug>/', PostDetailView.as_view(), name='detail'),

    path('scripts/', ScriptsListView.as_view(),name='lista'),
]