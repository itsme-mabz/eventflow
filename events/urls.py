from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.EventListCreateView.as_view(), name='event-list-create'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/tickets/', views.TicketCreateView.as_view(), name='ticket-create'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('tickets/', views.TicketListView.as_view(), name='ticket-list'),
    path('auth/signup/', views.SignUpView.as_view(), name='signup'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('search/', views.EventSearchView.as_view(), name='event-search'), 

]
