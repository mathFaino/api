from rest_framework.serializers import ModelSerializer
from analise_video.models import AnaliseVideo


class AnaliseVideoSerializer(ModelSerializer):
    class Meta:
        model = AnaliseVideo
        fields = ('possivel_depressao', 'porcentagem_emocao1', 'porcentagem_emocao2',
                  'porcentagem_emocao3', 'data')
