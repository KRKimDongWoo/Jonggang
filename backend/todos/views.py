from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes, permission_classes

from todos.serializers import TodoSerializer
from todos.models import Todo, Course, ShortenName

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CourseView(generics.CreateAPIView):
    permission_classes = (permissions.isAdminUser,)
    parser_classes = (JSONParser, )

    def post(self, request, *args, **kwargs):
        course_list = []
        for course in request.data["data"]:
            shorten_name = ''.join([word[0] for word in course["course_name"].split(" ")])
            shorten_name_plain = ''.join([i for i in shorten_name if not i.isdigit()])
    
            course_altname = []

            for alt in [shorten_name, shorten_name_plain]:
                alt_obj = ShortenName.objects.filter(name=alt)
                if len(alt_obj) == 0:
                    t = ShortenName.objects.create(name=alt)
                    course_altname.append(t.id)
                else:
                    course_altname.append(alt_obj[0].id)

            # course['course_altname'] = course_altname
            t = Course(**course)
            t.save()
            t.course_altname.set(course_altname)
            print(t)


        return Response(status=HTTP_201_CREATED) 
"""
@api_view(['POST'])
@parser_classes((JSONParser, ))
@permission_classes((permissions.AllowAny, ))
def CourseView(request, format=None):
    for course in request.data["data"]:
        shorten_name = ''.join([word[0] for word in course["course_name"].split(" ")])
        shorten_name_plain = ''.join([i for i in shorten_name if not i.isdigit()])

        course_altname = []

        for alt in [shorten_name, shorten_name_plain]:
            alt_obj = ShortenName.objects.filter(name=alt)
            if len(alt_obj) == 0:
                t = ShortenName.objects.create(name=alt)
                course_altname.append(t.id)
            else:
                course_altname.append(alt_obj[0].id)

        course['course_altname'] = course_altname
        
    return 
"""
# Create your views here.
