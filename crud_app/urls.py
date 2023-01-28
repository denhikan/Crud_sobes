from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", views.create_view, name='staff_create'),
    path("", views.listview, name='listview'),
    path("<int:id>/", views.staff_detail_view, name='staff_read'),
    path("update/<int:id>/", views.update_view, name='staff_update'),
    path('delete/<int:id>/', views.delete_view, name='staff_delete'),
    path('register/', views.RegisterUser.as_view(), name='staff_register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
