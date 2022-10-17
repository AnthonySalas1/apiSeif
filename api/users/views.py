from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, UnidadSerializer
from .models import User, Unidad
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


@csrf_exempt
def unidad_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        unidades = Unidad.objects.all()
        serializer = UnidadSerializer(unidades, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UnidadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def unidad_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        unidad = Unidad.objects.get(pk=pk)
    except Unidad.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UnidadSerializer(unidad)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UnidadSerializer(unidad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        unidad.delete()
        return HttpResponse(status=204)
