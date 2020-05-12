import telebot
import config
from bs4 import BeautifulSoup
import requests as req
from itertools import groupby
from telebot import types
from requests import get


def countries_europe():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/europe/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	countries = []
	links = []
	for i in range(1,len(tr)-1):
		td = tr[i].find('td')
		a = td.find('a')
		countries.append(a.text)
		links.append('https://index.minfin.com.ua/' + str(a.get('href')))

	return countries,links

def europe_all():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/europe/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	text = 'Всего\n'
	td = tr[len(tr)-1].find_all('td')
	text += 'Всего Заражений ' + td[1].text + '(' + td[2].text + ')\n'
	text += 'Смертельные случаи ' + td[3].text + '(' + td[4].text + ')\n'
	text += 'Выздоровевшие ' + td[5].text + '(' + td[6].text + ')\n'
	text += 'Сейчас болет ' + td[7].text



	return text

def countries_asia():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/asia/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	countries = []
	links = []
	for i in range(1,len(tr)-1):
		td = tr[i].find('td')
		a = td.find('a')
		countries.append(a.text)
		links.append('https://index.minfin.com.ua/' + str(a.get('href')))

	return countries,links

def asia_all():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/asia/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	text = 'Всего\n'
	td = tr[len(tr)-1].find_all('td')
	text += 'Всего Заражений ' + td[1].text + '(' + td[2].text + ')\n'
	text += 'Смертельные случаи ' + td[3].text + '(' + td[4].text + ')\n'
	text += 'Выздоровевшие ' + td[5].text + '(' + td[6].text + ')\n'
	text += 'Сейчас болет ' + td[7].text



	return text

def countries_north_america():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/north_america/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	countries = []
	links = []
	for i in range(1,len(tr)-1):
		td = tr[i].find('td')
		a = td.find('a')
		countries.append(a.text)
		links.append('https://index.minfin.com.ua/' + str(a.get('href')))

	return countries,links

def north_america_all():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/north_america/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	text = 'Всего\n'
	td = tr[len(tr)-1].find_all('td')
	text += 'Всего Заражений ' + td[1].text + '(' + td[2].text + ')\n'
	text += 'Смертельные случаи ' + td[3].text + '(' + td[4].text + ')\n'
	text += 'Выздоровевшие ' + td[5].text + '(' + td[6].text + ')\n'
	text += 'Сейчас болет ' + td[7].text



	return text

def countries_south_america():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/south_america/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	countries = []
	links = []
	for i in range(1,len(tr)-1):
		td = tr[i].find('td')
		a = td.find('a')
		countries.append(a.text)
		links.append('https://index.minfin.com.ua/' + str(a.get('href')))

	return countries,links

def south_america_all():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/south_america/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	text = 'Всего\n'
	td = tr[len(tr)-1].find_all('td')
	text += 'Всего Заражений ' + td[1].text + '(' + td[2].text + ')\n'
	text += 'Смертельные случаи ' + td[3].text + '(' + td[4].text + ')\n'
	text += 'Выздоровевшие ' + td[5].text + '(' + td[6].text + ')\n'
	text += 'Сейчас болет ' + td[7].text



	return text

def countries_africa():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/africa/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	countries = []
	links = []
	for i in range(1,len(tr)-1):
		td = tr[i].find('td')
		a = td.find('a')
		countries.append(a.text)
		links.append('https://index.minfin.com.ua/' + str(a.get('href')))

	return countries,links

def africa_all():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/africa/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	text = 'Всего\n'
	td = tr[len(tr)-1].find_all('td')
	text += 'Всего Заражений ' + td[1].text + '(' + td[2].text + ')\n'
	text += 'Смертельные случаи ' + td[3].text + '(' + td[4].text + ')\n'
	text += 'Выздоровевшие ' + td[5].text + '(' + td[6].text + ')\n'
	text += 'Сейчас болет ' + td[7].text



	return text

def countries_oceania():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/oceania/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	countries = []
	links = []
	for i in range(1,len(tr)-1):
		td = tr[i].find('td')
		a = td.find('a')
		countries.append(a.text)
		links.append('https://index.minfin.com.ua/' + str(a.get('href')))

	return countries,links

