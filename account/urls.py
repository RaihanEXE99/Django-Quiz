from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    # path('AAaccounts/',views.AAaccounts,name="AAaccounts"),
    path('analysis/',views.analysis,name="analysis"),
    path('adminPanel/',views.adminPanel,name="adminPanel"),
    path('adminDashboard/',views.adminDashboard,name="adminDashboard"),
    path('registration_view/', views.registration_view, name="registration_view"),
    path('login_view/', views.login_view, name="login_view"),
    path('logout_view/', views.logout_view, name="logout_view"),
    path('mysubmissions/', views.mysubmissions, name="mysubmissions"),
    path('password/',views.change_password, name='change_password'),
]
