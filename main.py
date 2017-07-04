from bs4 import BeautifulSoup
import urllib

from goose import Goose
from goose.text import StopWordsChinese
import sys

base_url = 'https://www.hk01.com/%E5%85%A9%E5%B2%B8/'

def main(argv):

    last = 102351
    g = Goose({'stopwords_class': StopWordsChinese})

    with open('train.txt', 'a') as f:
        for i in reversed(range(last)):

            url = base_url + str(i)
            r = urllib.urlopen(url).read()
            soup = BeautifulSoup(r)
            tag = soup.find("div", {"class": "module_article_tag"})
            soup2 = BeautifulSoup(str(tag), "html.parser")
            h4 = soup2.findAll("h4")
            for t in h4:
                #print(t.contents[0])
                f.write('__label__'+t.contents[0].replace(" ", "_").encode('utf-8').strip())
                f.write(' , ') 

            article = g.extract(url=url)    
            cxt = u''.join(article.cleaned_text[:])
            cxt = cxt.replace('\n', ' ').replace('\r', '')
            #print(cxt)
            f.write(cxt.encode('utf-8').strip())
            f.write('\n')


if __name__ == "__main__":
    main(sys.argv)
