import reconhece.reconhecer as reconhecer

caminho = '../media_images/videos/'
video = 'http://127.0.0.1:8000/media_files/videos/meu_video.mp4'
video = video.split('videos')


variavel = reconhecer.Reconhecer(caminho + video[1])
variavel2 = variavel.realizar_reconhecimento()
print(variavel2)
print("AAAAa")
