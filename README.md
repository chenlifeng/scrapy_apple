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
1.spider首先透過start_requests()函式默認從start_urls中的url中生成請求，並呼叫parse()作為callback function。  
2.在parse()中，你可以利用不同的selector去parse網頁並返回項目對象和請求對像。這些請求也將包含一個callback，然後被Scrapy下載，並有指定的callback。  
3.最後，從spider返回的項目會進到item pipelines。  
### Item Pipeline： 
item pipelines負責處理spider從網頁中parse完的item，它的主要任務是萃取、驗證和存儲數據。  
### 數據處理流程：  
數據處理流程如圖中標示的數字 (詳細流程可以點[這裡] (https://doc.scrapy.org/en/latest/topics/architecture.html))  
## Command Line Tool  
在這邊簡單介紹幾個常用的command line指令：  
1.scrapy startproject applenews (創建一個名為applenews的project)  
2.scrapy crawl applenews (執行applenews這個spider，spider的名稱定義在crawl.py中的name變數中)  
3.scrapy crawl applenews -o applenews.json -t json (執行applenews這個spider，並將抓取到的資料輸出成json檔存入applenews.json中)  
4.scrapy genspider mydomain mydomain.com (新增名為mydomain的spider)  
5.scrapy fetch "url" (利用downloader下載指定的url)  
6.scrapy parse "url" --spider=applenews 利用applenews這個spider去parse某個url網址  
7.scrapy -h (察看更多的scrapy相關指令)  
## Selectors  
Scrapy提供了XPath和CSS兩個selector  
關於XPath下面提供幾個簡單的用法：  
/html/head/title:選擇HTML文檔中head標籤內的title元素  
/html/head/title/text():選擇上面提到的title元素的文字  
//td:選擇所有的td元素    
//div[@class="mine"]:選擇所有具有class="mine"屬性的div元素    
另外除了這兩個selectors也可以使用BeautifulSoup或其他的library  
關於Scrapy的詳細selector教學可以點[這裡] (https://doc.scrapy.org/en/0.20/topics/selectors.html)  
## Project架構  
items.py：可以透過撰寫items.py去定義parse完資料的欄位(數據性的結構方便處理 類似dictionary)  
settings.py：定義project的設定  
pipelines.py：可以透過撰寫pipelines.py去清理網頁資料、驗證抓取資料、去重覆化、將資料儲存至資料庫  
crawler.py；此為主要撰寫的python檔案  
