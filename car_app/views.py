import json
import pathlib

from django.http import FileResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from car_app.serializers import *
from car_app.utils import *


class CarsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode())
        except (json.decoder.JSONDecodeError, UnicodeDecodeError):
            data = None

        file = request.FILES.get("upload_file")

        if file:
            file_name = file.name
            file = file.read()
            path = os.path.join(
                pathlib.Path(__file__).parent, "tmp", f"{file_name}_{int(time())}.xlsx"
            )

            with open(path, "wb") as f:
                f.write(file)

            if ".csv" in file_name:
                data = parse_csv(path)
            elif ".xls" in file_name:
                data = parse_xlsx(path)

            os.remove(path)

        if isinstance(data, list):
            serializer = self.get_serializer(data=request.data if len(data) == 0 else data, many=True)

            serializer.is_valid(raise_exception=True)

            self.perform_create(serializer)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.GET.get("make_file") == "csv":
            headers = [i.name for i in Car._meta.fields]
            path = make_csv(headers, Car.objects.values_list())

            return FileResponse(open(path, "rb"))
        elif request.GET.get("make_file") == "xlsx":
            headers = [i.name for i in Car._meta.fields]
            path = make_xlsx(headers, Car.objects.values_list())

            return FileResponse(open(path, "rb"))

        return super().list(request, *args, **kwargs)



