from rest_framework import serializers, status
from rest_framework.response import Response


class RegisterApiView(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        email = serializers.EmailField()
        phone = serializers.CharField()
        password = serializers.CharField()
        confirm_password = serializers.CharField()

    def post(self, request):
        if request.user.is_authenticated:
            return Response(
                {"error": "You are already authenticated"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.InputSerializer(request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
