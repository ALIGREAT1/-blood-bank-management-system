
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Donors
    path('donors/', views.donor_list, name='donor_list'),
    path('donors/add/', views.add_donor, name='add_donor'),
    path('donors/<int:donor_id>/edit/', views.update_donor, name='update_donor'),
    path('donors/<int:donor_id>/delete/', views.delete_donor, name='delete_donor'),

    # Recipients
    path('recipients/', views.recipient_list, name='recipient_list'),
    path('recipients/add/', views.add_recipient, name='add_recipient'),
    path('recipients/<int:recipient_id>/edit/', views.update_recipient, name='update_recipient'),
    path('recipients/<int:recipient_id>/delete/', views.delete_recipient, name='delete_recipient'),

    # Hospitals
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('hospitals/add/', views.add_hospital, name='add_hospital'),
    path('hospitals/<int:hospital_id>/edit/', views.update_hospital, name='update_hospital'),
    path('hospitals/<int:hospital_id>/delete/', views.delete_hospital, name='delete_hospital'),
    

    # DONATION MANAGEMENT
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/add/', views.add_donation, name='add_donation'),
    path('donations/<int:donation_id>/edit/', views.update_donation, name='update_donation'),
    path('donations/<int:donation_id>/delete/', views.delete_donation, name='delete_donation'),

    # BLOOD INVENTORY MANAGEMENT
    path('blood-units/', views.blood_unit_list, name='blood_unit_list'),
    path('blood-units/add/', views.add_blood_unit, name='add_blood_unit'),
    path('blood-units/<int:bloodunit_id>/edit/', views.update_blood_unit, name='update_blood_unit'),
    path('blood-units/<int:bloodunit_id>/delete/', views.delete_blood_unit, name='delete_blood_unit'), 

    # BLOOD TESTING MANAGEMENT
    path('blood-tests/', views.blood_test_list, name='blood_test_list'),
    path('blood-tests/add/', views.add_blood_test, name='add_blood_test'),
    path('blood-tests/<int:test_id>/edit/', views.update_blood_test, name='update_blood_test'),
    path('blood-tests/<int:test_id>/delete/', views.delete_blood_test, name='delete_blood_test'),

    # BLOOD REQUEST MANAGEMENT
    path('blood-requests/', views.blood_request_list, name='blood_request_list'),
    path('blood-requests/add/', views.add_blood_request, name='add_blood_request'),
    path('blood-requests/<int:request_id>/edit/', views.update_blood_request, name='update_blood_request'),
    path('blood-requests/<int:request_id>/delete/', views.delete_blood_request, name='delete_blood_request'),


    # COLLECTIONSITE MANAGEMENT
    path('collection-sites/', views.collection_site_list, name='collection_site_list'),
    path('collection-sites/add/', views.add_collection_site, name='add_collection_site'),
    path('collection-sites/<int:site_id>/edit/', views.update_collection_site, name='update_collection_site'),
    path('collection-sites/<int:site_id>/delete/', views.delete_collection_site, name='delete_collection_site'),


    # Authentication
    path('login/', auth_views.LoginView.as_view(
        template_name='bloodbank/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
