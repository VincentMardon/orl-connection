"""frantz_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from orl_connection.custom_admin import admin_site
from orl_connection.views import IndexView

from rest_framework_nested import routers

from authentication.views import AccountViewSet, LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^orl-rest-api/', include(router.urls)),
    url(r'^orl-rest-api/auth/login', LoginView.as_view(), name='login'),
    url(r'^orl-rest-api/auth/logout', LogoutView.as_view(), name='logout'),
    url(r'^orl-rest-api/docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', admin_site.urls),
    url('.*', IndexView.as_view(), name='index'),
]

urlpatterns += [
    url(r'^orl-rest-api/api-auth/', include('rest_framework.urls')),
]
