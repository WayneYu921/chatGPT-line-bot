"""
LINE Bot 與 OpenAI GPT 聊天機器人整合
此檔案實現了一個 Flask Web 服務，用於接收來自 LINE 平台的訊息，
並使用 OpenAI GPT-3.5 模型產生回應。
"""
import openai  # 引入 OpenAI API 庫
from flask import Flask, request  # 引入 Flask Web 框架
from linebot import LineBotApi, WebhookHandler  # 引入 LINE Bot SDK
from linebot.models import TextSendMessage  # 引入 LINE 文字訊息模型
import json  # 引入 JSON 處理庫
from requests.exceptions import Timeout  # 引入超時異常處理
import os  # 引入 os 模組，用於讀取環境變數
from dotenv import load_dotenv  # 引入 dotenv 模組，用於從 .env 檔案讀取環境變數

# 載入環境變數
load_dotenv()

# 從環境變數中獲取敏感資訊
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# 初始化 Flask 應用
app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    """
    主要的 LINE Bot 處理函數，處理從 LINE 平台接收的 webhook 請求
    """
    # 從請求中獲取資料
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)  # 印出接收到的 JSON 數據，用於偵錯
    
    try:
        # 初始化 LineBotApi 和 WebhookHandler，使用環境變數
        line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
        handler = WebhookHandler(LINE_CHANNEL_SECRET)
        
        # 從請求頭中獲取簽名，用於驗證請求來源
        signature = request.headers['X-Line-Signature']
        
        # 處理請求，驗證簽名
        handler.handle(body, signature)
        
        # 從 JSON 數據中獲取回覆權杖和使用者發送的訊息
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        
        # 設置 OpenAI 的 API 金鑰，使用環境變數
        openai.api_key = OPENAI_API_KEY
        
        try:
            # 創建 ChatGPT 請求，並設置超時時間
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": msg},
                ],
                timeout=10  # 為 API 請求設置超時時間，避免等待時間過長
            )
            
            # 從回應中擷取 AI 生成的內容
            reply_msg = response['choices'][0]['message']['content']
        except Timeout:
            # 處理請求超時情況
            reply_msg = "對不起，我目前無法協助你。請稍後再試。"
        
        # 創建文字訊息物件
        text_message = TextSendMessage(text=reply_msg)
        
        # 使用 LineBotApi 回覆訊息給使用者
        line_bot_api.reply_message(tk, text_message)
        
    except Exception as e:
        # 捕獲並記錄所有其他錯誤
        print(f'發生錯誤: {e}')
    
    return 'OK'  # 回傳成功狀態碼給 LINE 平台

if __name__ == "__main__":
    # 以偵錯模式啟動 Flask 應用
    app.run(debug=True)
