from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("person/add/", views.add_person, name="add_person"),
    path('', views.qr_scanner, name='qr_scanner'),
    path("api/scan_qr/", views.scan_qr, name="scan_qr"),
    path("attendance/", views.attendance_list, name="attendance_list"),
    path("paired/", views.paired_attendance_list, name="paired_attendance"),
    path('person/<int:pk>/edit/', views.edit_person, name='edit_person'),
    path('person/<int:pk>/delete/', views.delete_person, name='delete_person'),
    path('export/excel/', views.export_attendance_excel, name='export_attendance_day_excel'),
    path('export/pdf/', views.export_attendance_pdf, name='export_attendance_day_pdf'),
    path('api/attendance/', views.attendance_list_api, name='attendance_list_api'),
    path('api/paired-attendance/', views.paired_attendance_api, name='paired_attendance_api'),
    path('api/persons/', views.PersonProfileListCreateAPI.as_view(), name='person_api'),
    path('api/scan-qr/', views.scan_qr_api, name='scan_qr_api'),
    path("monthly-report/", views.monthly_person_report, name="monthly_report"),
    path("monthly-report/export/", views.export_monthly_report_excel, name="export_monthly_report_excel"),
    path("monthly-detailed-report/", views.monthly_person_detailed_report, name="monthly_detailed_report"),
     path("monthly-detailed-report/export-excel/", views.export_monthly_detailed_excel, name="export_monthly_detailed_excel"),
    path("monthly-detailed-report/export-pdf/", views.export_monthly_detailed_pdf, name="export_monthly_detailed_pdf"),
]



