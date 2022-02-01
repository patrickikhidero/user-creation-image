from django.urls import path

from .views import BackEndAssessment, BackendAssessmentUpdate, BackendAssessmentGet


urlpatterns = [
    path('register-users', BackEndAssessment.as_view(), name='get-users'),
    path('update/<int:pk>', BackendAssessmentUpdate.as_view(), name='update-user'),
    path('weather-data', BackendAssessmentGet.as_view(), name="get-data" )
]
