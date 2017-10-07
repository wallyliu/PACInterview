# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time, re, json
from bs4 import BeautifulSoup

class MicroScholar:
    """
    Input: Bayesian operational modal analysis: Theory, computation, practice
    Output: {affiliations:[...], authors:[...], journal:’...’} (json format)
    """

    def __init__(self):
        self.authors = []
        self.journal = []
        self.affiliations = []
        self.query = ''
        self.res = ''

    def run(self, query):
        self.res = self.spider(query)
        self.parse()
        return self.jsonencode()

    def spider(self, query):
        driver = webdriver.Chrome()
        base_url = "https://academic.microsoft.com/"
        driver.get(base_url + "/")
        #driver.find_element_by_css_selector("ma-queryformulation.searchWrap > div.search-input > #searchControl").clear()
        driver.find_element_by_css_selector("ma-queryformulation.searchWrap > div.search-input > #searchControl").send_keys(query)
        driver.find_element_by_css_selector("ma-queryformulation.searchWrap > div.search-btn").click()
        time.sleep(10)

        res = driver.page_source
        driver.close()
        return res

    def parse(self):
        soup = BeautifulSoup(self.res, "lxml")

        # parse authors and affiliations
        for author in soup.select('.paper-authors .paper-author-affiliation'):
            af = re.findall(r'\([\S\s]*.\)', author.text)
            self.affiliations.append(af[0].replace(')', '').replace('(', ''))
            self.authors.append(author.text.replace(af[0], '')[:-1])
        # parse journal
        tmp_journal = []
        for journal in soup.select('.paper-venue ul > li')[1:]:
            tmp_journal.append(str(journal.text))
        self.journal.append(','.join(tmp_journal))

    def jsonencode(self):
        return json.dumps({'affiliations': self.affiliations, 'authors': self.authors, 'journal': self.journal})

if __name__ == '__main__':
    query = "Bayesian operational modal analysis: Theory, computation, practice"
    spider = MicroScholar()
    result = spider.run(query)
    print(result)
