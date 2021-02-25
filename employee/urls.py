from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^api/v1/employee/(?P<pk>[0-9]+)$',
            views.get_delete_update_employee.as_view(),
            name='get_delete_update_employee'
    ),
    path('api/v1/employees/',
         views.get_post_employees.as_view(),
         name='get_post_employees'
    )
]
