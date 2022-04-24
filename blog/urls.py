from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',  views.homepage, name=''),
    path('postBlog', views.postBlog, name='postBlog'),
    path('allDoctors', views.alldocs, name='allDoctors'),
    path('appointment', views.appointment, name='appointment'),
    path('docAppointments', views.docAppointments, name='docAppointments')
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)