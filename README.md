# TradingView Strategy Auto Trading Bot (使用TradingView上的策略來進行自動化交易)
這是一個透過Discord、TradingView、幣安來達成的自動交易機器人。
<h1>目的</h1>
在網路上看到許多影片，但是大部分的影片都很複雜，於是就自己動手做一個自動交易機器人。
<h1>使用到的技術</h1>
Python</br>
API</br>
webhook</br>
Discord</br>

*Azure VM*</br>
*Linux*

<h1>參考資料</h1>

* [自動交易機器人](https://github.com/blockplusim/crypto_trading_service_for_tradingview)</br>

* [很猛的外國人做的交易機器人](https://github.com/hackingthemarkets/tradingview-binance-strategy-alert-webhook)</br>

* [python-binance包的說明文件](https://python-binance.readthedocs.io/en/latest/)</br>

* [binance的說明文件](https://binance-docs.github.io/apidocs/spot/cn/#45fa4e00db)</br>

* [python-binance API Error code](https://github.com/binance/binance-spot-api-docs/blob/master/errors.md)</br>


<h1>先備條件</h1>
一台電腦</br>
VScode</br>
Discord帳號</br>
Binance帳號</br>
TradingView Pro帳號</br>


<h1>帳號註冊</h1>

* [幣安註冊](https://www.binance.com/zh-TW/activity/referral/offers/claim?ref=CPA_00JTV45LM5)</br>

* [Discord註冊](https://discord.com/)</br>

* [TradingView 註冊](https://tw.tradingview.com/gopro/?share_your_love=hibana2077)</br>

<h1>開始</h1>
先去下載Python，如果已經安裝了可以跳過這一段。</br>

* [下載Python](https://www.python.org/downloads/)</br>

![](img/download-Python.png)

![](img/click.png)

![](img/click2.png)

![](img/click3.png)

![](img/click4.png)

重新開機，接著按照下圖流程走。

![](img/cmd3.png)

![](img/cmd2.png)

下載地點選一個你開心的地方就好。

解壓縮後，以VScode開啟。

![](img/file.png)

![](img/file1.png)

![](img/passwd.png)

![](img/passwd1.png)

![](img/passwd2.png)

![](img/passwd3.png)

![](img/passwd4.png)

然後依序填進去passwd.py即可，再按下ctrl+s。</br>
在下載下來的地方開啟終端機，輸入python mainbot.py。</br>
到這邊就建置完成了。</br>
然後把機器人加入到你個人的DC伺服器。</br>
再去DC設定好webhook機器人和去TV載入策略。</br>
並且建立警報。</br>
警報內容填入</br>
<strong>{"content":"binfuex {{ticker}} {{strategy.order.action}} {{strategy.order.contracts}} {{strategy.market_position}} {{timenow}} {{strategy.order.price}}"}</strong>
</br>這個是下單的指令，訂單數量需要在TV裡面改。

