from django.urls import path, include
from restaurant import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tables", views.BookingViewSet)

urlpatterns = [
    path("menu/", views.MenuItemsView.as_view(), name="menu_list"),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view(), name="menu_detail"),
    path("booking/", include(router.urls))
]
