from django.urls import path
from restaurant import views

urlpatterns = [
    path("menu/", views.MenuItemsView.as_view(), name="menu_list"),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view(), name="menu_detail"),
]
