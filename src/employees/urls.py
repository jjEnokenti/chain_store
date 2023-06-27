from django.urls import path

from employees import views


urlpatterns = [
    path('signup/', views.EmployeeCreateView.as_view(), name='employee_signup'),
    path('login/', views.EmployeeLoginSerializer.as_view(), name='employee_login'),
    path('logout/', views.EmployeeLogoutView.as_view(), name='employee_logout'),
    path('profile/', views.EmployeeView.as_view(), name='employee_profile'),
]
