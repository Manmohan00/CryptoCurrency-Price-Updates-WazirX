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
    kmd = float(jn["kmdinr"]["last"]) #Komodo
    ctsi = float(jn["ctsiinr"]["last"])#Cartesi
    push = float(jn["pushinr"]["last"])
    ark = float(jn["arkinr"]["last"])
    print("Mailing the updated prices...")
    SendMail(inch, wrx, crv, bat, uft, xrp, xlm, doge, trx, kmd,ctsi,
    push, ark);

receivers = []

def SendMail(inch, wrx, crv, bat, uft, xrp, xlm, doge, trx, kmd, ctsi,
push, ark):  
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("","")
    server.sendmail("",
                    receivers,
                    """Subject: !!Crpto Price Update!!

    1inch --> {0}
    
    WazirX(WRX) --> {1}
    
    Curve DAO Token(CRV) --> {2}
    
    Basic attention Token(BAT) --> {3}
    
    Uniled(UFT) --> {4}
    
    Ripple(XRP) --> {5}
    
    Stellar(XLM) --> {6}
    
    Doge --> {7}
    
    Tron(TRX) --> {8}
    
    Komodo(KMD) --> {9}
    
    Cartesi(CTSI) --> {10}
    
    PUSH --> {11}
    
    ARK --> {12}
    **Delete this email after reading**""".format(str(inch),str(wrx),str(crv),str(bat),
    str(uft),str(xrp),str(xlm),str(doge),str(trx),str(kmd), str(ctsi),
    str(push), str(ark)))
    server.quit

clear = lambda: os.system('clear')
clear()
while True:
    try:
        print("Napping for 30 minutes..")
        for i in tqdm(range(0,1800),ascii=False,desc="zzz",colour='magenta'):
            time.sleep(1)
        checkPrice()
        print("That's all for now")
        print("Taking half an hour nap now")
        print("See you on the other side!")
        time.sleep(4)
        clear()
    except:
        print("Skipping of this time...")
