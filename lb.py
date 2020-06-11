# -*- coding: utf8 -*-

import telebot
from telebot import types
bot = telebot.TeleBot('1041127038:AAET9NNqg1bqlCxrJkBRaWFscqt-hMARTps')

############################# MAIN ############################# 
keyboard_main = telebot.types.ReplyKeyboardMarkup(True, True)
btn1 = types.KeyboardButton(text = '/start')
keyboard_main.add(btn1)



############################# KEYBOARD FOR CZECH ############################# 
kb_for_cz = telebot.types.InlineKeyboardMarkup()
audio = telebot.types.InlineKeyboardButton(text = 'Аудио', callback_data = 'Audio_for_cz')
YouTube = telebot.types.InlineKeyboardButton(text = 'Каналы Ютуб', callback_data = 'YT_for_cz' )
inst = telebot.types.InlineKeyboardButton(text = 'Аккаунты Инстаграм', callback_data = 'Inst_for_cz')
textbook = telebot.types.InlineKeyboardButton(text = 'Учебники', callback_data = 'Textbooks_for_cz')
reading = telebot.types.InlineKeyboardButton(text = 'Книги', callback_data = 'Books_for_cz')
TV = telebot.types.InlineKeyboardButton(text = 'Сериалы и фильмы', callback_data = 'TV_for_cz')
words = telebot.types.InlineKeyboardButton(text = 'Изучение слов', callback_data = 'Words_for_cz')
kb_for_cz.add(audio)
kb_for_cz.add(YouTube)
kb_for_cz.add(inst)
kb_for_cz.add(textbook)
kb_for_cz.add(reading)
kb_for_cz.add(TV)
kb_for_cz.add(words)

############################# INFO FOR CZECH ################################### 
info_audio_for_cz = ''' 
1⃣) Pimsleur - Наверное лучшее аудио для уровня 🅰2 - 🅰1, когда вы хоть чуть поняли что из себя представляет язык, уроки по 20 минут, узнаете как поприветствовать, пригласить человека куда-нибудь, заказать еду в ресторане, спросить дорогу
Купить(120$) - https://www.pimsleur.com/learn-cz
Скачать с торрента - https://rutracker.org/forum/viewtopic.php?t=1215003
2⃣) Berlitz - даны озвученные диалоги и упражнения к ним в книге, также дан словарь с более чем 1000 слов и выражений. В озвученных диалогах вы найдете самые необходимые выражения и фразы. Для начального уровня, как и Пимслер, но вы должны выбрать для себя какой метод обучения вам нравится больше: Повторение в Pimsleur или задания в Berlitz
Купить - http://www.berlitzpublishing.com/en/languages/czech/
Скачать с торрента - https://rutracker.org/forum/viewtopic.php?t=2940150
3⃣) Zdeňkův český podcast - 🅰2 и выше. Чешский учитель английского ведет свой подкаст в котором говорит, один либо с друзьями, наверное обо всем, начиная от пива, стрельбы из лука заканчивая рассказами о путешествиях в другие страны. Рекомендую
https://zdenkuvceskypodcast.podbean.com/
4⃣) Český rozhlas - уровень 🅱1-🅱2. Портал, с новостями, подкастами, видео, радио. Есть такие темы как: история, политика, наука.
https://portal.rozhlas.cz/
Аудио - https://temata.rozhlas.cz/hry-a-cetba	
'''
info_yt_for_cz ='''	
1⃣) TrochuLepší - человек читает книги, и пересказывает их суть в коротких роликах, контент направлен в сторону саморазвития. Есть такие темы как: Финансовая грамотность, откуда берется хорошее настроение, как найти сильную волю и т.д
https://www.youtube.com/channel/UCPeggYc0oUjcRZJq1P08onA/featured
2⃣) metalearning_cz - похожий по направлению на TrochuLepší.
https://www.youtube.com/channel/UCb0n4wXxHMme2hTmrXcvvbg/featured
3⃣) A Cup of Style - две сестры ведут свой блог
https://www.youtube.com/user/ACupOfStyle/featured
4⃣) Show Jana Krause - подобие Вечернего Урганта
https://www.youtube.com/user/SJKshow/featured
5⃣) Prima Comedy Central - стендапы 
https://www.youtube.com/channel/UCNvom0TLEORYmo9B3XRlpcA
'''
info_inst_for_cz = '''	
1⃣) Ксения - учительница, которая первая открыла свою интернет школу по изучению Чешского(https://www.instagram.com/czech_krokosschool_prague/), в своем инстаграме, дает вам пинка для изучения чешского, полезные советы, разбирает слова. Очень полезный аккаунт
https://www.instagram.com/xeniafromczechia/
2⃣) Faktazeme - аккаунт с короткими фактами
https://instagram.com/faktazeme?igshid=64gafwa6ejd0.
'''
info_textbook_for_cz = ''' 
Сначала вам нужно решить, что вам нужно от учебника: Грамматика? Коммуникация? Или все вместе?
Грамматика:
	1⃣) Учебник чешского языка (для I и II курсов) - грамматика, и перевод на чешский.
	https://rutracker.org/forum/viewtopic.php?t=295192
	2) Communicative Czech - намного новее, нежели первый учебник. Но он на английском
	🅰1-🅰2 - https://rutracker.org/forum/viewtopic.php?t=3691450
	🅱1-🅱2 - https://rutracker.org/forum/viewtopic.php?t=3691450
	
Учебники общего назначения:
В них есть и аудирование, диалоги, грамматика, лексика:
	1⃣) Čeština Expres - Дается две книги. Приложение и Лекции
	В приложении: объяснение грамматики
	В лекциях: задания
	Čeština Expres 1 - https://rutracker.org/forum/viewtopic.php?t=4308973
	Čeština Expres 2 - https://rutracker.org/forum/viewtopic.php?t=4378387
	Čeština Expres 3 - https://rutracker.org/forum/viewtopic.php?t=5520826
	2⃣) Čeština pro cizince - 
		a. Мини-диалоги: вы слушаете, сопоставляете что услышали к картинкам, делаете задания по ним
		b. Лексика: даются нужные слова, выражения. И упражнения
		c. Диалоги: слушаете, делаете задания(вставить пропущеное слово, Правда/Ложь и т.д)
		d. Грамматика
		e. Чтение: читаете текст и выполняете задания
		f. Аудирование
		g. Произношение 
		h. Чтение: тут текст(ы) которые рассказывают историю, обычаи и т.д
	Этот учебник понравился мне больше остальных
	🅱1-🅱2 - https://rutracker.org/forum/viewtopic.php?t=5413157
'''
info_reading_for_cz = 'books' 
info_tv_for_cz = 'tv shows'
info_words_for_cz = 'words'

