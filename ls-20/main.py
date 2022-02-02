#5255231520:AAEZ4M0RoDQfFD0vA9mRKX1j793sZ2o9r74
import telebot

bot = telebot.TeleBot("5255231520:AAEZ4M0RoDQfFD0vA9mRKX1j793sZ2o9r74")
#UserAge
#UserName
#UserSurname
#UserPet
#UserEducation 
#Citizenship
#Gender
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	if message.text=='/help':
		bot.reply_to(message, "So, how can i help you?")
	elif message.text=='/start':
		bot.reply_to(message, "Interview started!!")
		bot.reply_to(message, "Tell us about yourself?")
		


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "Hellow":
        bot.reply_to(message, "Haw are you?")	 
    elif message.text == "Iam fine":
        bot.reply_to(message, "Cats or dogs ?")
    elif message.text == "Cats":
	    bot.reply_to(message, 'This is good. Coffee or tea')    
    elif message.text == "Dogs":
        bot.reply_to(message, "Nice to know. Coffee or tea")
    elif message.text == "Coffee":
	    bot.reply_to(message, 'This is good. Pc or mobile games?')  
    elif message.text == "Tea":
        bot.reply_to(message, "Nice to know. Pc or mobile games?")
    elif message.text == "Pc":
	    bot.reply_to(message, 'This is good.')  
    elif message.text == "Mobile":
        bot.reply_to(message, "Nice to know.")
    elif message.text == "Yes":
	    bot.reply_to(message, 'This is good.')  
    elif message.text == "No":
        bot.reply_to(message, "Nice to know.")
    else:
        bot.reply_to(message, "Can you repeat?")


		
			
	#bot.reply_to(message, message.text)
bot.infinity_polling()
