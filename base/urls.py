from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index_page,name="index_page"),
    
    path('department/',views.dept_data,name="dept"),
    path('update/<str:pk>',views.update_pg,name="update_page"),
    path('delete/<str:pk>',views.delete_pg,name="delete_page"),
    path('create_dept/',views.create_dept,name="create_dept"),

    path('post_det',views.posi_data,name="position_data"),
    path('create_post/',views.create_posi,name="create_posi"),
    path('update_position/<str:pk>',views.update_posi,name="update_posi_page"),
    path('delete_position/<str:pk>',views.delete_posi,name="delete_posi_page"),

    path('emp_det',views.emp_data,name="emp_data"),
    path('create_emp/',views.create_emp,name="create_emp"),
    path('update_employee/<str:pk>',views.update_emp,name="update_emp_page"),
    path('delete_employee/<str:pk>',views.delete_emp,name="delete_emp_page"),

    path('dashboard/',views.dashboard,name="dash_board")


]
