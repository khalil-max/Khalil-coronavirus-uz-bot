from covid.api import CovId19Data
import telebot


api = CovId19Data(force=True)

bot = telebot.TeleBot('Sizning belgi')
@bot.message_handler(commands=['start'])
def welcome(message):

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, созданный для того чтобы показать тебе сколько человек \n    Заражено \n    Умерло\n    Выздровело \nОт COVID19\nВсе очень просто ты пишешь страну я тебе отвечаю\nНапример США, Узбекистан и т.д\nДля списка комманд напишите /commands".format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(commands=['commands'])
def command(message):
	bot.send_message(message.chat.id, "\n/list: Список доступных стран\n""/authors: Авторы проэкта\n/communication: Связь т.е данные чтобы со мной связаться")

@bot.message_handler(commands=['list'])
def ldl(message):
	bot.send_message(message.chat.id, "Все страны т.е абсолютно все страны.\nЭтот бот даст информацию о COVID19 во всем мире главное напишите название страны правильно")


@bot.message_handler(commands=['authors'])
def author(message):
	bot.send_message(message.chat.id,"Бота сделали:\nПрограммист(Создатель):Джалолов Абдухалил(14лет)\nТестировщик:Джалолов Далер(21год)")
@bot.message_handler(commands=['communication'])
def comm(message):
	bot.send_message(message.chat.id,"Мой телерамм:\nhttps://t.me/abdukhalilZ3Kalinethunter")
@bot.message_handler(content_types=['text'])
def mess(message):

	good_bye_message = ""
	a = message.text
	test = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Diamond Princess', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon', 'Liberia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malaysia', 'Maldives', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Taiwan*', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'US', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe', 'Dominica', 'Grenada', 'Mozambique', 'Syria', 'Timor-Leste', 'Belize', 'Laos', 'Libya', 'West Bank and Gaza', 'Guinea-Bissau', 'Mali', 'Saint Kitts and Nevis', 'Kosovo', 'Burma', 'MS Zaandam', 'Botswana', 'Burundi', 'Sierra Leone', 'Malawi', 'South Sudan', 'Western Sahara', 'Sao Tome and Principe', 'Yemen', 'Comoros', 'Tajikistan']

	if a == "AQSH" or a == 'Amerika' or a == 'aqsh':
		res = api.filter_by_country("US")
	elif a == "Ukraina":
		res = api.filter_by_country("Ukraine")
	elif a == "Rossiya":
		res = api.filter_by_country("Russia")
	elif a == "Belarusiya":
		res = api.filter_by_country("Belarus")
	elif a == "Qozog’iston":
		res = api.filter_by_country("Kazakhstan")
	elif a == "Italiya":
		res = api.filter_by_country("Italy")
	elif a == "Frantsiya":
		res = api.filter_by_country("French")
	elif a == "Germaniya":
		res = api.filter_by_country("Germany")
	elif a == "Yaponiya":
		res = api.filter_by_country("Japan")
	elif a == "Ozbekiston":
		res = api.filter_by_country('Uzbekistan')
	elif a == "Xitoy":
		res = api.filter_by_country('China')
	elif a == 'Afgoniston':
		res = api.filter_by_country(test[0])
	elif a == "Albaniya":
		res = api.filter_by_country(test[1])
	#elif a == "":
		#res = api.filter_by_country(test[42])
	else:
		res = api.get_stats()
		good_bye_message = f"Во всем мире:\n     Последнее обновление: {res['last_updated']}\n<b>     Выздровело</b> {res['recovered']:,} людей\n     <b>Заражено: </b>{res['confirmed']:,} людей\n     <b>Умерло: </b>{res['deaths']:,} людей "

	if good_bye_message == "":
		good_bye_message = f"Данные по стране:\n     Последние данные были обновлены: {res['last_updated']}\n    Выздровело {res['recovered']:,}\n     Заражено: {res['confirmed']:,}\n     Умерло: {res['deaths']:,}"

	bot.send_message(message.chat.id, good_bye_message, parse_mode='html')

bot.polling(none_stop=True)
#Barcha mavjud bo'lgan mamlakatlarni ko'rsatadi.
#res = api.show_available_countries()
#Mamlakat filtri
#res = api.filter_by_country("Uzbekistan")
#print(res)
