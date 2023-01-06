# from django.http import HttpResponse
# from django.views import View
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import TaskSerializer
from .models import Task
from django.contrib.auth.models import User

# ////////////////////////////////login /register
# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# register
@api_view(['POST'])
def  register(req):
    username=req.data["username"]
    password=req.data["password"]
    # create a new user (encrypt password)
    try:
        User.objects.create_user(username=username,password=password)
    except:
        return Response("error")    
    return Response(f"{username} registered")
 
        



# ///////////////////////////end login

# //////////test method
@api_view(['GET'])
def test(req):
    return Response("hello")

# /////////// Tasks table (CRUD)
@api_view(['GET','POST','DELETE','PUT','PATCH'])
@permission_classes([IsAuthenticated])
def tasks(req,id=-1):
    if req.method =='GET':
        user= req.user
        if id > -1:
            try:
                temp_task=user.task_set.get(id=id)
                return Response (TaskSerializer(temp_task,many=False).data)
            except Task.DoesNotExist:
                return Response ("not found") 
        
        all_tasks=TaskSerializer(user.task_set.all(),many=True).data
        return Response ( all_tasks)
        
    if req.method =='POST':
        print(type( req.user))
        Task.objects.create(title =req.data["title"],description=req.data["description"],completed= req.data["completed"],user=req.user)
        return Response ("post...")

    if req.method =='DELETE':
        user= req.user
        try:
            temp_task=user.task_set.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")    
        
        temp_task.delete()
        return Response ("del...")
    if req.method =='PUT':
        user= req.user
        try:
            temp_task=user.task_set.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")
        
        old_task = user.task_set.get(id=id)
        old_task.title =req.data["title"]
        old_task.completed =req.data["completed"]
        old_task.description=req.data["description"]
        old_task.save()
        return Response("res")

   

    #     user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # title = models.CharField(max_length=50)
    # description = models.CharField(max_length=100)
    # completed = models.BooleanField(default=False)
        # req.data["user_id"] = "eyal" # req.user
        
        # tsk_serializer = TaskSerializer(data=req.data)



        # if tsk_serializer.is_valid():
        #     tsk_serializer.save()