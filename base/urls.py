from django.urls import path
from .views import tasks 
from . import views 

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.register ),
    path('tasks/',tasks ),
    path('test/',views.test ),
    path('tasks/<int:id>',tasks),
]
