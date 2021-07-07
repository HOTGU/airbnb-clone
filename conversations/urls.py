from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path("go/<int:a_pk>/<int:b_pk>", views.go_conversation, name="go"),
    path("<int:pk>", views.ConversationsDetailView.as_view(), name="detail"),
]
