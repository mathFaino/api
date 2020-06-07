from rest_framework import serializers
from analise_video.models import AnaliseVideo
import reconhece.reconhecer as reconhecer


class AnaliseVideoSerializer(serializers.ModelSerializer):
    video = serializers.CharField(read_only=True)

    class Meta:
        model = AnaliseVideo
        fields = ('id', 'possivel_depressao', 'porcentagem_emocao1', 'porcentagem_emocao2',
                  'porcentagem_emocao3', 'data', 'video')
        read_only_fields = ['__all__']

    def create(self, validated_data):
        caminho = '../../media_images/videos/'
        video = validated_data['video']
        video = video.split('videos')

        reconhecer_obj = reconhecer.Reconhecer(caminho + video[1])
        result = reconhecer_obj.realizar_reconhecimento()

        emocoes = self.top_three(result)

        validated_data['porcentagem_emocao1'] = emocoes[0]
        validated_data['porcentagem_emocao2'] = emocoes[1]
        validated_data['porcentagem_emocao3'] = emocoes[2]

    def top_three(self, map_sended):
        lista = []
        contador = 0
        pos = []
        lista_emotions = []
        while contador <= (len(map_sended) - 1):
            lista.append(map_sended[contador][1])
            contador += 1
        original_list = lista.copy()
        lista.sort()
        tops = lista[-3:]
        q = sorted(tops, reverse=True)

        for a in q:
            print(a)
            pos.append(original_list.index(a))

        for b in pos:
            lista_emotions.append((map_sended[b][0] + map_sended[b][1]))
        return lista_emotions