############################# KEYBOARD FOR ENGLISH ############################# 
kb_for_en = telebot.types.InlineKeyboardMarkup()
audio = telebot.types.InlineKeyboardButton(text = 'Аудио', callback_data = 'Audio_for_en')
YouTube = telebot.types.InlineKeyboardButton(text = 'Каналы Ютуб', callback_data = 'YT_for_en' )
inst = telebot.types.InlineKeyboardButton(text = 'Аккаунты Инстаграм', callback_data = 'Inst_for_en')
textbook = telebot.types.InlineKeyboardButton(text = 'Учебники', callback_data = 'Textbooks_for_en')
reading = telebot.types.InlineKeyboardButton(text = 'Книги', callback_data = 'Books_for_en')
TV = telebot.types.InlineKeyboardButton(text = 'Сериалы и фильмы', callback_data = 'TV_for_en')
words = telebot.types.InlineKeyboardButton(text = 'Изучение слов', callback_data = 'Words_for_en')
kb_for_en.add(audio)
kb_for_en.add(YouTube)
kb_for_en.add(inst)
kb_for_en.add(textbook)
kb_for_en.add(reading)
kb_for_en.add(TV)
kb_for_en.add(words)

############################# INFO FOR ENGLISH ################################### 
info_audio_for_en = 'audio'
info_yt_for_en ='yt'
info_inst_for_en = 'inst'
info_textbook_for_en = 'textbook'
info_reading_for_en = 'books' 
info_tv_for_en = 'tv shows'
info_words_for_en = 'words'


############################# KEYBOARD FOR ITALIAN ############################# 
kb_for_it = telebot.types.InlineKeyboardMarkup()
audio = telebot.types.InlineKeyboardButton(text = 'Аудио', callback_data = 'Audio_for_it')
YouTube = telebot.types.InlineKeyboardButton(text = 'Каналы Ютуб', callback_data = 'YT_for_it' )
inst = telebot.types.InlineKeyboardButton(text = 'Аккаунты Инстаграм', callback_data = 'Inst_for_it')
textbook = telebot.types.InlineKeyboardButton(text = 'Учебники', callback_data = 'Textbooks_for_it')
reading = telebot.types.InlineKeyboardButton(text = 'Книги', callback_data = 'Books_for_it')
TV = telebot.types.InlineKeyboardButton(text = 'Сериалы и фильмы', callback_data = 'TV_for_it')
words = telebot.types.InlineKeyboardButton(text = 'Изучение слов', callback_data = 'Words_for_it')
kb_for_it.add(audio)
kb_for_it.add(YouTube)
kb_for_it.add(inst)
kb_for_it.add(textbook)
kb_for_it.add(reading)
kb_for_it.add(TV)
kb_for_it.add(words)

