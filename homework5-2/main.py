#!/usr/bin/env python
# -*- coding: utf-8 -*--
import cgi
from google.appengine.api import users
import webapp2
import urllib
import json

trains = []
f = urllib.urlopen('http://fantasy-transit.appspot.com/net')


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html;charset=utf-8'
        self.response.write('<h1>最短経路 検索</h1><form action="/transit" method="post">出発駅 <select name=station1><option value=品川>山手線 - 品川</option><option value=大崎>山手線 - 大崎</option><option value=五反田>山手線 - 五反田</option><option value=目黒>山手線 - 目黒</option><option value=恵比寿>山手線 - 恵比寿</option><option value=渋谷>山手線 - 渋谷</option><option value=原宿>山手線 - 原宿</option><option value=代々木>山手線 - 代々木</option><option value=新宿>山手線 - 新宿</option><option value=新大久保>山手線 - 新大久保</option><option value=高田馬場>山手線 - 高田馬場</option><option value=目白>山手線 - 目白</option><option value=池袋>山手線 - 池袋</option><option value=大塚>山手線 - 大塚</option><option value=巣鴨>山手線 - 巣鴨</option><option value=駒越>山手線 - 駒越</option><option value=田端駅>山手線 - 田端駅</option><option value=西日暮里>山手線 - 西日暮里</option><option value=日暮里>山手線 - 日暮里</option><option value=鶯谷>山手線 - 鶯谷</option><option value=上野>山手線 - 上野</option><option value=御徒町>山手線 - 御徒町</option><option value=秋葉原>山手線 - 秋葉原</option><option value=神田>山手線 - 神田</option><option value=東京>山手線 - 東京</option><option value=有楽町>山手線 - 有楽町</option><option value=新橋>山手線 - 新橋</option><option value=浜松町>山手線 - 浜松町</option><option value=田町>山手線 - 田町</option><option value=品川>山手線 - 品川</option><option value=横浜>東横線 - 横浜</option><option value=反町>東横線 - 反町</option><option value=東白楽>東横線 - 東白楽</option><option value=白楽>東横線 - 白楽</option><option value=妙蓮寺>東横線 - 妙蓮寺</option><option value=菊名>東横線 - 菊名</option><option value=大倉山>東横線 - 大倉山</option><option value=綱島>東横線 - 綱島</option><option value=日吉>東横線 - 日吉</option><option value=元住吉>東横線 - 元住吉</option><option value=武蔵小杉>東横線 - 武蔵小杉</option><option value=新丸子>東横線 - 新丸子</option><option value=多摩川>東横線 - 多摩川</option><option value=田園調布>東横線 - 田園調布</option><option value=自由が丘>東横線 - 自由が丘</option><option value=都立大学>東横線 - 都立大学</option><option value=学芸大学>東横線 - 学芸大学</option><option value=祐天寺>東横線 - 祐天寺</option><option value=中目黒>東横線 - 中目黒</option><option value=代官山>東横線 - 代官山</option><option value=渋谷>東横線 - 渋谷</option><option value=日吉>目黒線 - 日吉</option><option value=元住吉>目黒線 - 元住吉</option><option value=武蔵小杉>目黒線 - 武蔵小杉</option><option value=新丸子>目黒線 - 新丸子</option><option value=多摩川>目黒線 - 多摩川</option><option value=田園調布>目黒線 - 田園調布</option><option value=奥沢>目黒線 - 奥沢</option><option value=大岡山>目黒線 - 大岡山</option><option value=洗足>目黒線 - 洗足</option><option value=西小山>目黒線 - 西小山</option><option value=武蔵小山>目黒線 - 武蔵小山</option><option value=不動前>目黒線 - 不動前</option><option value=目黒>目黒線 - 目黒</option><option value=蒲田>池上線 - 蒲田</option><option value=蓮沼>池上線 - 蓮沼</option><option value=池上>池上線 - 池上</option><option value=千鳥町>池上線 - 千鳥町</option><option value=久が原>池上線 - 久が原</option><option value=御嶽山>池上線 - 御嶽山</option><option value=雪が谷大塚>池上線 - 雪が谷大塚</option><option value=石川台>池上線 - 石川台</option><option value=洗足池>池上線 - 洗足池</option><option value=長原>池上線 - 長原</option><option value=旗の台>池上線 - 旗の台</option><option value=荏原中延>池上線 - 荏原中延</option><option value=戸越銀座>池上線 - 戸越銀座</option><option value=大崎広小路>池上線 - 大崎広小路</option><option value=五反田>池上線 - 五反田</option><option value=多摩川>多摩川線 - 多摩川</option><option value=沼部>多摩川線 - 沼部</option><option value=鵜の木>多摩川線 - 鵜の木</option><option value=下丸子>多摩川線 - 下丸子</option><option value=武蔵新田>多摩川線 - 武蔵新田</option><option value=矢口渡>多摩川線 - 矢口渡</option><option value=蒲田>多摩川線 - 蒲田</option><option value=二子玉川>大井町線 - 二子玉川</option><option value=上野毛>大井町線 - 上野毛</option><option value=等々力>大井町線 - 等々力</option><option value=尾山台>大井町線 - 尾山台</option><option value=九品仏>大井町線 - 九品仏</option><option value=自由が丘>大井町線 - 自由が丘</option><option value=緑が丘>大井町線 - 緑が丘</option><option value=大岡山>大井町線 - 大岡山</option><option value=北千束>大井町線 - 北千束</option><option value=旗の台>大井町線 - 旗の台</option><option value=荏原町>大井町線 - 荏原町</option><option value=中延>大井町線 - 中延</option><option value=戸越公園>大井町線 - 戸越公園</option><option value=下神明>大井町線 - 下神明</option><option value=大井町>大井町線 - 大井町</option><option value=中目黒>日比谷線 - 中目黒</option><option value=恵比寿>日比谷線 - 恵比寿</option><option value=広尾>日比谷線 - 広尾</option><option value=六本木>日比谷線 - 六本木</option><option value=神谷町>日比谷線 - 神谷町</option><option value=霞ケ関>日比谷線 - 霞ケ関</option><option value=日比谷>日比谷線 - 日比谷</option><option value=銀座>日比谷線 - 銀座</option><option value=東銀座>日比谷線 - 東銀座</option><option value=築地>日比谷線 - 築地</option><option value=八丁堀>日比谷線 - 八丁堀</option><option value=茅場町>日比谷線 - 茅場町</option><option value=人形町>日比谷線 - 人形町</option><option value=小伝馬町>日比谷線 - 小伝馬町</option><option value=秋葉原>日比谷線 - 秋葉原</option><option value=仲御徒町>日比谷線 - 仲御徒町</option><option value=上野>日比谷線 - 上野</option><option value=入谷>日比谷線 - 入谷</option><option value=三ノ輪>日比谷線 - 三ノ輪</option><option value=南千住>日比谷線 - 南千住</option><option value=北千住>日比谷線 - 北千住</option></select><br>到着駅 <select name=station2><option value=品川>山手線 - 品川</option><option value=大崎>山手線 - 大崎</option><option value=五反田>山手線 - 五反田</option><option value=目黒>山手線 - 目黒</option><option value=恵比寿>山手線 - 恵比寿</option><option value=渋谷>山手線 - 渋谷</option><option value=原宿>山手線 - 原宿</option><option value=代々木>山手線 - 代々木</option><option value=新宿>山手線 - 新宿</option><option value=新大久保>山手線 - 新大久保</option><option value=高田馬場>山手線 - 高田馬場</option><option value=目白>山手線 - 目白</option><option value=池袋>山手線 - 池袋</option><option value=大塚>山手線 - 大塚</option><option value=巣鴨>山手線 - 巣鴨</option><option value=駒越>山手線 - 駒越</option><option value=田端駅>山手線 - 田端駅</option><option value=西日暮里>山手線 - 西日暮里</option><option value=日暮里>山手線 - 日暮里</option><option value=鶯谷>山手線 - 鶯谷</option><option value=上野>山手線 - 上野</option><option value=御徒町>山手線 - 御徒町</option><option value=秋葉原>山手線 - 秋葉原</option><option value=神田>山手線 - 神田</option><option value=東京>山手線 - 東京</option><option value=有楽町>山手線 - 有楽町</option><option value=新橋>山手線 - 新橋</option><option value=浜松町>山手線 - 浜松町</option><option value=田町>山手線 - 田町</option><option value=品川>山手線 - 品川</option><option value=横浜>東横線 - 横浜</option><option value=反町>東横線 - 反町</option><option value=東白楽>東横線 - 東白楽</option><option value=白楽>東横線 - 白楽</option><option value=妙蓮寺>東横線 - 妙蓮寺</option><option value=菊名>東横線 - 菊名</option><option value=大倉山>東横線 - 大倉山</option><option value=綱島>東横線 - 綱島</option><option value=日吉>東横線 - 日吉</option><option value=元住吉>東横線 - 元住吉</option><option value=武蔵小杉>東横線 - 武蔵小杉</option><option value=新丸子>東横線 - 新丸子</option><option value=多摩川>東横線 - 多摩川</option><option value=田園調布>東横線 - 田園調布</option><option value=自由が丘>東横線 - 自由が丘</option><option value=都立大学>東横線 - 都立大学</option><option value=学芸大学>東横線 - 学芸大学</option><option value=祐天寺>東横線 - 祐天寺</option><option value=中目黒>東横線 - 中目黒</option><option value=代官山>東横線 - 代官山</option><option value=渋谷>東横線 - 渋谷</option><option value=日吉>目黒線 - 日吉</option><option value=元住吉>目黒線 - 元住吉</option><option value=武蔵小杉>目黒線 - 武蔵小杉</option><option value=新丸子>目黒線 - 新丸子</option><option value=多摩川>目黒線 - 多摩川</option><option value=田園調布>目黒線 - 田園調布</option><option value=奥沢>目黒線 - 奥沢</option><option value=大岡山>目黒線 - 大岡山</option><option value=洗足>目黒線 - 洗足</option><option value=西小山>目黒線 - 西小山</option><option value=武蔵小山>目黒線 - 武蔵小山</option><option value=不動前>目黒線 - 不動前</option><option value=目黒>目黒線 - 目黒</option><option value=蒲田>池上線 - 蒲田</option><option value=蓮沼>池上線 - 蓮沼</option><option value=池上>池上線 - 池上</option><option value=千鳥町>池上線 - 千鳥町</option><option value=久が原>池上線 - 久が原</option><option value=御嶽山>池上線 - 御嶽山</option><option value=雪が谷大塚>池上線 - 雪が谷大塚</option><option value=石川台>池上線 - 石川台</option><option value=洗足池>池上線 - 洗足池</option><option value=長原>池上線 - 長原</option><option value=旗の台>池上線 - 旗の台</option><option value=荏原中延>池上線 - 荏原中延</option><option value=戸越銀座>池上線 - 戸越銀座</option><option value=大崎広小路>池上線 - 大崎広小路</option><option value=五反田>池上線 - 五反田</option><option value=多摩川>多摩川線 - 多摩川</option><option value=沼部>多摩川線 - 沼部</option><option value=鵜の木>多摩川線 - 鵜の木</option><option value=下丸子>多摩川線 - 下丸子</option><option value=武蔵新田>多摩川線 - 武蔵新田</option><option value=矢口渡>多摩川線 - 矢口渡</option><option value=蒲田>多摩川線 - 蒲田</option><option value=二子玉川>大井町線 - 二子玉川</option><option value=上野毛>大井町線 - 上野毛</option><option value=等々力>大井町線 - 等々力</option><option value=尾山台>大井町線 - 尾山台</option><option value=九品仏>大井町線 - 九品仏</option><option value=自由が丘>大井町線 - 自由が丘</option><option value=緑が丘>大井町線 - 緑が丘</option><option value=大岡山>大井町線 - 大岡山</option><option value=北千束>大井町線 - 北千束</option><option value=旗の台>大井町線 - 旗の台</option><option value=荏原町>大井町線 - 荏原町</option><option value=中延>大井町線 - 中延</option><option value=戸越公園>大井町線 - 戸越公園</option><option value=下神明>大井町線 - 下神明</option><option value=大井町>大井町線 - 大井町</option><option value=中目黒>日比谷線 - 中目黒</option><option value=恵比寿>日比谷線 - 恵比寿</option><option value=広尾>日比谷線 - 広尾</option><option value=六本木>日比谷線 - 六本木</option><option value=神谷町>日比谷線 - 神谷町</option><option value=霞ケ関>日比谷線 - 霞ケ関</option><option value=日比谷>日比谷線 - 日比谷</option><option value=銀座>日比谷線 - 銀座</option><option value=東銀座>日比谷線 - 東銀座</option><option value=築地>日比谷線 - 築地</option><option value=八丁堀>日比谷線 - 八丁堀</option><option value=茅場町>日比谷線 - 茅場町</option><option value=人形町>日比谷線 - 人形町</option><option value=小伝馬町>日比谷線 - 小伝馬町</option><option value=秋葉原>日比谷線 - 秋葉原</option><option value=仲御徒町>日比谷線 - 仲御徒町</option><option value=上野>日比谷線 - 上野</option><option value=入谷>日比谷線 - 入谷</option><option value=三ノ輪>日比谷線 - 三ノ輪</option><option value=南千住>日比谷線 - 南千住</option><option value=北千住>日比谷線 - 北千住</option></select><br><input type=submit value=検索></form>')


