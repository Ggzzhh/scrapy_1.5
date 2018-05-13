import time
from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient()
        self.db = self.client.Novel
        self.start = time.time()

    def close_spider(self, spider):
        self.client.close()
        print("总计用时：{}".format(time.time() - self.start))

    def process_item(self, item, spider):
        if item.get('qidian'):
            for name in item['qidian']:
                self.db.qidian.update({"_id": '500'}, {"$addToSet": {
                    'qidian': name}}, upsert=True)
        else:
            item = dict(item)
            novel = item.get('item')
            chapter = item.get('c_item')
            if novel:
                id = novel.get('novel_id')
                self.db.novel_msg.update({"_id": id}, {"$set": novel}, upsert=True)
            if chapter:
                c_id = chapter.pop('chapter_id')
                self.db.novels.update({"_id": c_id}, {"$set": chapter}, upsert=True)

        return novel['novel_name'] + "的章节" + chapter['chapter_name'] + '正在下载.....'
