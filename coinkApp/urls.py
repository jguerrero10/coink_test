from django.urls import path

from coinkApp.views import *

urlpatterns = [
    path('', list_user_basic, name='list-user-basic'),
    path('user-basic/create/', create_user_basic, name='create-user-basic'),
    path('user-basic/update/<int:id>', update_user_basic, name='update-user-basic'),
    path('user-basic/delete/<int:id>', delete_user_basic, name='delete-user-basic')
]
