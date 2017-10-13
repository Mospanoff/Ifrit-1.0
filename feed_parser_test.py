import time
import feedparser



def news_pars():
    d = feedparser.parse(chose_channel())
    mt = d['channel']['title']
    fn = d['entries'][0]['summary']
    sn = "Следующая новость.........", d['entries'][1]['summary']
    tn = "Следующая новость.........", d['entries'][2]['summary']
    fon = "Следующая новость.........", d['entries'][3]['summary']
    fin = "Следующая новость.........", d['entries'][4]['summary']
    answer = (mt,fn, sn, tn, fon, fin)
    print(answer)
    return answer

class key_words(object):
    main_news = ["главные", "общем", "вообщем"]
    tech_news = ["компьютеры", "техно", "digital", "технология", "технологий"
                 , "компьютер", "компьютерные"]
    world_news = ["мир", "мире", "других", "мировые"]
    ecom_news = ["экономика", "экономики", "экономический"
                 ,"экономические", "экономике"]
    society_news = ["общество", "общества", "общественные", "общественный"]
    random = ["рандом", "любая", "любые", "выбери", "случайно", "случайные", "не важно"]


    
class links(object):
    main_news = 'https://news.yandex.ru/index.rss'
    tech_news = 'https://news.yandex.ru/computers.rss'
    world_news = 'https://news.yandex.ru/world.rss'
    ecom_news = 'https://news.yandex.ru/business.rss'
    society_news = 'https://news.yandex.ru/society.rss'
    list_of_ch = (main_news, tech_news, world_news, ecom_news, society_news)

def chose_channel():
    from random import choice
    link = choice(links.list_of_ch)
    return link
    
def someth():
    if any(cognate in command for cognate in key_words.main_news):
        link = 'https://news.yandex.ru/index.rss'
        return link
    if any(cognate in command for cognate in key_words.tech_news):
        link = 'https://news.yandex.ru/computers.rss'
        return link
    if any(cognate in command for cognate in key_words.ecom_news):
        link = 'https://news.yandex.ru/business.rss'
        return link
    if any(cognate in command for cognate in key_words.world_news):
        link = 'https://news.yandex.ru/world.rss'
        return link
    if any(cognate in command for cognate in key_words.society_news):
        link = 'https://news.yandex.ru/society.rss'
        return link
    if any(cognate in command for cognate in key_words.random):
        from random import choice
        link = choice(links.list_of_ch)
        return link






















    
    
    

