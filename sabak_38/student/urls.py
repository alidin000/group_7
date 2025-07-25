from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import course, student, CourseViewSet, StudentListView, CourseListView, StudentCreateView, StudentCreatListView, CourseCreateView, CourseCreatListView, student_delete
urlpatterns = [
    path('student/', student, name="student"),
    path('student/delete/<str:name>', student_delete, name="student_delete"),
    path('courses/', course, name="course"),
    path('student/list/', StudentListView.as_view(), name="StudentListView"),
    # path('courses/list/', CourseListView.as_view(), name="CourseSerializer"),
    path('student/post/', StudentCreateView.as_view(), name="StudentCreateView"),
    # path('courses/post/', CourseCreateView.as_view(), name="CourseCreateView"),
    path('courses/post_list/', CourseCreatListView.as_view(), name="CourseCreatListView"),
    path('student/post_list/', StudentCreatListView.as_view(), name="StudentCreatListView"),
    path('student/post_list/', StudentCreatListView.as_view(), name="StudentCreatListView"),
]

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns += router.urls

#9892659ad3e9bfc7fc7edd2fe7c6012e773c19e1
# curl -X DELETE http://127.0.0.1:8000/student/delete/Temp2 -H 'Authorization: Token 9892659ad3e9bfc7fc7edd2fe7c6012e773c19e1'