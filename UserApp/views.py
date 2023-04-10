from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from django.contrib.auth import login, logout
from UserApp.models import UserFollowing, User
from UserApp.serializers import UserSerializer, UserFollowingSerializer, RegistrationSerializer, UserDetailSerializer


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        data = dict()
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = 'successfully registered new user.'
                data['email'] = user.email
                data['username'] = user.username
                token = Token.objects.get(user=user).key
                data['token'] = token
            else:
                data = serializer.errors
            return Response(data)
        except Exception as e:
            print(e)
            return Response({"errors":"Can't process the request. Please check logs"}, status=status.HTTP_400_BAD_REQUEST)

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get','put','delete']

    @action(detail=True, methods=['PUT'])
    def update_user(self, request,pk=None):
        user = User.objects.get(id=pk)

        if 'username' in request.data:
            setattr(user, "username", request.data['username'])
            user.save()
        serializer = UserSerializer(user,many=False)
        return Response(serializer.data)


    @action(detail=True, methods=['GET'])
    def no_of_follow(self, request,pk=None,format=None):
        user = User.objects.get(id=pk)
        return Response({"no_followers":len(UserSerializer(user).data['followers']),"no_following": len(UserSerializer(user).data['following'])})

class UserDetailViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    http_method_names = ['get']

class UserFollowingViewSet(viewsets.ModelViewSet):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer
    http_method_names = ['get']


class UserFollow(APIView):
    # return user if user exist
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise ValueError

    def get(self, request, pk, format=None):
        try:
            user = self.get_object(pk)
            # user = self.get_object(pk=1)
        except Exception as e:
            print(e)
            return Response({'message': 'User does not exists '})
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        # user = User.objects.get(pk=request.data['user'])
        user = request.user
        try:
            follow = self.get_object(pk)
        except Exception as e:
            print(e)
            return Response({'message': 'User does not exists '}, status=status.HTTP_404_NOT_FOUND)
        try:
            if user != follow:
                UserFollowing.objects.create(user_id=user, following_user_id=follow)
            else:
                return Response({"message": "You can't follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": f"You already follow {follow}"}, STATUS=status.HTTP_406_NOT_ACCEPTABLE)

        return Response({'message': f'You follow {follow}'})

    # unfollow users.
    def delete(self, request, pk, format=None):
        # user = User.objects.get(pk=request.data['user'])
        user = request.user
        try:
            follow = self.get_object(pk)
        except  Exception as e:
            print(e)
            return Response({'message': 'User does not exists '}, status=status.HTTP_404_NOT_FOUND)
        try:
            connection = UserFollowing.objects.filter(user_id=user, following_user_id=follow).first()
            connection.delete()
        except  Exception as e:
            print(e)
            return Response({'message': f"You don't follow {follow}"})
        return Response({'message': f'You unfollowed {follow}'})

class CustomAuthToken(ObtainAuthToken):

    def get(self, request, *args, **kwargs):

        return Response({"errors": "only post method allowed with username, password  and Token for authentication"})

    def post(self, request, *args, **kwargs):
        if User.objects.filter(username=request.data['username']).exists():
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            if serializer.is_valid():
             
                user = serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                login(user)
                user_data = UserSerializer(user).data
                # TODO: redirect to login next
                return Response({
                    'token': token.key,
                    'user': user_data
                })
            return Response({"errors": "Please check your Password"},
                            status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"errors": "User does not exixts with this email address"},
                            status=status.HTTP_404_NOT_FOUND)
