from django.conf.urls import url, include
from rest_framework import routers
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='History Table API')

router = routers.DefaultRouter()
router.register(r'features', views.FeaturesViewSet)
router.register(r'histories', views.HistoriesViewSet)
router.register(r'users', views.UserViewSet)

app_name = 'api_v1'

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^attributes/$', views.AttributesApiView.as_view()),
    url(r'^login/', obtain_jwt_token),
    # url(
    #     regex=r'^$',
    #     view=views.,
    #     name=''
    # ),
]
