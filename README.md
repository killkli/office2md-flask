# Office 檔案轉 Markdown 轉換器

這個專案是一個用 Flask 寫的網頁應用程式，可以把你的 Office 檔案 (xlsx、xls、docx、pptx、pdf) 轉成 Markdown 格式。我們使用了 `markitdown` 這個套件，讓整個程式碼簡潔好用，也方便部署。

## 功能特色

- **檔案轉檔：** 支援常見的 Office 檔案格式轉換成 Markdown，讓你輕鬆處理文件。
- **Docker 容器化：** 內建 `Dockerfile` 和 `docker-compose.yaml`，讓你用 Docker 一鍵部署，輕鬆上線。我們用了兩階段建置，讓 Docker 映像檔更小、建置速度更快。
- **輸入驗證：** 會檢查檔案類型和大小，避免錯誤發生，讓轉換過程更穩定。
- **友善介面：** 網頁介面簡單易用，就算不熟悉程式碼也能輕鬆操作。
- **下載結果：** 轉換完成後，可以直接下載轉換好的 Markdown 檔案。
- **錯誤處理：** 程式碼有完善的錯誤處理機制，就算遇到問題也能優雅地處理，不會當掉。
- **Gunicorn 部署：** 適合用 Gunicorn 部署到生產環境，效能更好。

## 開始使用

1. **複製程式碼：** `git clone <repository_url>`
2. **建置 Docker 映像檔：** `docker-compose build`
3. **執行應用程式：** `docker-compose up`
4. **開啟網頁：** 在瀏覽器輸入 `http://localhost:5000` 就可以開始使用了！

## 相依套件

- Flask
- markitdown
- Gunicorn (生產環境用)
- 其他相依套件請參考 `requirements.txt`

## 授權條款

這個專案採用 MIT 授權，詳細內容請參考 [LICENSE](LICENSE) 檔案。
