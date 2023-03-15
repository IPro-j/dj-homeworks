import telebot
import urllib
from bs4 import BeautifulSoup
import random


bot = telebot.TeleBot('6109078696:AAEUh_jyZUme1oC_69GjzN89J-4e4pmQKGY')
site = urllib.request.urlopen('https://pythonist.ru/spisok-zadach-proekt-ejlera-s-resheniyami/').read()
soup = BeautifulSoup(site, "html.parser")

raw_excersises = soup.find('div', {"class": 'entry-content'}) #забираем интересующий нас кусок кода
excersises = raw_excersises.find_all('a')
links_to_excersises = []
for i in range(len(excersises)):
    links_to_excersises.append(excersises[i].get('href'))


@bot.message_handler(commands=['task'])
def send_task(message):
    link_to_send = random.choice(links_to_excersises)
    bot.reply_to(message, f'Окей, решайте вот эту задачу — {link_to_send}')

    site = urllib.request.urlopen('%s' % link_to_send).read()
    task_text = BeautifulSoup(site, "html.parser")
    raw_text = task_text.find('div', {"class": 'entry-content'})
    text = []
    for tag in raw_text:
        if tag.name in ['h3', 'h4', 'p', 'pre', ]:
            text.append(tag.text)

    print(  '\n'.join(text) )
    bot.reply_to(message, '\n\n'.join(text))

    #raw_text = task_text.find('div', {"class": 'entry-content'})



@bot.message_handler(commands=['start'])
def command_hello(message):
    bot.reply_to(message, "Привет, если вы видите это сообщение, значит я работаю так, как надо:)")



bot.polling(none_stop=True, interval=0)

