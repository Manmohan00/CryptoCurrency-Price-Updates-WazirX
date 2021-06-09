import requests
import json
import smtplib
from tqdm import tqdm
import time
import os


def checkPrice():
    n = requests.get("https://api.wazirx.com/api/v2/tickers")
    jn = json.loads(n.text)
    inch = float(jn["1inchinr"]["last"])##
    wrx = float(jn["wrxinr"]["last"])##
    crv = float(jn["crvinr"]["last"])##
    bat = float(jn["batinr"]["last"]) 
    uft = float(jn["uftinr"]["last"])##
    xrp = float(jn["xrpinr"]["last"]) #Ripple
    xlm = float(jn["xlminr"]["last"]) #steller
    doge = float(jn["dogeinr"]["last"])
    trx = float(jn["trxinr"]["last"]) #tron
    print("Mailing the updated prices...")
    SendMail(inch, wrx, crv, bat, uft, xrp, xlm, doge, trx);

#receivers = []

def SendMail(inch, wrx, crv, bat, uft, xrp, xlm, doge, trx):  
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("","")
    server.sendmail("",
                    "",
                    """Subject: !!Crpto Price Update!!

    1inch --> {0}
    WazirX(WRX) --> {1}
    Curve DAO Token(CRV) --> {2}
    Basic attention Token(BAT) --> {3}
    Uniled(UFT) --> {4}
    Ripple(XRP) --> {5}
    Stellar(XLM) --> {6}
    Doge --> {7}
    Tron(TRX) --> {8}""".format(str(inch),str(wrx),str(crv),str(bat),
    str(uft),str(xrp),str(xlm),str(doge),str(trx)))
    server.quit
    print("Reading out the prices for you...")
    speak(inch, crv, bat);


def speak(inch, crv, bat):
    Sinch = "./speech.sh " + "1Inch price inr {0}".format(str(inch))
    Scrv = "./speech.sh " + "Curve DAO Token price inr {0}".format(str(crv))
    Sbat = "./speech.sh " + "Basic attention Token price inr {0}".format(str(bat))
    os.system(Sinch)
    os.system(Scrv)
    os.system(Sbat)

clear = lambda: os.system('clear')
clear()
while True:
    print("Napping for 10 seconds..")
    for i in tqdm(range(0,10),ascii=False,desc="zzz",colour='magenta'):
        time.sleep(1)
    checkPrice()
    print("That's all for now")
    print("Taking a small nap now")
    print("See you on the other side!")
    time.sleep(4)
    clear()
