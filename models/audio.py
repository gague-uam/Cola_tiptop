import speech_recognition as sr

def transcribe_audio():
    reconocedor = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando el ruido ambiental...")
        reconocedor.adjust_for_ambient_noise(source, duration=3)
        print("Grabando audio...")

        try:
            audio = reconocedor.listen(source, timeout=5, phrase_time_limit=10)
            print("Reconociendo")

            texto = reconocedor.recognize_google(audio, language='es-ES')
            print("Texto reconocido: ")
            print(texto)
            return texto
        
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado. No se detectó audio.")
            return None
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
            return None
        except sr.RequestError as e:
            print(f"No se pudo conectar al servicio de reconocimiento de voz: {e}")
            return None