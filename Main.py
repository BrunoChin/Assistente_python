from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
from sqlalchemy import null
from gtts import gTTS
from playsound import playsound
import core
from nlu.classifier import classify

bot = ChatBot("Hikary")

def recognition():
    mic = sr.Recognizer()
    mic.energy_threshold = 4000
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Mic...")
        audio = mic.listen(source)
    try:
        frase = mic.recognize_google(audio, language='pt-BR')
        print(str(frase))
        return frase
    except sr.UnknownValueError:
        print('Bot: Não foi possivel identificar')
        return null

def synthesize(audio):
    if audio == "" or audio == " ":
        return
    tts = gTTS(audio, lang="pt-BR")
    tts.save('bot.mp3')
    playsound('bot.mp3')

conversa = open('conversation.txt', 'r', encoding='utf-8').read().split('\n')
print(conversa)
trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    quest = recognition()
    if quest != null:

        entity = classify(quest)

        if entity == "time/getTime":
            synthesize(core.SystemInfo.get_time())
            print("Time")
        elif entity == "time/getDate":
            synthesize(core.SystemInfo.get_date())
            print("Date")
        else:
            resposta = bot.get_response(quest)
            synthesize(str(resposta))
            print('Hikary: ', resposta )