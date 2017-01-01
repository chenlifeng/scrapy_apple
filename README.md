# Scrapy  
## 簡介  
[Scrapy] (https://scrapy.org/)是一個網路爬蟲的架構。它定義了許多流程，包含網頁的爬取、資料的處理及儲存，  
並且它使用了Twitsted的非同步框架，可以較快速的去剖析網頁。  
## 安裝  
我的安裝方法是  
1.先下載 [Anaconda](https://www.continuum.io/downloads) 這個python的資料處理平台  
2.接著在Anaconda Prompt中安裝Scrapy: pip install scrapy 即可  
## 架構  
![Scrapy architecture] (https://doc.scrapy.org/en/latest/_images/scrapy_architecture_02.png)  
### Scrapy engine：  
Scrapy engine是用來控制整個系統的數據處理流程，並進行事務處理的觸發。  
### Scheduler：  
scheduler負責排程，scheduler會在scrapy engine發出請求後進行enqueue的動作，並在排序完後return給scrapy engine。  
### Downloader:   
downloader的主要職責是抓取網頁並將網頁內容return給scrapy engine(之後再return給spider)。  
### Spiders：  
spiders讓user自己定義用來解析網頁並抓取、制定URL返回的內容的方法。換句話說就是用來定義特定網站的抓取和解析規則。   
1.spider首先透過start_requests()函式默認從start_urls中的url中生成請求，並呼叫parse()作為callback function  
2.在parse()中，你可以利用不同的selector去parse網頁並返回項目對象和請求對像。這些請求也將包含一個callback，然後被Scrapy下載，並有指定的callback。  
3.最後，從spider返回的項目會進到item pipelines。  
### Item Pipeline：item pipelines負責處理spider從網頁中parse完的item，它的主要任務是萃取、驗證和存儲數據。
 
