import RPi.GPIO as GPIO
import time
import atexit
import os
import logging
import time
from datetime import datetime
from gpiozero import CPUTemperature

# Definizione dei pin GPIO per la valvola e il finecorsa
valvola_pin = 17
finecorsa_pin = 18

# Definizione dei pin GPIO per la pompa
pompa_pin = 23
# Inizializzazione dei pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(valvola_pin, GPIO.OUT)
GPIO.setup(finecorsa_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pompa_pin, GPIO.OUT)


# Specifica il percorso della cartella da controllare/creare
folder_path = "data"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created.")
else:
    print(f"Folder '{folder_path}' already exists.")


now = datetime.now()
hourstr = now.strftime("%Y-%m-%d %H:%M")


try:
    loggingR = logging.getLogger('RPI')
    loggingR.setLevel(logging.INFO)
    fh = logging.FileHandler('./data/RPI_SH.log')
    fh.setLevel(logging.DEBUG)
    loggingR.addHandler(fh)
    loggingR.error("STARDED LOGGING FILE____time: %s", str(hourstr))

except Exception as e:
    print("ERROR LOGGING: ", e)



# Definizione dei pin GPIO per la valvola e il finecorsa
valvola_pin = 17
finecorsa_pin = 18

# Definizione dei pin GPIO per la pompa
pompa_pin = 23

# secondi_settimana = 604800
secondi_settimana = 604800
secondi_svuotamento = 10
secondi_pompaggio = 20

# Inizializzazione dei pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(valvola_pin, GPIO.OUT)
GPIO.setup(finecorsa_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pompa_pin, GPIO.OUT)


def apri_valvola():
    GPIO.output(valvola_pin, GPIO.HIGH)  # Accendi il motore della valvola


def chiudi_valvola():
    GPIO.output(valvola_pin, GPIO.LOW)  # Spegni il motore della valvola


def controlla_finecorsa():
    return GPIO.input(finecorsa_pin)  # Restituisci lo stato del finecorsa


def attiva_pompa():
    GPIO.output(pompa_pin, GPIO.HIGH)  # Accendi la pompa


def disattiva_pompa():
    GPIO.output(pompa_pin, GPIO.LOW)  # Spegni la pompa


def calcola_tempo_rimanente():
    now = time.localtime()
    # Calcola il tempo in secondi fino al prossimo lunedì alle 12:00
    next_monday = 7 - now.tm_wday  # Giorni fino al prossimo lunedì
    if next_monday == 7:  # Se oggi è lunedì, il prossimo sarà tra 7 giorni
        next_monday = 0
    seconds_until_monday = next_monday * 86400  # Secondi in un giorno
    hours_until_noon = 12 - now.tm_hour
    minutes_until_noon = 60 - now.tm_min
    seconds_until_noon = hours_until_noon * 3600 + minutes_until_noon * 60
    remaining_time = seconds_until_monday + seconds_until_noon
    return remaining_time

def main():
    cicli_eseguiti = 0
    try:
        while True:

            #OGNI LUNDI______

            # # Calcola il tempo rimanente fino al prossimo ciclo settimanale
            # remaining_time = calcola_tempo_rimanente()
            #
            # # Aspetta fino al prossimo lunedì alle 12:00
            # time.sleep(remaining_time)


            #TEST HOME
            time.sleep(60)

            now = datetime.now()
            hourstr = now.strftime("%Y-%m-%d %H:%M")
            loggingR.error("STARDED cycle: %s", str(hourstr))
            cicli_eseguiti += 1
            loggingR.error("CICLO: %s", str(cicli_eseguiti))
            cpu = CPUTemperature()
            loggingR.error("CPU_temp RPI: %s" % str(cpu.temperature))



            # Apri la valvola
            apri_valvola()

            # Aspetta fino a quando la valvola si apre completamente
            while not controlla_finecorsa():
                time.sleep(0.1)

            # Aspetta 10 secondi per svuotare il serbatoio
            time.sleep(secondi_svuotamento)

            # Chiudi la valvola
            chiudi_valvola()

            # Aspetta fino a quando la valvola si chiude completamente
            while controlla_finecorsa():
                time.sleep(0.1)

            # Attiva la pompa
            attiva_pompa()

            # Attendi un po' per consentire il riempimento del serbatoio
            time.sleep(secondi_pompaggio)

            # Disattiva la pompa
            disattiva_pompa()

            # Pulisci i GPIO alla fine del ciclo settimanale
            GPIO.cleanup()



    except KeyboardInterrupt:
        pass  # Non fare nulla in caso di KeyboardInterrupt



if __name__ == "__main__":
    main()