############################# INFO FOR ITALIAN ################################### 
info_audio_for_it = 'audio'
info_yt_for_it ='yt'
info_inst_for_it = 'inst'
info_textbook_for_it = 'textbook'
info_reading_for_it = 'books' 
info_tv_for_it = 'tv shows'
info_words_for_it = 'words'



@bot.message_handler(commands = ['start'])

def start_message(message):
	# bot.send_message(message.chat.id, 'Привет, выбери язык')
	keyboard = telebot.types.InlineKeyboardMarkup()
	Czech = telebot.types.InlineKeyboardButton(text = 'Чешский', callback_data='Czech')
	English = telebot.types.InlineKeyboardButton(text = 'Английский', callback_data = 'English')
	Italian = telebot.types.InlineKeyboardButton(text = 'Итальянский', callback_data = 'Italian')
	keyboard.add(Czech)
	keyboard.add(English)
	keyboard.add(Italian)
  
	bot.send_message(message.chat.id, '''
		Каждый человек, который начинает учить какой-либо язык задается вопросом: "С чего начать?". Этот бот создан, чтобы постараться решить этот вопрос.Я собрал ресурсы, которые пробывал лично (В Чешском, Итальянском и Английском) и по аналогии сделал это для других языков, в надежде что это вам поможет в процессе изучения языка,и вы не будете тратить время, на то чтобы искать информацию
		А теперь, пожалуйста, выбери язык по которому хочешь найти ресурсы:
		''',
		reply_markup=keyboard)

##################### ЧЕШСКИЙ #####################



@bot.callback_query_handler(func = lambda call:True)
def Choose(call):
	if call.data == 'Czech':
		kb_for_cz = telebot.types.InlineKeyboardMarkup()
		audio = telebot.types.InlineKeyboardButton(text = 'Аудио', callback_data = 'Audio_for_cz')
		YouTube = telebot.types.InlineKeyboardButton(text = 'Каналы Ютуб', callback_data = 'YT_for_cz' )
		inst = telebot.types.InlineKeyboardButton(text = 'Аккаунты Инстаграм', callback_data = 'Inst_for_cz')
		textbook = telebot.types.InlineKeyboardButton(text = 'Учебники', callback_data = 'Textbooks_for_cz')
		reading = telebot.types.InlineKeyboardButton(text = 'Книги', callback_data = 'Books_for_cz')
		TV = telebot.types.InlineKeyboardButton(text = 'Сериалы и фильмы', callback_data = 'TV_for_cz')
		words = telebot.types.InlineKeyboardButton(text = 'Изучение слов', callback_data = 'Words_for_cz')
		kb_for_cz.add(audio)
		kb_for_cz.add(YouTube)
		kb_for_cz.add(inst)
		kb_for_cz.add(textbook)
		kb_for_cz.add(reading)
		kb_for_cz.add(TV)
		kb_for_cz.add(words)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выбери по какому направлению ты хочешь получить информацию?",reply_markup=kb_for_cz)

	if call.data =='Audio_for_cz':
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text="Назад", callback_data="Czech")
		keyboard.add(backbutton)
		bot.answer_callback_query(call.id)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = info_audio_for_cz, reply_markup=keyboard)

	if call.data =='YT_for_cz':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Czech')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_yt_for_cz, reply_markup = keyboard)

	if call.data =='Inst_for_cz':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Czech')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = info_inst_for_cz, reply_markup = keyboard)


	if call.data =='Textbooks_for_cz':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Czech')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_textbook_for_cz, reply_markup = keyboard)


	if call.data =='Books_for_cz':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Czech')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_reading_for_cz, reply_markup = keyboard)


	if call.data =='TV_for_cz':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Czech')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_tv_for_cz, reply_markup = keyboard)

	if call.data =='Words_for_cz':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Czech')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_words_for_cz, reply_markup = keyboard)

