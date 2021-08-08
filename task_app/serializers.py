from rest_framework_json_api import serializers
from task_app.models import Word

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
