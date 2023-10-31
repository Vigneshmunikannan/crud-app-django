from django.urls import path
from .views import StudentDetails

urlpatterns = [
     path('add/',StudentDetails.as_view(),name="add-student-details"),
     path('get/',StudentDetails.as_view(),name="get-student"),
     path('get/<int:pk>/',StudentDetails.as_view(),name="get-single-student"),
     path('delete/<int:pk>/',StudentDetails.as_view(),name="delete-single-student"),
     path('update/<int:pk>/',StudentDetails.as_view(),name="update-single-student"),
]