################################## ENGLISH ##################################
	if call.data == 'English':
		kb_for_en = telebot.types.InlineKeyboardMarkup()
		audio = telebot.types.InlineKeyboardButton(text = 'Аудио', callback_data = 'Audio_for_en')
		YouTube = telebot.types.InlineKeyboardButton(text = 'Каналы Ютуб', callback_data = 'YT_for_en' )
		inst = telebot.types.InlineKeyboardButton(text = 'Аккаунты Инстаграм', callback_data = 'Inst_for_en')
		textbook = telebot.types.InlineKeyboardButton(text = 'Учебники', callback_data = 'Textbooks_for_en')
		reading = telebot.types.InlineKeyboardButton(text = 'Книги', callback_data = 'Books_for_en')
		TV = telebot.types.InlineKeyboardButton(text = 'Сериалы и фильмы', callback_data = 'TV_for_en')
		words = telebot.types.InlineKeyboardButton(text = 'Изучение слов', callback_data = 'Words_for_en')
		kb_for_en.add(audio)
		kb_for_en.add(YouTube)
		kb_for_en.add(inst)
		kb_for_en.add(textbook)
		kb_for_en.add(reading)
		kb_for_en.add(TV)
		kb_for_en.add(words)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Выбери по какому направлению ты хочешь получить информацию?', reply_markup = kb_for_en)

	if call.data =='Audio_for_en':
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text="Назад", callback_data="English")
		keyboard.add(backbutton)
		bot.answer_callback_query(call.id)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = info_audio_for_en, reply_markup=keyboard)

	if call.data =='YT_for_en':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='English')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_yt_for_en, reply_markup = keyboard)

	if call.data =='Inst_for_en':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='English')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = info_inst_for_en, reply_markup = keyboard)


	if call.data =='Textbooks_for_en':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='English')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_textbook_for_en, reply_markup = keyboard)


	if call.data =='Books_for_en':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='English')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_reading_for_en, reply_markup = keyboard)


	if call.data =='TV_for_en':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='English')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_tv_for_en, reply_markup = keyboard)

	if call.data =='Words_for_en':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='English')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_words_for_en, reply_markup = keyboard)


################################## ITALIAN ##################################

	if call.data =='Italian':
		kb_for_it = telebot.types.InlineKeyboardMarkup()
		audio = telebot.types.InlineKeyboardButton(text = 'Аудио', callback_data = 'Audio_for_it')
		YouTube = telebot.types.InlineKeyboardButton(text = 'Каналы Ютуб', callback_data = 'YT_for_it' )
		inst = telebot.types.InlineKeyboardButton(text = 'Аккаунты Инстаграм', callback_data = 'Inst_for_it')
		textbook = telebot.types.InlineKeyboardButton(text = 'Учебники', callback_data = 'Textbooks_for_it')
		reading = telebot.types.InlineKeyboardButton(text = 'Книги', callback_data = 'Books_for_it')
		TV = telebot.types.InlineKeyboardButton(text = 'Сериалы и фильмы', callback_data = 'TV_for_it')
		words = telebot.types.InlineKeyboardButton(text = 'Изучение слов', callback_data = 'Words_for_it')
		kb_for_it.add(audio)
		kb_for_it.add(YouTube)
		kb_for_it.add(inst)
		kb_for_it.add(textbook)
		kb_for_it.add(reading)
		kb_for_it.add(TV)
		kb_for_it.add(words)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text = 'Выбери по какому направлению ты хочешь получить информацию?', reply_markup = kb_for_it)

	if call.data == 'Audio_for_it':
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text="Назад", callback_data="Italian")
		keyboard.add(backbutton)
		bot.answer_callback_query(call.id)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = info_audio_for_it, reply_markup=keyboard)


	if call.data == 'YT_for_it':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Italian')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_yt_for_it, reply_markup = keyboard)


	if call.data == 'Inst_for_it':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Italian')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = info_inst_for_it, reply_markup = keyboard)


	if call.data == 'Textbook_for_it':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Italian')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_textbook_for_it, reply_markup = keyboard)


	if call.data == 'Books_for_it':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Italian')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_reading_for_it, reply_markup = keyboard)


	if call.data == 'TV_for_it':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Italian')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_tv_for_it, reply_markup = keyboard)
		

	if call.data == 'Words_for_it':
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		backbutton = types.InlineKeyboardButton(text = "Назад", callback_data ='Italian')
		keyboard.add(backbutton)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,text =  info_words_for_it, reply_markup = keyboard)


bot.polling(none_stop = True)
