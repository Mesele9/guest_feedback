from django.contrib import admin
from django.urls import path
from comments.views import feedback_view, success_view, feedback_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', feedback_view, name='feedback'),
    path('success/', success_view, name='success'),
    path('feedback-dashboard/', feedback_dashboard, name='feedback_dashboard'),

]
