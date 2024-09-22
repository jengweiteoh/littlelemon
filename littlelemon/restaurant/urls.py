#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu/', views.menu, name='menu'),
    # path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('api-token-auth/', obtain_auth_token),
    path('book/', views.book, name="book"),
    # path('bookings/', views.BookingViewSet.as_view({'get': 'list'}), name="bookings"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('bookings/', views.bookings, name="bookings"),
]
