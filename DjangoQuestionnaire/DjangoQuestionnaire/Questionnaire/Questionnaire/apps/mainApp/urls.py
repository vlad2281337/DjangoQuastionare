from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='index'),

                  path('register/', views.regist, name='register'),
                  path('add_appointment/', views.newApointment, name='add_appointment'),
                  path('detail_appointment/<int:id>', views.detail_appointment, name='detail_appointment'),
                  path('delete_appointment/<int:id>', views.delete_appointment, name='delete_appointment'),
                  path('login/', views.loginPage, name='login'),
                  path('find/', views.find, name='find'),
                  path('logout/', views.logoutUser, name='logout'),
                  path('statistics/', views.statistics, name='statistics'),
                  path('medical/', views.medical, name='medical'),
                  path('about/', views.about, name='about'),

                  path('appointment_info/', views.appointment_info, name='appointment_info'),
                  path('lab_info/', views.lab_info, name='lab_info'),
                  path('rules/', views.rules, name='rules'),
                  path('advantages/', views.advantages, name='advantages'),
                  path('faq/', views.faq, name='faq'),
                  path('news/', views.news, name='news'),
                  path('contacts/', views.contacts, name='contacts'),

                  path('order/<str:name>', views.order, name='order'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
