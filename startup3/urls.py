from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('customer',customer, name='customer'),
    path('form-success/<str:id>',form_success_view, name='form-success'),
    path('login',login_page,name='login_page'),
    path('user/<str:id>',user,name='user_home'),
    
    path('save-personal', save_personal, name='save-personal'),
    path('family',family, name='family'),
    path('bankacc',bankacc,name='bankacc'),
    path('credit',credit,name='credit'),
    path('debit',debit,name='debit'),
    
    path('add-personal-loan',add_personal_loan,name='add-personal-loan'),
    path('add-gold-loan',add_gold_loan,name='add-gold-loan'),
    path('add-house-loan',add_house_loan,name='add-house-loan'),
    
    path('edit-personal-loan/<int:pk>/', edit_personal_loan, name='edit-personal-loan'),
    path('delete-personal-loan/<int:pk>/', delete_personal_loan, name='delete-personal-loan'),
    
    path('add-vehicle-loan/', add_vehicle_loan, name='add-vehicle-loan'),
    path('edit-vehicle-loan/<int:pk>/', edit_vehicle_loan, name='edit-vehicle-loan'),
    path('delete-vehicle-loan/<int:pk>/', delete_vehicle_loan, name='delete-vehicle-loan'),
    
    path('edit-gold-loan/<int:pk>/', edit_gold_loan, name='edit-gold-loan'),
    path('delete-gold-loan/<int:pk>/', delete_gold_loan, name='delete-gold-loan'),
    
    path('edit-house-loan/<int:pk>/', edit_house_loan, name='edit-house-loan'),
    path('delete-house-loan/<int:pk>/', delete_house_loan, name='delete-house-loan'),
    
    path('properties',property, name='properties'),
    
    path('veh-insurance', veh_insurance, name='add-veh-insurance'),
    
    path('stock-investment',stock_investment, name='stock-investment'),
    path('edit-stock-invest/<int:pk>/', edit_stock_invest, name='edit-stock-invest'),
    path('del-stock-invest/<int:pk>/', del_stock_invest, name='del-stock-invest'),
    
    path('fund-investment',funds_investment, name='fund-investment'),
    path('edit-fund-invest/<int:pk>/', edit_stock_invest, name='edit-fund-invest'),
    path('del-fund-invest/<int:pk>/', del_stock_invest, name='del-fund-invest'),
    
    path('schemes',schemes,name='schemes'),
    path('card',card,name='card'),
    
    path('edit-family/<int:member_id>/', edit_family, name='edit-family'),
    path('delete-family/<int:member_id>/', delete_family, name='delete-family'),
    
    path('edit-bank/<int:member_id>/', edit_bank, name='edit-bank'),
    path('delete-bank/<int:member_id>/', delete_bank, name='delete-bank'),
    
    path('edit-credit/<int:member_id>/', edit_credit, name='edit-credit'),
    path('delete-credit/<int:member_id>/', delete_credit, name='delete-credit'),
    
    path('edit-debit/<int:member_id>/', edit_debit, name='edit-debit'),
    path('delete-debit/<int:member_id>/', delete_debit, name='delete-debit'),
    
    path('edit-veh-insurance/<int:member_id>/', edit_veh_insurance, name='edit-veh-insurance'),
    path('delete-veh-insurance/<int:member_id>/', delete_veh_insurance, name='delete-veh-insurance'),
    
    path('edit-property/<int:member_id>/', edit_property, name='edit-property'),
    path('delete-property/<int:member_id>/', delete_property, name='delete-property'),
    
    path('edit-schemes/<int:member_id>/', edit_schemes, name='edit-schemes'),
    path('delete-schemes/<int:member_id>/', delete_schemes, name='delete-schemes'),
    
    path('edit-card/<int:member_id>/', edit_card, name='edit-card'),
    path('delete-card/<int:member_id>/', delete_card, name='delete-card'),
    
    path('pricing',pricing,name='pricing'),
    
    path('doc',documents,name='doc'),
    
    path('add-life-insurance/', add_life_insurance, name='add-life-insurance'),
    path('edit-life-insurance/<int:pk>/', edit_life_insurance, name='edit-life-insurance'),
    path('delete-life-insurance/<int:pk>/', delete_life_insurance, name='delete-life-insurance'),
    
    path('add-term-insurance/', add_term_insurance, name='add-term-insurance'),
    path('edit-term-insurance/<int:pk>/', edit_term_insurance, name='edit-term-insurance'),
    path('delete-term-insurance/<int:pk>/', delete_term_insurance, name='delete-term-insurance'),
    
    path('add-health-insurance/', add_health_insurance, name='add-health-insurance'),
    path('edit-health-insurance/<int:pk>/', edit_health_insurance, name='edit-health-insurance'),
    path('delete-health-insurance/<int:pk>/', delete_health_insurance, name='delete-health-insurance'),
    
    path('pf/add/', add_pf, name='add-pf'),  # Add a new PF record
    path('pf/edit/<int:id>/', edit_pf, name='edit-pf'),  # Edit an existing PF record
    path('pf/delete/<int:id>/', delete_pf, name='delete-pf'),  # Delete a PF record
]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
