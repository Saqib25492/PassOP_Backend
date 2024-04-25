from django.urls import path, include
from Manager import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("create", views.Create.as_view(), name="create"),
    path("read/<int:user>", views.Read.as_view(), name="read"),
    path("readone/<int:pk>", views.ReadOne.as_view(), name="readone"),
    path("update/<int:pk>", views.Update.as_view(), name="update"),
    path("delete/<int:pk>", views.Delete.as_view(), name="delete"),
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path("token/", views.MyTokenObtain.as_view(), name="token"),
    path("toekn/refrest/", TokenRefreshView.as_view(), name="refresh_token"),
]
