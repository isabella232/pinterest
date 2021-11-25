from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Pins.models import Pin
from .serializers import PinSerializer


class PinList(APIView):
    """
    List all pins, or create a new pin.
    """

    def get(self, request, format=None):
        pins = Pin.objects.all()
        serialized_pins = PinSerializer(instance=pins, many=True)
        return Response(data=serialized_pins.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serialized_pin = PinSerializer(data=request.data)
        if serialized_pin.is_valid():
            serialized_pin.save()
            return Response(serialized_pin.data, status=status.HTTP_201_CREATED)
        return Response(serialized_pin.errors, status=status.HTTP_400_BAD_REQUEST)


class PinDetails(APIView):
    """
    Retrieve, update or delete a pin instance.
    """

    def get_object(self, pk):
        try:
            return Pin.objects.get(pk=pk)
        except Pin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pin = self.get_object(pk)
        serialized_pin = PinSerializer(pin)
        return Response(serialized_pin.data)

    def patch(self, request, pk, format=None):
        pin = self.get_object(pk)
        serialized_pin = PinSerializer(pin, data=request.data, partial=True)
        if serialized_pin.is_valid():
            serialized_pin.save()
            return Response(serialized_pin.data)
        return Response(serialized_pin.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        pin = self.get_object(pk)
        serialized_pin = PinSerializer(pin, data=request.data)
        if serialized_pin.is_valid():
            serialized_pin.save()
            return Response(serialized_pin.data)
        return Response(serialized_pin.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pin = self.get_object(pk)
        pin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)