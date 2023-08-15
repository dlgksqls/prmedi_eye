from django.urls import path


from .views import UserListView,UserDiseaseMediView,UserAllergyMediView,UserSignupView

app_name = 'accounts'

urlpatterns = [
    path('list/',UserListView.as_view()),
    path('signup/',UserSignupView.as_view()),
    path('disease-medi/',UserDiseaseMediView.as_view()),
    path('allergy-medi/',UserAllergyMediView.as_view()),
]

