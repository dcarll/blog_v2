from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/new/', views.BLogCreateView.as_view(), name='post_new'), # essa linha precisa vir antes do slug
    path('post/<slug:slug>/', views.BLogDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    

]