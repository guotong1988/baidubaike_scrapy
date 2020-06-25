import scrapy
import time
import re
out_file = open("data.txt",mode="w",encoding="utf-8")
remove = re.compile('\s')
name_set = set()
f = open("baike.dic",mode="r",encoding="utf-8")
for line in f:
    name_set.add(line.strip())

class YoulaiSpider(scrapy.Spider):
    name = "baike"
    allowed_domains = ["baike.baidu.com"]
    start_urls = [
        "http://baike.baidu.com/item/"
    ]

    def start_requests(self):
        for name in name_set:
            url = self.start_urls[0] + name
            # print(url)
            # print("停顿1秒...............")
            time.sleep(1)

            requests = scrapy.Request(url,
                                      callback=self.sub_parse)
            yield requests


    def sub_parse(self, response):
        # print(response.url + " !!!")
        content_list = response.xpath('.//div[@class="para"]').xpath('string(.)').extract()
        for content in content_list:
            content = re.sub(remove, '', content)
            print(content)
            out_file.write(content)
            out_file.write("\n")
            out_file.flush()
