# tokens.py
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import StudentSerializer

class StudentAccessToken(RefreshToken):
    def __init__(self, student=None):
        super().__init__(student)
        # Serialize the student instance to include its data in the token payload
        serializer = StudentSerializer(student)
        self.update(serializer.data)
        # Add other custom claims as needed

    def __str__(self):
        return str(self.access_token)