def oceania_all():
	link = 'https://index.minfin.com.ua/reference/coronavirus/geography/oceania/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	div6 = article.find('div',id = 'tm-table')
	table = div6.find('table')
	tr = table.find_all('tr')
	text = 'Всего\n'
	td = tr[len(tr)-1].find_all('td')
	text += 'Всего Заражений ' + td[1].text + '(' + td[2].text + ')\n'
	text += 'Смертельные случаи ' + td[3].text + '(' + td[4].text + ')\n'
	text += 'Выздоровевшие ' + td[5].text + '(' + td[6].text + ')\n'
	text += 'Сейчас болет ' + td[7].text



	return text

def country_stat(link):
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	table = article.find('table')
	caption = table.find('caption')
	title = caption.text
	text = str(title) + '\n'
	tr = table.find_all('tr')
	for i in tr:
		td = i.find_all('td')
		for j in range(len(td)):
			td[j] = ''.join(td[j].text.split('­­­­­­­­­'))
		text += str(' '.join(td)) + '\n'	
	return text

def stats_all():
	link = 'https://index.minfin.com.ua/reference/coronavirus/'
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	soup = BeautifulSoup(resp.text,'lxml')
	body = soup.body
	main = body.main
	div1 = main.find('div',class_ = 'mfz-container')
	div2 = div1.find('div',class_ = 'mfz-content-wrapper')
	div3 = div2.find('div',class_ = 'mfz-col-content')
	div4 = div3.find('div',class_ = 'container clearfix')
	div5 = div4.find('div',id = 'idx-wrapper')
	article = div5.find('article',id = 'idx-content')
	table = article.find('table')
	caption = table.find('caption')
	title = caption.text
	text = str(title) + '\n'
	tr = table.find_all('tr')
	for i in tr:
		td = i.find_all('td')
		for j in range(len(td)):
			td[j] = ''.join(td[j].text.split('­'))
		text += str(' '.join(td)) + '\n'	
	return text

bot = telebot.TeleBot(config.TOKEN)

back = ''

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.InlineKeyboardMarkup(row_width = 1)
	item2 = types.InlineKeyboardButton(text = 'Статистика по миру',callback_data = 'stats_all')
	item3 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'stats_countries')
	markup.add(item2,item3)
	bot.send_message(message.chat.id,text = 'Коронавирус',reply_markup = markup)
	file = open('data.txt','r')
	data = file.read()
	file.close()
	if str(message.from_user.username) not in data:
		data += ',@' + str(message.from_user.username)
	file = open('data.txt','w')
	file.write(str(data))
	file.close()

