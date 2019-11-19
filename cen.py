from bs4 import BeautifulSoup
import datetime
import requests

mode = {
    "0" : False,
    "6" : False,
}

print("system start")
#_____token_____#
token = "igrgeRUTnr6PSNkLmMfY2RIV0D3BDcdVibYqkx/UDwakdUcCUWpt8Es7r8poEyPi+Rp7L1Xh1dunbzd2ofMPPaB1oBJvCsNCs36j/PMEzEsiWhdeqjaa/5nwt3iEvAaaWrLzEEchP/BKY4lOWE/9xQdB04t89/1O/w1cDnyilFU="

#_____def_____#
def LineNotify(token,message):
   line_notify_token = token
   line_notify_api = 'https://notify-api.line.me/api/notify'
   payload = {'message': message}
   headers = {'Authorization': 'Bearer ' + line_notify_token} 
   requests.post(line_notify_api, data=payload, headers=headers)
def count():
  time = datetime.datetime.now()
  yea = time.year
  mont = time.month
  today = time.day
  dtA = datetime.datetime(yea,mont,today)
  dtB = datetime.datetime(2020,1,18)
  theday = dtB - dtA
  num = theday.days
  message = "\n日付が変わりました\n今日は" + str(mont) + "月" + str(today) + "日です\nセンター試験まで残り" + str(num) + "日です。"
  return message
def getWeather():
    url = "https://tenki.jp/lite/forecast/3/16/4410/13113/"
    r = requests.get(url)
    bsObj = BeautifulSoup(r.content, "html.parser")
    we = bsObj.find(class_="weather-telop")
    weth = we.get_text()
    hig = bsObj.find(class_="high-temp temp")
    high = hig.get_text()
    lo = bsObj.find(class_="low-temp temp")
    low = lo.get_text()
    if "雨" in weth:
        unb = "必要"
    else:
        unb = "不要"
    mess = "天気:" + weth + "\n最高気温:" + str(high) + "\n最低気温:" + str(low) + "\n傘:" + unb
    return mess
def main():
 try:
    time = datetime.datetime.now()
    if time.hour == 0:
     if time.minute == 0:
       if mode["0"] != True:
          mode["0"] = True
          message = count()
          LineNotify(token,message)
    if time.hour == 6:
       if mode["6"] != True:
          mode["6"] = True
          message = "\nおはようございます。\n6時になったので今日の天気をお知らせします。\n" + getWeather() + "\n今日も一日がんばりましょう"
          LineNotify(token,message)
    if time.hour == 8:
       if mode["0"] == True:
          mode["0"] = False
       if mode["6"] == True:
          mode["6"] = False
    if time.hour == 10:
       if mode["0"] == True:
          mode["0"] = False
       if mode["6"] == True:
          mode["6"] = False
 except Exception as e:
  print(str(e))
while True:
 main()
