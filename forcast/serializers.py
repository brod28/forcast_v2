from rest_framework import serializers

#serializer of forcast model
class ForcastSerializer(serializers.Serializer):
    
    temperature = serializers.CharField(required=True)
    desctiption = serializers.CharField(required=True)
    date = serializers.CharField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.date = validated_data.get('date', instance.date)
        instance.desctiption = validated_data.get('desctiption', instance.desctiption)
        instance.save()
        return instance