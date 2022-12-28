from pyrogram import Client,filters
import sheet

API_ID = "17156186"
API_HASH = "c2957f899e43014b76d8df20574764c3"
BOT_TOKEN = "5901972668:AAHj1SNZ0nTDvOEAFwtqGZtOHH2s7EFQ7Z0"

admin_id = 1667320421

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH,bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("""
    اهلا وسهلا بك في بوت المعاملات 

    ما هو اسمك الثلاثي ؟
    """)

@app.on_message(filters.chat(admin_id) & filters.command("help"))
def help(client, message):
    message.reply_text("""
    اهلا بك عزيزي الادمن  🫡

    📌  اضغط /file لتغير ملف المعاملات  
    📌  اضغط /welcome لتغير الرسالة الترحيبية  
    📌  اضغط /error لتغير رسالة الخطأ

    .
    """)

current_state = ""
@app.on_message(filters.chat(admin_id) & filters.command("file"))
def upload_xlsx(client, message):
    global current_state
    message.reply_text("الرجاء ارسال الفايل الجديد")
    current_state = "waiting"
@app.on_message(filters.chat(admin_id) & filters.document)
def handle_file(client,message):
    global current_state
    if current_state == "waiting":
        if message.document.file_name.endswith(".xlsx"):
            app.download_media(message.document.file_id, file_name="file.xlsx")
            message.reply_text("!تم")
        else:
            message.reply_text("(xlsx) يجب ان تكون صيغه الفايل")
        current_state = ""
        return sheet.get_names_from_sheet("./downloads/file.xlsx")



@app.on_message(filters.text)
def handle_message(client, message):
    message.reply_text(sheet.search_name(message.text,
    names=sheet.get_names_from_sheet()["names"],
    sheet=sheet.get_names_from_sheet()["sheet"]
    ))

    
app.run()


#TODO 

# (done) make command(help) that show admin commands
# (done)make an admin page that let the admin change
# 1.the file 
# 2.the welcome message
# 3.the qustion? message
# 4.the error message 
