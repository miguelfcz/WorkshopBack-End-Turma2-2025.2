#Gera todas as Restful URLs
from rest_framework import routers
from apiRest.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register(r'enderecos', EnderecoViewSet, basename='enderecos')

urlpatterns = router.urls