# this " search " use make trains

def search(eki_name):
    exist = False
    for train in trains:
        for name in train:
            if name == eki_name:
                exist = True
    return exist

# plus neighbors
def neighbors_insert(index, rosen_count, eki_name, itemList):
    for train in trains:
        for name in train:
            if name == eki_name:
                if index == 0:
                    train[name].append(str(itemList[1]))
                elif 0 < index and index < rosen_count-1:
                    train[name].append(str(itemList[index-1]))
                    train[name].append(str(itemList[index+1]))
                elif index == rosen_count - 1:
                    train[name].append(str(itemList[index-1]))

                    
def searchstation(eki_name):
    for train in trains:
        for name in train:
            if name == eki_name:
                return train[name]

            
# breadth first search
def breadthFirstSearch(station1, station2):

    qList = []
    visited = set()
    preVisit = set()
    visited.add(station1) # visited a station
    preVisit.add(station1)
    qList.append(station1)

    previous = dict()
    previous[station1] = 'first'
    
    while not len(qList) == 0:
        r = qList[0]
        visited.add(r)
        qList = qList[1:]

        if r == station2: # arrive staion2
            return previous
            break
        
        rNeighbors = searchstation(r)
        if rNeighbors == None:
            lenNeigbors = 0
        else:
            lenNeigbors = len(rNeighbors)
        
        num = 0
        while num < lenNeigbors:
            r2 = rNeighbors[num]
            if ((r2 in visited) == False) and ((r2 in preVisit) == False):
                previous[r2] = r
                qList.append(r2)
                preVisit.add(r2)
            num += 1
                


