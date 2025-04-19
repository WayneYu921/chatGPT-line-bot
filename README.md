# LINE Bot GPT - 智能聊天機器人整合方案

一個基於 LINE Messaging API 和 OpenAI GPT-3.5 的聊天機器人解決方案，讓使用者能夠透過 LINE 應用程式與 AI 智能助手交流。

## 技術棧概覽

- **後端框架**: Flask (Python)
- **AI 技術**: OpenAI GPT-3.5 Turbo
- **通訊平台**: LINE Messaging API
- **部署方式**: Docker 容器化
- **伺服器**: Gunicorn WSGI HTTP Server
- **環境變數管理**: python-dotenv

## 主要功能

- 接收來自 LINE 平台的用戶訊息
- 將訊息傳遞給 OpenAI GPT-3.5 模型處理
- 處理 API 請求超時情況
- 將 AI 生成的回應傳回 LINE 平台
- 錯誤處理與日誌記錄

## 技術亮點

1. **無縫整合**: 完美結合 LINE Messaging API 與 OpenAI API，創造流暢的用戶體驗
2. **穩健錯誤處理**: 實現請求超時處理和異常捕捉，確保系統穩定性
3. **容器化部署**: 使用 Docker 封裝應用程式，便於跨平台部署和擴展
4. **簡潔高效的代碼**: 遵循 Python 最佳實踐，程式碼結構清晰，便於維護
5. **安全性考量**: 透過環境變數管理敏感資訊，避免敏感資訊外洩

## 快速啟動

### 必要條件

- Python 3.8+
- LINE 開發者帳號與 Messaging API Channel
- OpenAI API 金鑰

### 安裝與運行

1. 克隆儲存庫:
   ```
   git clone <儲存庫網址>
   cd chatGPT-line-bot
   ```

2. 安裝依賴:
   ```
   pip install -r requirements.txt
   ```

3. 設定環境變數:
   ```
   cp .env.example .env
   ```
   然後編輯 `.env` 檔案，填入您的 API 金鑰和密鑰:
   ```
   LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
   LINE_CHANNEL_SECRET=your_line_channel_secret
   OPENAI_API_KEY=your_openai_api_key
   ```

4. 啟動應用:
   ```
   python line-bot.py
   ```

### 使用 Docker 運行

1. 設定環境變數 (同上方步驟 3)

2. 構建並運行 Docker 容器:
   ```
   docker build -t line-bot-gpt .
   docker run --env-file .env -p 5000:5000 line-bot-gpt
   ```

## 系統架構

```
用戶 (LINE App) <--> LINE Platform <--> Flask Web 服務 <--> OpenAI GPT API
```

## 安全性注意事項

- **敏感資訊處理**: 所有 API 金鑰和密鑰皆透過環境變數管理，避免硬編碼在程式碼中
- **環境變數檔案**: `.env` 檔案已被加入 `.gitignore` 中，不會被上傳到版本控制系統
- **範本提供**: 專案提供 `.env.example` 作為範本，說明需要設置的環境變數

## 未來改進方向

- 實現對話上下文維護，提升對話連貫性
- 增加更多 LINE 功能支援，如圖片分析、多媒體回應等
- 優化令牌使用效率，降低 API 成本
- 增加用戶身份驗證與個人化回應功能

---

*此專案展示了我在 API 整合、雲端服務、自然語言處理和後端開發方面的技能，並體現了我能夠設計和實現實用且可擴展的解決方案的能力。*
