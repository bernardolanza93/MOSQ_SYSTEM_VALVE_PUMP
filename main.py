import sys

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
finecorsa_pin = 27
# Definizione dei pin GPIO per la pompa
pompa_pin = 22
# Inizializzazione dei pin GPIO


# secondi_settimana = 604800
secondi_settimana = 604800
secondi_svuotamento = 8
secondi_pompaggio = 5


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







def gira_valvola():
    GPIO.output(valvola_pin, GPIO.HIGH)  # Accendi il motore della valvola


def ferma_valvola():
    GPIO.output(valvola_pin, GPIO.LOW)  # Spegni il motore della valvola


def controlla_finecorsa():
    print("STATO PIN FINECORSA:", GPIO.input(finecorsa_pin) )
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
    # Inizializzazione dei pin GPIO

    try:
        while True:

            print("inizializzo")
            time.sleep(2)

            GPIO.setmode(GPIO.BCM)
            GPIO.setup(valvola_pin, GPIO.OUT)
            GPIO.setup(finecorsa_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(pompa_pin, GPIO.OUT)

            #OGNI LUNDI______

            # # Calcola il tempo rimanente fino al prossimo ciclo settimanale
            # remaining_time = calcola_tempo_rimanente()
            #
            # # Aspetta fino al prossimo lunedì alle 12:00
            # time.sleep(remaining_time)


            #TEST HOME


            now = datetime.now()
            hourstr = now.strftime("%Y-%m-%d %H:%M")
            loggingR.error("STARDED cycle: %s", str(hourstr))
            cicli_eseguiti += 1
            loggingR.error("CICLO: %s", str(cicli_eseguiti))
            cpu = CPUTemperature()
            loggingR.error("CPU_temp RPI: %s" % str(cpu.temperature))

            print("inizio ciclo")




            # Apri la valvola
            print("apertura valvola)")
            time.sleep(1)
            gira_valvola()

            # Aspetta fino a quando la valvola si apre completamente
            while not controlla_finecorsa():
                time.sleep(0.1)
            print("finecors raggiunto // STOP // VALVE OPEN")

            ferma_valvola()

            # Aspetta 10 secondi per svuotare il serbatoio
            print("svuotamento")
            time.sleep(secondi_svuotamento)

            print("svuot finito... chiusura valvola....")

            # Chiudi la valvola
            gira_valvola()

            # Aspetta fino a quando la valvola si chiude completamente
            while controlla_finecorsa():
                time.sleep(0.05)

            ferma_valvola()



            print("STOP! CHIUSURA AVVENUTA, attivo pompa")



            time .sleep(2)
            print("pompaggio....")


            # Attiva la pompa
            attiva_pompa()

            # Attendi un po' per consentire il riempimento del serbatoio
            time.sleep(secondi_pompaggio)

            # Disattiva la pompa
            disattiva_pompa()

            print("pompa ferma")

            # Pulisci i GPIO alla fine del ciclo settimanale
            GPIO.cleanup()
            loggingR.error("CYCLE TEMRINATED ")
            print("fine ciclo")
            time.sleep(20)

    except Exception as e:
        loggingR.error("ERRORE: %s", str(e))
        print(e)
        GPIO.cleanup()
        sys.exit()


if __name__ == "__main__":
    main()