from django.urls import path
from rest_framework import routers

from .views import UserListView,UserDiseaseMediView,UserAllergyMediView,UserSignupView,UserMediViewSet

app_name = 'accounts'

router = routers.SimpleRouter()
router.register(r'medis',UserMediViewSet)

urlpatterns = [
    path('list/',UserListView.as_view()),
    path('disease-medi/',UserDiseaseMediView.as_view()),
    path('allergy-medi/',UserAllergyMediView.as_view()),
    path('sign-up/',UserSignupView.as_view()),
] 
urlpatterns += router.urls

