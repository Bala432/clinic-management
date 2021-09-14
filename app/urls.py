from django.urls import path
from app import views

appname = "app"

urlpatterns = [

    path('',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name="logout"),
    path('create_record/',views.CreateRecordView,name="create_record"),
    path('patient_list/',views.PatientListView.as_view(),name="patient_list"),
    path('done/',views.done,name="done"),
    path('patient_list/<int:pk>/',views.PatientDetailView.as_view(),name="patient_detail"),
    path('patient_update/<int:pk>/', views.PatientUpdateView.as_view(), name="update_record"),
    path('email/<int:pk>/',views.PatientEmailView,name="email"),
    path("success/",views.success,name="success"),
    path('patient_name/',views.PatientNameListView,name="patient_name"),
    path('name_list/',views.index,name='name_list'),
    path('patient_name/<int:pk>/',views.PatientNameDetailView.as_view(),name="patient_name_detail"),
    path('problem_list/',views.home,name="problem_list"),
    path('patient_problem/',views.PatientProblemListView,name="patient_problem"),
    path('patient_problem/<int:pk>/',views.PatientProblemDetailView.as_view(),name="patient_problem_detail"),
    path('add_record/<int:pk>/',views.AddRecord,name="add_record"),
    path('add/',views.Add,name="add"),
    path('list_record/<int:pk>/',views.RecordsListView.as_view(),name="list_record"),
    path('list_record/<int:pk>/<int:pks>/',views.RecordsDetailView.as_view(),name="detail_record"),
    path('id_list/',views.complete,name="id_list"),
    path('patient_id/',views.PatientIDListView,name="patient_id"),
    path('patient_id/<int:pk>/',views.PatientIDDetailView.as_view(),name="patient_detail"),
    path('record_delete/<int:pk>/',views.PatientDeleteView.as_view(),name="record_delete"),
    path('record_person_delete/<int:pk>/',views.ConsultDeleteView.as_view(),name="record_person_delete"),

]