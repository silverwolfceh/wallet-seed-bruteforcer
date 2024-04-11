import requests

def init_telegram(token, chatid):
	try:
		url=f"https://api.telegram.org/bot{token}/sendMessage"
		requests.get(url, params = {"chat_id": chatid,"text": "Telegram connect successfully"})
	except Exception as e:
		print(e)

def send_found(wq, token, chatid, w, coin, bl):
	wq.put(f"{w} | {coin} | {bl}")
	if token is not None and token != "":
		data= f"I found it : {w} | {coin} | {bl}"
		url=f"https://api.telegram.org/bot{token}/sendMessage"
		requests.get(url, params = {"chat_id": chatid,"text":data})