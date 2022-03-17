from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=100,
        min_length=3,
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,)

    email = serializers.EmailField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True)

    def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], 
                   validated_data['email'], validated_data['password'])
            return user

    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ('password')
