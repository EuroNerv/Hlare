import datetime
import requests

mode = {
    "day" : False,
}

token = "igrgeRUTnr6PSNkLmMfY2RIV0D3BDcdVibYqkx/UDwakdUcCUWpt8Es7r8poEyPi+Rp7L1Xh1dunbzd2ofMPPaB1oBJvCsNCs36j/PMEzEsiWhdeqjaa/5nwt3iEvAaaWrLzEEchP/BKY4lOWE/9xQdB04t89/1O/w1cDnyilFU="

def LineNotify(token,message):
   line_notify_token = token
   line_notify_api = 'https://notify-api.line.me/api/notify'
   payload = {'message': message}
   headers = {'Authorization': 'Bearer ' + line_notify_token} 
   requests.post(line_notify_api, data=payload, headers=headers)

def center():
    time = datetime.datetime.now()
    if time.hour == 0:
       if mode["day"] != True:
          mode["day"] = True
          yea = time.year
          mont = time.month
          today = time.day
          dtA = datetime.datetime(yea,mont,today)
          dtB = datetime.datetime(2020,1,18)
          theday = dtB - dtA
          num = theday.days
          message = "\n日付が変わりました\n今日は" + str(mont) + "月" + str(today) + "日です\nセンター試験まで残り" + str(num) + "日です。合格目指して頑張りましょう"
          LineNotify(token,message)
    if time.hour == 8:
       if mode["day"] == True:
          mode["day"] = False
    if time.hour == 10:
       if mode["day"] == True:
          mode["day"] = False
while True:
 center()
