'''
Author: your name
Date: 2022-04-09 21:22:53
LastEditTime: 2022-04-09 21:25:51
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \HELP\lab.py
'''
import binance
client = binance.Client('ZfPdO0K6PONcxTyFSawpMkr8HkZFdI5aBBC1tmzPw8j2Tz89V2uCkC7zYMYswYvm','mZKX4SydJlEaq3NgPyKypbZWvxprzts2LB6eVeUDfXMLz490kvtcpRNmJO55dfgP')
address = client.get_deposit_address(coin='BTC')
print(f"get a deposit address for {address['coin']} address: {address['address']}")