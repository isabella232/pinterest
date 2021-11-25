from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Boards.models import Board
from .serializers import BoardSerializer


class BoardList(APIView):
    """
    List all boards, or create a new board.
    """

    def get(self, request, format=None):
        boards = Board.objects.all()
        serialized_boards = BoardSerializer(instance=boards, many=True)
        return Response(data=serialized_boards.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serialized_board = BoardSerializer(data=request.data)
        if serialized_board.is_valid():
            serialized_board.save()
            return Response(serialized_board.data, status=status.HTTP_201_CREATED)
        return Response(serialized_board.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetails(APIView):
    """
    Retrieve, update or delete a board instance.
    """

    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        board = self.get_object(pk)
        serialized_board = BoardSerializer(board)
        return Response(serialized_board.data)

    def patch(self, request, pk, format=None):
        board = self.get_object(pk)
        serialized_board = BoardSerializer(board, data=request.data, partial=True)
        if serialized_board.is_valid():
            serialized_board.save()
            return Response(serialized_board.data)
        return Response(serialized_board.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        board = self.get_object(pk)
        serialized_board = BoardSerializer(board, data=request.data)
        if serialized_board.is_valid():
            serialized_board.save()
            return Response(serialized_board.data)
        return Response(serialized_board.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)