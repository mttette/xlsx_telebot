from pyrogram import Client,filters,types
import sheet


API_ID = "17156186"
API_HASH = "c2957f899e43014b76d8df20574764c3"
BOT_TOKEN = "5901972668:AAHj1SNZ0nTDvOEAFwtqGZtOHH2s7EFQ7Z0"


app = Client("my_bot", api_id=API_ID, api_hash=API_HASH,bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("اهلا وسهلا, ما هو اسمك الكامل(الثلاثي)؟")

@app.on_message(filters.text)
def handle_message(client, message):
    message.reply_text(sheet.search_name(message.text))

# @app.on_message(filters.document)
# def test(client,message):
#     types.Document().file_name
#     message.reply_text("good job")
    
app.run()


#TODO 

# make command(help) that show admin commands 
# make an admin page that let the admin change
# 1.the file 
# 2.the welcome message
# 3.the qustion? message
# 4.the erorr message 
