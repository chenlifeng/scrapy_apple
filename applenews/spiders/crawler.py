import scrapy
from bs4 import BeautifulSoup
from applenews.items import ApplenewsItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ApplenewsCrawler(CrawlSpider):
	name = 'applenews'
	start_urls = ["http://www.appledaily.com.tw/realtimenews/section/new/"]
	rules = [
		Rule(LinkExtractor(allow=('/realtimenews/section/new/[1-10]$')), callback='parse_list', follow=True)
	]
	def parse_list(self, response):
		domain = 'http://www.appledaily.com.tw'
		res = BeautifulSoup(response.body)
		for news in res.select('.rtddt'):
			yield scrapy.Request(domain + news.select('a')[0]['href'], self.parse_detail)

	def parse_detail(self, response):
		res = BeautifulSoup(response.body)
		applenews_item = ApplenewsItem()
		applenews_item['title'] = res.select('#h1')[0].text
		applenews_item['content'] = res.select('#summary')[0].text
		applenews_item['time'] = res.select('.gggs time')[0].text
		return applenews_item