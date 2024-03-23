from django.contrib import admin
from django.urls import path
from employee_app import views
urlpatterns = [
    path('', views.list_of_employees, name="show"),
    path('save-employee', views.save_employee, name='save_employee'),
    path('delete-employee', views.delete_employee, name='delete_employee'),
    path('present-employee', views.present_employee, name='present_employee'),
    path('today-attendance', views.todays_attendance, name='today-attendance'),
    path('all-attendance-employee', views.all_attendance_employee, name='all-attendance-employee'),
    path('edit-employee', views.edit_employee, name='edit-employee'),
]