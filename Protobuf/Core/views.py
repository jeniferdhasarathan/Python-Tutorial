from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SampleModel
from .serializer import SampleModelSerializer
from .demo_pb2 import SampleData # Import generated protobuf class
from google.protobuf.message import DecodeError
from .demo_pb2 import SampleData
from .models import SampleModel
import base64

class SampleDataAPIView(APIView):
    def post(self, request):
        try:
            # Extract data from the request
            id=request.data.get('id')
            name = request.data.get('name')
            description = request.data.get('description')
            
            # Create and serialize protobuf data
            sample = SampleData(name=name, description=description,id=id)
            serialized_data = sample.SerializeToString()
            print(serialized_data,"*******************")
            
            # Encode serialized data to Base64 for storage
            # data_base64 = base64.b64encode(serialized_data).decode('utf-8')
            
            # Save to the database
            sample_data_model =SampleModel (
                id=sample.id,
                name=sample.name,
                description=sample.description,
                data=serialized_data
            )
            sample_data_model.save()

            return Response({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def get(self, request):
            try:
                id = request.query_params.get('id', None)
                # Retrieve the object from the database
                sample_data_model = SampleModel.objects.get(id=id)
                
                # Get the raw binary data from the database
                serialized_data = sample_data_model.data
                print(serialized_data,"**********************")
                
                # Deserialize protobuf data
                sample = SampleData()
                sample.ParseFromString(serialized_data)
                
                
                # Convert the protobuf object to a dictionary
                data_dict = {
                    'id': sample.id,
                    'name': sample.name,
                    'description': sample.description
                }

                return Response(data_dict, status=status.HTTP_200_OK)

            except SampleModel.DoesNotExist:
                return Response({'error': 'Sample data not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User, Project
from .serializer import UserSerializer, AdminSerializer, ProjectSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_admin=False)  # Only return regular users
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admins can manage users

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_admin=True)  # Only return admin users
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admins can manage other admins

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]  # Any authenticated user can manage their own projects

    def get_queryset(self):
        # Admins can see all projects, users can only see their own
        user = self.request.user
        if user.is_admin:
            return Project.objects.all()
        return Project.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        # Automatically assign the project to the current user
        serializer.save(owner=self.request.user)
