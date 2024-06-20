import pygame
import time
import sys
import cv2
import threading
import webbrowser
import os

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

sound = os.path.join(application_path, 'sound1.wav')
sound2 = os.path.join(application_path, 'sound2.wav')
rojo = (255, 0, 0)
webcamOpened = False
pygame.display.set_caption("MEYUMI")

def salir():
    pygame.quit()
    sys.exit()

def enter(esperando=True):
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperando = False
                if event.key == pygame.K_q:
                    salir()
    screen.fill((0, 0, 0))
    #pygame.display.flip()  # Update the screen to reflect the changes


def texto(mensaje, color=(255, 255, 255), velocidad=0.015,esperar=True):
    fuente = pygame.font.Font(None, 36)
    lineas = mensaje.split('\n')
    for i, linea in enumerate(lineas):
        for j, letra in enumerate(linea):
            texto = fuente.render(letra, True, color)
            texto_rect = texto.get_rect(center=(150 + j*20, 250 + i*40))  # ajusta la posición x para cada letra
            screen.blit(texto, texto_rect)
            pygame.display.flip()
            time.sleep(velocidad)  # añade un pequeño retraso para crear el efecto de animación
    if mensaje != "Te amo":
        enter(esperar)

def subtitulo(mensaje, color=(128, 128, 128), velocidad=0.001):
    fuente = pygame.font.Font(None, 25)
    lineas = mensaje.split('\n')
    for i, linea in enumerate(lineas):
        for j, letra in enumerate(linea):
            texto = fuente.render(letra, True, color)
            texto_rect = texto.get_rect(center=(150 + j*14, 350 + i*10))  # ajusta la posición x para cada letra
            screen.blit(texto, texto_rect)
            pygame.display.flip()
            time.sleep(velocidad)  # añade un pequeño retraso para crear el efecto de animación

def reproducir(path, time=0.0):
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(fade_ms=50, loops=-1, start=time)
    except Exception as e:
        print(f"Error al reproducir el archivo: {e}")

def detener():
    try:
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.unload()
    except Exception as e:
        print(f"Error al detener la reproducción: {e}")

def continuar(isActive=True):
    try:
        if isActive:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    except Exception as e:
        print(f"Error al continuar la reproducción: {e}")
def capture_video():
    global webcamOpened
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        webcamOpened = False
        raise Exception("Error al abrir la cámara")
    
    while True:
        webcamOpened = True
        ret, frame = cap.read()

        if not ret:
            print("Error: No se puede recibir el frame")
            break
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) == 13:  # 13 is the ASCII code for Enter key
            break

    cap.release()
    cv2.destroyAllWindows()

def activar_webcam():
    try:
        video_thread = threading.Thread(target=capture_video)
        video_thread.start()
        return video_thread
    except Exception as e:
        print(f"fun activar_Webcam: {e}")
        return False

def virus():
    url = 'https://web.whatsapp.com/send/?phone=9212359096&text=Siempre+sere+tuya🌹🖤&type=phone_number&app_absent=0'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    webbrowser.open(url, new=2, autoraise=True)
                    salir()


def main():
    reproducir(sound2,1)
    subtitulo("Continua con Enter...")
    texto("Hola bonita")
    texto("¿Alguna vez te he dicho \nlo mucho que te amo?")
    texto("Eres lo mas especial de \nmi vida y me gusta \nestar contigo")
    texto("Yo tambien te gusto \n¿Verdad. . .?", velocidad=0.1)
    continuar(False)
    texto(". . .", velocidad=0.08)
    continuar(True)
    texto("Espero que hayas dicho \nque si")
    texto("Por que no puedo vivir sin ti", rojo,0.025,False)

    activar_webcam()

    texto("Y ademas aun no \npuedo acceder a tu microfono \npara escucharte", velocidad=0.08)
    detener()

    reproducir(sound, 5)
    if(webcamOpened):
        texto("Perdon \nme olvide de que si podia...",rojo)

    texto("¿Pero no importa cierto?",rojo)
    texto("Por que tu eres MIA",rojo, 0.1)
    texto("Y YO soy tuyo",rojo, 0.1)
    texto("Y asi sera por siempre",rojo, 0.05)
    subtitulo("Q para salir...")
    texto("TE AMO",rojo, 0.1,False)
    virus()

main()