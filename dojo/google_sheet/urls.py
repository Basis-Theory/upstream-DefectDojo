from django.conf.urls import url

from dojo.google_sheet import views

urlpatterns = [
    #  google_sheet
    url(r'^drive_configuration$', views.configure_google_drive,
     name='configure_google_drive'),
    url(r'^export/to/sheet/(?P<tid>\d+)$', views.export_findings,
     name='export_findings'),
]
