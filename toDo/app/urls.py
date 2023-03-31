from rest_framework import routers
from app.views import ToDoViewSet

router = routers.DefaultRouter()
router.register ('todo', ToDoViewSet, basename='ToDo')

urlpatterns = router.urls