@bot.message_handler(commands=['SendUsers'])
def send(message):
	file = open('data.txt','r')
	data = file.read()
	file.close()
	bot.send_message(chat_id = '@aganydavai',text = str(data))

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	global back
	if call.data == 'main':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item2 = types.InlineKeyboardButton(text = 'Статистика по миру',callback_data = 'stats_all')
		item3 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'stats_countries')
		markup.add(item2,item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус',reply_markup = markup)
	elif call.data == 'stats_all':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Главная',callback_data = 'main')
		markup.add(item1)

		text = stats_all()
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)
	elif call.data == 'stats_countries':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Европа',callback_data = 'europe')
		item2 = types.InlineKeyboardButton(text = 'Азия',callback_data = 'asia')
		item3 = types.InlineKeyboardButton(text = 'Северная Америка',callback_data = 'north_america')
		item4 = types.InlineKeyboardButton(text = 'Южная Америка',callback_data = 'south_america')
		item5 = types.InlineKeyboardButton(text = 'Африка',callback_data = 'africa')
		item6 = types.InlineKeyboardButton(text = 'Австралия и Океания',callback_data = 'oceania')
		item7 = types.InlineKeyboardButton(text = 'Главная',callback_data = 'main')
		markup.add(item1,item2,item3,item4,item5,item6,item7)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Статистика по частям мира',reply_markup = markup)
	

	elif call.data == 'europe':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'europe_countries1')
		item2 = types.InlineKeyboardButton(text = 'Всего',callback_data = 'europe_all')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'stats_countries')
		markup.add(item1,item2,item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
	elif call.data == 'europe_all':
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1)

		text = europe_all()
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)
	elif call.data == 'europe_countries1':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		countries,link = countries_europe()
		for i in range(5):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)

		item1 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries2')
		item2 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries2':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(5,10):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries1')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries3')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries3':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(10,15):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries2')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries4')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries4':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(15,20):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries3')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries5')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries5':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(20,25):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries4')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries6')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries6':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(25,30):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries5')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries7')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries7':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(30,35):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries6')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries8')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries8':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(35,40):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries7')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries9')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries9':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(40,45):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries8')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'europe_countries10')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif call.data == 'europe_countries10':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_europe()
		for i in range(45,50


			):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'europe_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'europe_countries9')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'europe')
		markup.add(item1)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Европа',reply_markup = markup)
		back = call.data
	elif 'europe_country_' in call.data:
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text= 'Назад',callback_data = back)
		markup.add(item1)
		link_id = ''.join(call.data.split('europe_country_'))
		countries,link = countries_europe()
		text = country_stat(link[int(link_id)])
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)


	elif call.data == 'asia':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'asia_countries1')
		item2 = types.InlineKeyboardButton(text = 'Всего',callback_data = 'asia_all')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'stats_countries')
		markup.add(item1,item2,item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
	elif call.data == 'asia_all':
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1)

		text = asia_all()
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)
	elif call.data == 'asia_countries1':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		countries,link = countries_asia()
		for i in range(5):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)

		item1 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries2')
		item2 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries2':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(5,10):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries1')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries3')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries3':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(10,15):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries2')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries4')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries4':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(15,20):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries3')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries5')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries5':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(20,25):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries4')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries6')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries6':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(25,30):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries5')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries7')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries7':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(30,35):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries6')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries8')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries8':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(35,40):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries7')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries9')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries9':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(40,45):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries8')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'asia_countries10')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif call.data == 'asia_countries10':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_asia()
		for i in range(45,49):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'asia_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'asia_countries9')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'asia')
		markup.add(item1)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Азия',reply_markup = markup)
		back = call.data
	elif 'asia_country_' in call.data:
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text= 'Назад',callback_data = back)
		markup.add(item1)
		link_id = ''.join(call.data.split('asia_country_'))
		countries,link = countries_asia()
		text = country_stat(link[int(link_id)])
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)

	elif call.data == 'north_america':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'north_america_countries1')
		item2 = types.InlineKeyboardButton(text = 'Всего',callback_data = 'north_america_all')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'stats_countries')
		markup.add(item1,item2,item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
	elif call.data == 'north_america_all':
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1)

		text = north_america_all()
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)
	elif call.data == 'north_america_countries1':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		countries,link = countries_north_america()
		for i in range(5):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)

		item1 = types.InlineKeyboardButton(text = '>>>',callback_data = 'north_america_countries2')
		item2 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1,item2)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'north_america_countries2':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_north_america()
		for i in range(5,10):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'north_america_countries1')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'north_america_countries3')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'north_america_countries3':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_north_america()
		for i in range(10,15):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'north_america_countries2')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'north_america_countries4')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'north_america_countries4':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_north_america()
		for i in range(15,20):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'north_america_countries3')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'north_america_countries5')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'north_america_countries5':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_north_america()
		for i in range(20,25):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'north_america_countries4')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'north_america_countries6')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'north_america_countries6':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_north_america()
		for i in range(25,30):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'north_america_countries5')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'north_america_countries7')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'north_america_countries7':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_north_america()
		for i in range(30,35):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'north_america_countries6')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'north_america_countries8')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'north_america_countries8':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_north_america()
		for i in range(35,37):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'north_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'north_america_countries7')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'north_america')
		markup.add(item1)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Северная Америка',reply_markup = markup)
		back = call.data
	elif 'north_america_country_' in call.data:
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text= 'Назад',callback_data = back)
		markup.add(item1)
		link_id = ''.join(call.data.split('north_america_country_'))
		countries,link = countries_north_america()
		text = country_stat(link[int(link_id)])
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)

	elif call.data == 'south_america':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'south_america_countries1')
		item2 = types.InlineKeyboardButton(text = 'Всего',callback_data = 'south_america_all')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'stats_countries')
		markup.add(item1,item2,item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Южная Америка',reply_markup = markup)
	elif call.data == 'south_america_all':
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'south_america')
		markup.add(item1)

		text = south_america_all()
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)
	elif call.data == 'south_america_countries1':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		countries,link = countries_south_america()
		for i in range(5):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'south_america_country_' + str(i))
			markup.add(item)

		item1 = types.InlineKeyboardButton(text = '>>>',callback_data = 'south_america_countries2')
		item2 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'south_america')
		markup.add(item1,item2)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Южная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'south_america_countries2':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_south_america()
		for i in range(5,10):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'south_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'south_america_countries1')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'south_america_countries3')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'south_america')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Южная Америка',reply_markup = markup)
		back = call.data
	elif call.data == 'south_america_countries3':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_south_america()
		for i in range(10,15):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'south_america_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'south_america_countries2')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'south_america')
		markup.add(item1)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Южная Америка',reply_markup = markup)
		back = call.data
	elif 'south_america_country_' in call.data:
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text= 'Назад',callback_data = back)
		markup.add(item1)
		link_id = ''.join(call.data.split('south_america_country_'))
		countries,link = countries_south_america()
		text = country_stat(link[int(link_id)])
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)

	elif call.data == 'africa':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'africa_countries1')
		item2 = types.InlineKeyboardButton(text = 'Всего',callback_data = 'africa_all')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'stats_countries')
		markup.add(item1,item2,item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
	elif call.data == 'africa_all':
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1)

		text = africa_all()
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)
	elif call.data == 'africa_countries1':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		countries,link = countries_africa()
		for i in range(5):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)

		item1 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries2')
		item2 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries2':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(5,10):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries1')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries3')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries3':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(10,15):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries2')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries4')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries4':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(15,20):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries3')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries5')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries5':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(20,25):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries4')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries6')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries6':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(25,30):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries5')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries7')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries7':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(30,35):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries6')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries8')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries8':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(35,40):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries7')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries9')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries9':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(40,45):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries8')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries10')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'adrica_countries10':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(45,50):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries9')
		item2 = types.InlineKeyboardButton(text = '>>>',callback_data = 'africa_countries11')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1,item2)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif call.data == 'africa_countries11':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_africa()
		for i in range(50,55):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'africa_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'africa_countries10')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'africa')
		markup.add(item1)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Африка',reply_markup = markup)
		back = call.data
	elif 'africa_country_' in call.data:
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text= 'Назад',callback_data = back)
		markup.add(item1)
		link_id = ''.join(call.data.split('africa_country_'))
		countries,link = countries_africa()
		text = country_stat(link[int(link_id)])
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)

	elif call.data == 'oceania':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton(text = 'Статистика по странам',callback_data = 'oceania_countries1')
		item2 = types.InlineKeyboardButton(text = 'Всего',callback_data = 'oceania_all')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'stats_countries')
		markup.add(item1,item2,item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Австралия и Океания',reply_markup = markup)
	elif call.data == 'oceania_all':
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'oceania')
		markup.add(item1)

		text = oceania_all()
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)
	elif call.data == 'oceania_countries1':
		markup = types.InlineKeyboardMarkup(row_width = 1)
		countries,link = countries_oceania()
		for i in range(5):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'oceania_country_' + str(i))
			markup.add(item)

		item1 = types.InlineKeyboardButton(text = '>>>',callback_data = 'oceania_countries2')
		item2 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'oceania')
		markup.add(item1,item2)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Австралия и Океания',reply_markup = markup)
		back = call.data
	elif call.data == 'oceania_countries2':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		countries,link = countries_oceania()
		for i in range(5,6):
			item = types.InlineKeyboardButton(text = str(countries[i]),callback_data = 'oceania_country_' + str(i))
			markup.add(item)
		item1 = types.InlineKeyboardButton(text = '<<<',callback_data = 'oceania_countries1')
		item3 = types.InlineKeyboardButton(text = 'Назад',callback_data = 'oceania')
		markup.add(item1)
		markup.add(item3)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Коронавирус.Австралия и Океания',reply_markup = markup)
		back = call.data
	elif 'oceania_country_' in call.data:
		markup = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton(text= 'Назад',callback_data = back)
		markup.add(item1)
		link_id = ''.join(call.data.split('oceania_country_'))
		countries,link = countries_oceania()
		text = country_stat(link[int(link_id)])
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = str(text),reply_markup = markup)

bot.polling(none_stop=True)