def main(station1, station2):

    # make trains
    for line in f:   
        itemList = line[:-1].split('\t')
        #del itemList[0]

        rosen_count = len(itemList)

        for num in range(1,rosen_count):
            graph = {}
            station = str(itemList[num])
            
            exist = search(station)
            if exist == False:
                graph[station] = []
                trains.append(graph)
            neighbors_insert(num, rosen_count, station, itemList)

    # BFS
    previous = breadthFirstSearch(station1, station2)

    answer = []
    eki2 = station2
    answer.insert(0,station2)
    while True:
        eki1 = previous[eki2]
        answer.insert(0,eki1)
        if eki1 == station1:
            break
        else:
            eki2 = eki1

    return answer


class Transit(webapp2.RequestHandler):
    def post(self):
        station1 = self.request.get('station1')
        station2 = self.request.get('station2')

        from_sta = station1.encode('utf-8')
        to_sta = station2.encode('utf-8')

        answer = main(from_sta, to_sta)

        self.response.headers['Content-Type'] = 'text/html;charset=utf-8'
        if answer == None:
            self.response.write('answer is NONE')
        else:       
            while True:
                self.response.write('<font size=5> %s </font>' % answer[0])
                answer = answer[1:]
                if answer == []:
                    break
                else:
                    self.response.write('<font size=5>-></font>')

                    
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/transit', Transit),
], debug=True)
