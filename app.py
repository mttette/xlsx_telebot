from pyrogram import Client,filters
from pyrogram.handlers.message_handler import MessageHandler
import sheet
import data

API_ID = "17156186"
API_HASH = "c2957f899e43014b76d8df20574764c3"
BOT_TOKEN = "5901972668:AAHj1SNZ0nTDvOEAFwtqGZtOHH2s7EFQ7Z0"
ADMIN_ID = 1667320421

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH,bot_token=BOT_TOKEN)

#the obj is the data like the welcome var and the error var 
obj = data.get()

#the state is the other solition of next_step_handler
state = ";"


@app.on_message(filters.command("start")) #when someone send /start to the bot
def start(client, message):
    message.reply_text(obj["welcome"])

@app.on_message(filters.chat(ADMIN_ID) & filters.command("help")) #when the admin send /help to send the help menu
def help(client, message):
    message.reply_text("""
    اهلا بك عزيزي الادمن  🫡

    📌  اضغط /file لتغير ملف المعاملات  
    📌  اضغط /welcome لتغير الرسالة الترحيبية  
    📌  اضغط /error لتغير رسالة الخطأ

    .
    """)


@app.on_message(filters.chat(ADMIN_ID) & filters.command("file"))#when the admin want to change the xlsx file with the command /file
def upload_xlsx(client, message):
    message.reply_text("الرجاء ارسال الفايل الجديد")
    def handle_file(client,message):
        if message.document.file_name.endswith(".xlsx"):
            app.download_media(message.document.file_id, file_name="file.xlsx")
            message.reply_text("!تم")
        else:
            message.reply_text("(xlsx) يجب ان تكون صيغه الفايل")
        return sheet.get_names_from_sheet("./downloads/file.xlsx")
    app.add_handler(MessageHandler(handle_file,filters=filters.chat(ADMIN_ID) & filters.document))


@app.on_message(filters.chat(ADMIN_ID) & filters.command("welcome"))#when the admin want to change the welcome message
def edit_welcome(client,message):
    global state
    message.reply_text("الرجاء ارسال الرسالة الترحيبية الجديدة")
    state = str(message.chat.id)+";welcome"



@app.on_message(filters.chat(ADMIN_ID & filters.command("error")))#when the admin want to change the error message
def edit_error(client,message):
    global state
    message.reply_text("الرجاء ارسال رسالة الخطأ الجديدة")
    state = str(message.chat.id)+";error"


@app.on_message(filters.text)# when the bot get any text message 
def handle_message(client, message):
    check_state(state,message)# this func with check for the state 

def new_welcome(message):
    # this function edit the welcome message 
    # when he send it
    global state
    obj["welcome"] = message.text
    data.set(obj)
    message.reply_text("!تم")
    #make state back to " ; "(the defalt looking)
    state = " ; "
        

def new_error(message):
    # this function edit the error message 
    # when he send it
    global state
    obj["error"] = message.text
    data.set(obj)
    message.reply_text("!تم")
    #make state back to " ; "(the defalt looking)
    state = " ; "

def check_state(state,message):# this func with check the state
    state = state.split(";")
    id = state[0]
    state = state[1]
    if state == "welcome" and str(message.chat.id) == id:
        return new_welcome(message)
    elif state == "error" and str(message.chat.id) == id:
        return new_error(message)
    else:
        return message.reply_text(sheet.search_name(message.text,
    names=sheet.get_names_from_sheet()["names"],
    sheet=sheet.get_names_from_sheet()["sheet"],
    error_reply=obj["error"]
    ))
    


    
app.run()#this one run the app