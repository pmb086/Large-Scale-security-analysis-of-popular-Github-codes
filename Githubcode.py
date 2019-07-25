# -*- coding: utf-8 -*-
'''
This file should be replaced to generate test data for the analysis
'''

import scrapy
import json
import pprint
import os
import csv

dir_path_file = os.path.realpath(__file__) # Get the director path of this file
dir_path_this = os.path.dirname(dir_path_file)
os.chdir(dir_path_this)
#epochs = 50
language = ['lua','lisp','java','javascript','php','ruby','c#','c','c++','python','Objective-C','Assembly','Go','Rust','HTML','CSS','Shell']
class GithubcodeSpider(scrapy.Spider):
    name = 'Githubcode'
    allowed_domains = ["github.com"]
    base_uri = "http://www.github.com"
    start_urls = ["https://api.github.com/search/repositories?q=python:assembly&sort=stars&order=desc"]
	
    def parse(self, response):
        #print(response.text)
        json_data = json.loads(response.text)
        #pprint.pprint(json_data)
        filename = 'my_data'+ '.json'
        print(len(json_data['items']))
        with open('test_file.csv', mode='a') as out_file:
            out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range (0, len (json_data['items'])):
                line = str(json_data['items'][i]['svn_url'])+','+str(json_data['items'][i]['svn_url'][19:])+','+str(json_data['items'][i]['language'])+','+str(json_data['items'][i]['created_at'])+','+str(json_data['items'][i]['pushed_at'])+','+str(json_data['items'][i]['forks_count'])+','+str(json_data['items'][i]['watchers_count'])+','+str(json_data['items'][i]['stargazers_count'])+','+str(json_data['items'][i]['open_issues_count'])+','+str(json_data['items'][i]['score'])+','+'0'+','+'None'+','+'None'+','+'None'+','+'None'
                out_file.write('\n'+ line)
                print("%s,%s,%s,%s,%d,%d,%d,%d,%f,0,None,None,None,None" %(json_data['items'][i]['svn_url'],json_data['items'][i]['svn_url'][19:],json_data['items'][i]['created_at'],json_data['items'][i]['pushed_at'],json_data['items'][i]['forks_count'],json_data['items'][i]['watchers_count'],json_data['items'][i]['stargazers_count'],json_data['items'][i]['open_issues_count'],json_data['items'][i]['score']))
        with open(filename, 'w') as outfile:
            json.dump(json_data, outfile)
        for i in language:
            uri = "https://api.github.com/search/repositories?q=" + str(i) + ":assembly&sort=stars&order=desc"
            yield scrapy.Request(uri)#default callback is parse()
        '''authors = response.xpath("//a[@class = 'v-align-middle']/text()").extract()
        projects = response.css(".v-align-middle::attr(href)").extract()
        yield {'author': authors, "project": projects}
		
        while pages:
            next_page_url = response.xpath("//a[@class='next_page']/@href").extract_first()
            pages = pages-1
            if next_page_url:
                yield scrapy.Request(base_uri+next_page_url,callback=self.GithubProjectItem)'''