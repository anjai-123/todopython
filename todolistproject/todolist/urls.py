from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:taskid>/',views.update,name='update'),
    path('cbvindex/',views.IndexListview.as_view(),name="cbvindex"),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_p(),name='cbvdetail'),
    path('cbvupdate/<int:id>/',views.UpdateView.as_p(),name="cbvupdate")
]
