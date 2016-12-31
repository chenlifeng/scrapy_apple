# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
class ApplenewsPipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect('applenews.sqlite')
		self.cur = self.conn.cursor()
		self.cur.execute('create table if not exists applenews(title VARCHAR(100), content TEXT, time VARCHAR(50))')
	
	def close_spider(self, spider):
		self.conn.commit()
		self.conn.close()
	
	def process_item(self, item, spider):
		col = ','.join(item.keys())
		placeholders = ','.join(len(item) * '?')
		sql = 'insert into applenews({}) values({})'
	#	self.cur.execute(sql.format(col, placeholders), item.values())
		self.cur.execute("insert into applenews values(?,?,?)",(item['title'], item['content'], item['time']))
		return item