from django.urls import path
from .views import CustomUserListCreateAPIView, CustomUserRetrieveUpdateDestroyAPIView, \
                   ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView, \
                   ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView, \
                   ProjectAssignmentListCreateAPIView, ProjectAssignmentRetrieveUpdateDestroyAPIView, UserRegistrationAPIView, UserProjectsListAPIView, ClientUpdateAPIView

urlpatterns = [
    path('users/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('users/', CustomUserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
    path('assignments/', ProjectAssignmentListCreateAPIView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', ProjectAssignmentRetrieveUpdateDestroyAPIView.as_view(), name='assignment-detail'),
    path('user/projects/', UserProjectsListAPIView.as_view(), name='user-projects'),
    path('clients/update/', ClientUpdateAPIView.as_view(), name='client-update'),
    
]

