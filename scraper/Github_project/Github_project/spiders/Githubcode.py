# -*- coding: utf-8 -*-
import scrapy
import json
import pprint
import os
import csv
import pandas as pd

#file_name = 'C:\Users\Balaji\Github_project\Github_project\spiders\100.csv'

df = pd.read_csv(r'C:\Users\Balaji\Github_project\Github_project\spiders\100.csv', sep=",", error_bad_lines=False)
projects = list(df['Project_Name'])
dir_path_file = os.path.realpath(__file__) # Get the director path of this file
dir_path_this = os.path.dirname(dir_path_file)
os.chdir(dir_path_this)


class GithubcodeSpider(scrapy.Spider):
    name = 'Githubcode'
    allowed_domains = ["api.github.com"]
    base_uri = "http://www.api.github.com"
    start_urls = ["https://api.github.com/repos/"+projects[0]]
	
    def parse(self, response):
        #print(response.text)
        json_data = json.loads(response.text)
        #pprint.pprint(json_data)
        filename = 'my_data'+ '.json'
        #print(len(json_data))
        with open('train_file.csv', mode='a') as out_file:
            out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            line = str(json_data['svn_url'])+','+str(json_data['svn_url'][19:])+','+str(json_data['language'])+','+str(json_data['created_at'])+','+str(json_data['pushed_at'])+','+str(json_data['forks_count'])+','+str(json_data['watchers_count'])+','+str(json_data['stargazers_count'])+','+str(json_data['open_issues_count'])+','+str(json_data['subscribers_count'])#+','+str(df.iloc[i,1])+','+str(df.iloc[i,2])+','+str(df.iloc[i,3])+','+str(df.iloc[i,4])+','+str(df.iloc[i,5])
            out_file.write('\n'+ line)
            #print("%s,%s,%s,%s,%d,%d,%d,%d,%f" %(json_data['svn_url'],json_data['svn_url'][19:],json_data['created_at'],json_data['pushed_at'],json_data['forks_count'],json_data['watchers_count'],json_data['stargazers_count'],json_data['open_issues_count'],json_data['subscribers_count']))
        with open(filename, 'w') as outfile:
            json.dump(json_data, outfile)
        for i in range(1,len(projects)):  
            uri = "https://api.github.com/repos/" + str(projects[i])
            yield scrapy.Request(uri)#default callback is parse()			
        '''authors = response.xpath("//a[@class = 'v-align-middle']/text()").extract()
        projects = response.css(".v-align-middle::attr(href)").extract()
        yield {'author': authors, "project": projects}
		
        while pages:
            next_page_url = response.xpath("//a[@class='next_page']/@href").extract_first()
            pages = pages-1
            if next_page_url:
                yield scrapy.Request(base_uri+next_page_url,callback=self.GithubProjectItem)'''