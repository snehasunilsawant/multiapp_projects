from django.conf.urls import url,include

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^new$',views.register),
    url(r'^$',views.index),

]