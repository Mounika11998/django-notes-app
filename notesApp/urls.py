from django.urls import path
from . import views 
urlpatterns=[
    path('note_list/',views.note_list,name='note_list'),
    path('add_note/', views.add_note, name='add_note'),
    path('edit_note/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete_note/<int:pk>/', views.delete_note, name='delete_note'),
]