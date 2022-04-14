
import csv
path = 'myorderbook.csv'
def setorder(flat,time,quil,price,pair,way):
    flatsing=1 if flat != "flat" else 0
    with open(path,'a+',newline='') as csvfile:
        weiter = csv.writer(csvfile)
        weiter.writerow([flatsing,time,quil*price,pair,way])
def count_profit_or_loss():   
    
    with open(path,'r',newline='') as csvfile:
        rows=csv.reader(csvfile)
        totprofit=0
        temp=0
        for t in rows:
            if int(t[0]):temp=int(t[2])
            else:totprofit=totprofit+abs(temp-int(t[2]))
        
    return "總損益:" + str(totprofit) + "    "
'''
setbuyorder(1,'0414',1,12,'APEUSDT','BUY') #新增buyorder(price,count)
setbuyorder(0,'0414',1,13,'APEUSDT','SELL')#新增sellorder(price,count)
setbuyorder(1,'0414',1,14,'APEUSDT','BUY') 
setbuyorder(0,'0414',1,15,'APEUSDT','SELL') 
print(count_profit_or_loss())#計算損益
'''