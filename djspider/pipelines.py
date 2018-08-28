# -*- coding: utf-8 -*-
import urllib
import urllib.request
import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DjspiderPipeline_ImgExternal(object):
    allowImagesDomain = ["file.your.domain.com","images.your.domain.com",]
    def process_item(self, item, spider):
        if(item["item_type"] == "imgurl"):
            #如果不在我们的file1, file2
            if(item["img_domain"].lower() not in self.allowImagesDomain):  
               item["errors"].append("external_url")
            #通过head 判断图片是否可访问
            # req = urllib.request.Request('http://python.org/',method="HEAD")
            # try:
            #     resp = urllib.request.urlopen(req)
            #     if(resp.code == 200):
            #         pass
            # except urllib.error.HTTPError as e:
            #     if(e.code == 404):
            #         item  = {"type":"not_exists","domain": imguri.netloc, "src": imgsrc}
            #         bad_img.append(item)
            #     pass
            # pass
        return item

class DjspiderPipeline_ImgValid(object):
    def process_item(self, item, spider):
        if(item["item_type"] == "imgurl"):          
            #通过head 判断图片是否可访问
            req = urllib.request.Request(item["img_src"],method="HEAD")
            try:
                resp = urllib.request.urlopen(req,timeout=2000)
                if(resp.code == 200):
                    pass
            except urllib.error.HTTPError as e:
                item["errors"].append(e.msg)            
                pass
            except TimeoutError as e:
                item["errors"].append("Timeout")            
                pass
            except urllib.error.URLError as e:
                item["errors"].append("UrlError")            
                pass
            except Exception as e:
                item["errors"].append("Unknown")            
                pass
            pass
        return item

class DjspiderPipeline_jsonPrint(object):
    def process_item(self, item, spider):
        if("errors" in item and len(item["errors"]) > 0):
            logging.warning('================================================')
            logging.warning(item["errors"])
            logging.warning(item["article_title"])
            logging.warning(item["article_url"])
            logging.warning(item["img_src"])

        return item
        