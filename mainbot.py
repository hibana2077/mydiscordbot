'''
Author: your name
Date: 2022-04-09 21:03:33
LastEditTime: 2022-04-14 22:46:17
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \HELP\price.py
'''
#導入 passwd.py
import requests,discord,json,ccxt,binance,passwd,requests,datetime,countprofit,csv
#client 是我們與 Discord 連結的橋樑
client = discord.Client()
binclient = binance.Client(passwd.API_KEY,passwd.API_SECRET)
require = ['BTC','ETH']
payload={}
headers = {
  'Content-Type': 'application/json'
}

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    if message.content.startswith('price'):
        
        if len(message.content.split(" ")) == 2:
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + message.content.split(" ")[1].upper() + "USDT"
            response = requests.request("GET", url, headers=headers, data=payload)
            pos = response.text.index("lastPrice") + 12     
            await message.channel.send(message.content.split(" ")[1].upper() + "價格為:" + response.text[pos:pos+8]+" USDT")
        else:    
         i = 0
         await message.channel.send('現貨價格為')
         while i < len(require):
           url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + require[i] + "USDT"
           response = requests.request("GET", url, headers=headers, data=payload)
           pos = response.text.index("lastPrice") + 12     
           await message.channel.send(require[i] + ":" + response.text[pos:pos+8])
           i = i + 1
    if message.content.startswith('fprice'):
        
        if len(message.content.split(" ")) == 2:
            url = "https://fapi.binance.com/fapi/v1/premiumIndex?symbol=" + message.content.split(" ")[1].upper() + "USDT"
            response = requests.request("GET", url, headers=headers, data=payload)
            pos = response.text.index("markPrice") + 12     
            await message.channel.send(message.content.split(" ")[1].upper() + "標記價格為:" + response.text[pos:pos+8]+" USDT")
        else:    
         i = 0
         await message.channel.send('標記價格為')
         while i < len(require):
           url = "https://fapi.binance.com/fapi/v1/premiumIndex?symbol=" + require[i] + "USDT"
           response = requests.request("GET", url, headers=headers, data=payload)
           pos = response.text.index("markPrice") + 12     
           await message.channel.send(require[i] + ":" + response.text[pos:pos+8])
           i = i + 1
    if message.content.startswith('binprice'):
        if len(message.content.split(" ")) == 2:
            price,coin=binclient.get_all_tickers(),message.content.split(" ")[1].upper()
            for t in price:
                if t['symbol']==coin:await message.channel.send(message.content.split(" ")[1].upper() + "價格為:" + t['price']+"USDT")
        else:await message.channel.send('請輸入幣種名稱 EX:APEUSDT')

    if message.content.startswith('bindeposit'):
        if len(message.content.split(" ")) == 2:
            address = binclient.get_deposit_address(coin=message.content.split(" ")[1].upper())
            await message.channel.send(message.content.split(" ")[1].upper() + "存款地址為:" +address['address'])
        else:await message.channel.send('請輸入要存款的幣種')

    if message.content.startswith('binwithdraws'):
        if len(message.content.split(" ")) == 2:
            wi = binclient.get_withdraw_history(coin=message.content.split(" ")[1].upper())
            if len(wi)!=0:
                for t in range(1):
                    await message.channel.send(message.content.split(" ")[1].upper() + "存款地址為:" +str(wi[1]))
        else:await message.channel.send('沒有提款紀錄將不會顯示')
    
    if message.content.startswith('MCserver'):
        await message.channel.send('https://web.nttu.edu.tw/s31/MinecraftServer/server.php')

    if message.content.startswith('MCbuild'):
        await message.channel.send('https://youtu.be/uldhfEZydTo')
    
    if message.content.startswith('TTweather'):
        r=requests.get('https://data.epa.gov.tw/api/v2/aqx_p_249?api_key=a5e87e8e-043a-4724-98e6-4bc3e547e83b', verify=False)
        for t in range(6):
            await message.channel.send(f"時間{datetime.date.today()}:{r.json()['records'][t]['sitename']}的{r.json()['records'][t]['itemengname']}為 {r.json()['records'][t]['concentration']} {r.json()['records'][t]['itemunit']}")

    if message.content.startswith('date'):
        await message.channel.send(f"現在時間:{datetime.date.today()}")

    if message.content.startswith('講中文拉幹!'):
        await message.channel.send(f"我幹你娘機掰!沒被幹過是不是!")

    if message.content.startswith('python Docs'):
        await message.channel.send(f"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png")
        await message.channel.send(f"https://docs.python.org/3/")

    if message.content.startswith('cpp Docs'):
        await message.channel.send(f"https://pic.vsixhub.com/35/5d/b4f78906-078e-4ba3-88ef-02999a9bb4b7-logo.png")
        await message.channel.send(f"https://en.cppreference.com/w/")

    if message.content.startswith('UVI'):
        r=requests.get('https://data.epa.gov.tw/api/v2/uv_s_01?api_key=a5e87e8e-043a-4724-98e6-4bc3e547e83b', verify=False)
        for t in range(34):await message.channel.send(f"地點:{r.json()['records'][t]['sitename']} UV:{r.json()['records'][t]['uvi']} 時間:{r.json()['records'][t]['publishtime']}")
    
    if message.content.startswith('binfuex') and message.content.split()[1]!="test":#非常重要的部分 考慮挖出來做?
        try:
            qu=float(message.content.split()[3])
            order=binclient.futures_create_order(symbol=message.content.split()[1],side=message.content.split()[2].upper(),type="MARKET",quantity=int(qu))
            await message.channel.send(f"下單 {order['symbol']} 狀態{order['status']} 方向{order['side']} ")
        except Exception as e:await message.channel.send(e.message, "error")
    
    if message.content.startswith('binasset'):
        asetname=message.content.split()[1]
        await message.channel.send(f"資產項目:{binclient.get_asset_balance(asset=asetname)['asset']} 可用: {binclient.get_asset_balance(asset=asetname)['free']} 不可用: {binclient.get_asset_balance(asset=asetname)['locked']}")

    if message.content.startswith('binleverange'):
        coinname,lv=message.content.split()[1],int(message.content.split()[2])
        case=binclient.futures_change_leverage(symbol=coinname,leverage=lv)
        await message.channel.send(f"更改 {case['symbol']} 的槓桿為 {case['leverage']} 倍，最大名義值為 {case['maxNotionalValue']} USDT。")
    
    if message.content.startswith('testbinorder'):
        try:
            qu=float(message.content.split()[3])
            countprofit.setorder(message.content.split()[4],message.content.split()[5],int(qu),float(message.content.split()[6]),message.content.split()[1],message.content.split()[2])
            await message.channel.send(f"測試下單成功")
        except Exception as e:await message.channel.send(e.message, "error")

    if message.content.startswith('binleverange'):
        await message.channel.send(countprofit.count_profit_or_loss())
    
client.run(passwd.API_DISCORD_TOKEN) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
