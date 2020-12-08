from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunc, BlogList, BlogDetail, BlogCreate, BlogUpdate

urlpatterns = [
    path("helloworldapp/", helloworldfunc),
    path("list/", BlogList.as_view(), name="list"),
    path("detail/<int:pk>", BlogDetail.as_view(), name="detail"),
    path("create/", BlogCreate.as_view(), name="create"),
    path("update/<int:pk>", BlogUpdate.as_view(), name="update"),

    path("list/<str:category>", helloworldfunc)
]