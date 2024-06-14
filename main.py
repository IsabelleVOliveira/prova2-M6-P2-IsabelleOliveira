import sys
import signal
import cv2

end = False

# --------------------------------------

# Carregar o classificador pré-treinado
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
# smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Ler o vídeo
video = cv2.VideoCapture('la_cabra.mp4')

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    
   
    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Detectar rostos de perfil 
    # profile = profile_cascade.detectMultiScale(gray, 1.1, 10)
    # # Detectar sorisos
    # smile = smile_cascade.detectMultiScale(gray, 1.1, 10)
    # Detectar rostos
    faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.08,
            minNeighbors=10,
            minSize=(64,64),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

    # Desenhar retângulos em torno dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Mostrar o frame resultante
    cv2.imshow('Frame', frame)

    # Pausar a execução se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # for (x, y, w, h) in profile:
    #     pass

    # for (x, y, w, h) in smile:
    #     pass

def signal_handler(signal, frame):
    global end
    end = True

if not video.isOpened():
    print('Não foi possível abrir a web cam.')
    sys.exit(-1)

# Cria o arquivo de video de saída
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# Captura o sinal de CTRL+C no terminal
signal.signal(signal.SIGINT, signal_handler)


video.release()
out.release()
# Liberar recursos
video.release()
cv2.destroyAllWindows()