from rest_framework import serializers
from analise_video.models import AnaliseVideo


class AnaliseVideoSerializer(serializers.ModelSerializer):
    video = serializers.CharField(read_only=True)

    class Meta:
        model = AnaliseVideo
        fields = ('id', 'possivel_depressao', 'porcentagem_emocao1', 'porcentagem_emocao2',
                  'porcentagem_emocao3', 'data', 'video')
        read_only_fields = ['__all__']
