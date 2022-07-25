from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,ReplyKeyboardMarkup



bntCreat = InlineKeyboardButton('👨‍🎓 Создатель бота', url='t.me/sisosoakakqladjM')
bntInfo = InlineKeyboardButton('👨‍💻 Мой профиль', callback_data = 'button1')
btnTime = InlineKeyboardButton('⏳ Дата и время', callback_data = 'time1')
bntRandom = InlineKeyboardButton('🎲 Рандомное число', callback_data = 'bntRandom1') 
back = InlineKeyboardButton("🔙 Назад", callback_data = 'back1')
backinline = InlineKeyboardMarkup().add(back)
mainMenu1 = InlineKeyboardMarkup().add(bntCreat, bntInfo, btnTime,bntRandom)

