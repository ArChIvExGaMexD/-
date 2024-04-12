import RPi.GPIO as GPIO
import telebot
import time
token="6704811470:AAFmlHtEnA3nWS4dfZ2GepCcJE3nfd0xEZs"
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12, GPIO.IN)
try:
    while True:
        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id,"Привет ")
        
        @bot.message_handler(commands=['OPEN'])
        def open_message(message):
            GPIO.output(6, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(6, GPIO.LOW)
        
        bot.infinity_poling()
        
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()