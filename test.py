import requests

token = "igrgeRUTnr6PSNkLmMfY2RIV0D3BDcdVibYqkx/UDwakdUcCUWpt8Es7r8poEyPi+Rp7L1Xh1dunbzd2ofMPPaB1oBJvCsNCs36j/PMEzEsiWhdeqjaa/5nwt3iEvAaaWrLzEEchP/BKY4lOWE/9xQdB04t89/1O/w1cDnyilFU="

def LineNotify(token,message):
   line_notify_token = token
   line_notify_api = 'https://notify-api.line.me/api/notify'
   payload = {'message': message}
   headers = {'Authorization': 'Bearer ' + line_notify_token} 
   requests.post(line_notify_api, data=payload, headers=headers)

LineNotify(token,"これはテスト送信です")
