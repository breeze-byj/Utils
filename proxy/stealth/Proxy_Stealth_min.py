# 解决selenium 白屏反爬
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


options = Options()
driver = Chrome(options=options)
with open('stealth.min.js') as f:
    js = f.read()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})
driver.get('https://')




