from rest_framework import routers
from mainapp.views import *


router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'type', TypeViewSet)
router.register(r'product', ProductViewSet)

router.register(r'message', MessagesViewSet)
