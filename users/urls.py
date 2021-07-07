from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("sighup/", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("update-password/", views.UpdatePassword.as_view(), name="password"),
    path("<int:pk>/", views.UserProfielView.as_view(), name="profile"),
    path("switch-hosting/", views.switch_hosting, name="switch-hosting"),
    path("switch-language/", views.switch_language, name="switch-language"),
]
