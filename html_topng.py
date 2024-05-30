from selenium import webdriver

# ブラウザを開く
driver = webdriver.Chrome()

# HTMLページを開く
driver.get("file:///C:/Users/takah/investigate/plot_map.html")

# スクリーンショットを取得してPNG画像として保存
driver.save_screenshot("screenshot.png")

# ブラウザを閉じる
driver.quit()
