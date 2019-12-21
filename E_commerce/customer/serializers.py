from rest_framework import serializers
from django.contrib.auth import get_user_model 

CustomUser = get_user_model()


class CustomerSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = CustomUser.objects.create(
            username=validated_data['username'],
            is_company=False
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = CustomUser
        fields = ( "id", "username", "password",)