import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
import os
load_dotenv()
# Replace with your actual API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN =os.getenv("TELEGRAM_BOT_TOKEN")
# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get AI response
def get_gemini_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Handle user messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = get_gemini_response(user_message)
    await update.message.reply_text(response)

# Start the bot
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()


