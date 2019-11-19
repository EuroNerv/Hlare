#coding:UTF-8
import requests

def main():
    url = "https://notify-api.line.me/api/notify"
    token = "igrgeRUTnr6PSNkLmMfY2RIV0D3BDcdVibYqkx/UDwakdUcCUWpt8Es7r8poEyPi+Rp7L1Xh1dunbzd2ofMPPaB1oBJvCsNCs36j/PMEzEsiWhdeqjaa/5nwt3iEvAaaWrLzEEchP/BKY4lOWE/9xQdB04t89/1O/w1cDnyilFU="
    headers = {"Authorization" : "Bearer "+ token}

    message = 'message送信！'
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
