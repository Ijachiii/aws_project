from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProcessSerializer
from .tasks import process_message
from celery.result import AsyncResult
from .models import Process

# Create your views here.
class ProcessAPIView(APIView):
    def post(self, request):
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid():
            message_instance = serializer.save(status="queued")
            task = process_message.delay(message_instance.id)
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatusView(APIView):
    def get(self, request, task_id):
        result = AsyncResult(task_id)

        # Default response
        response_data = {
            "task_id": task_id,
        }

        try:
            message = Process.objects.get(id=task_id)
            response_data.update({
                "status": message.status,
                "message_id": message.id,
                "result": message.result,
            })
        except Process.DoesNotExist:
            response_data["detail"] = "ID does not exist"

        return Response(response_data, status=status.HTTP_200_OK)


# class TaskStatusView(APIView):
#     def get(self, request, task_id):
#         result = AsyncResult(task_id)
#         return Response({
#             'task_id': task_id,
#             'state': result.state,
#             'result': result.result if result.ready() else None
#         })