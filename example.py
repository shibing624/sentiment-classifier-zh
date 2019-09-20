# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description:
"""

import sentiment_classifier

if __name__ == '__main__':
    texts = ["苹果是一家伟大的公司", "我刚去吃饭了", "你到底在干嘛呀", "我以前是个小偷，现在是个警察了",
             "再也不敢吃紫菜了",
             "我正在刘鑫描述凶案事发过程江歌母亲在日请愿判凶手死刑的主页，朋友们快来看看吧",
             "王者荣耀游戏风靡校园。据了解，在上海和国内不少城市的中小学校，玩王者荣耀的学生比例不低。有小学生称，"
             "班里有同学为了玩游戏，凌晨3点起床，一直打到6点，再去上学。专家表示，中小学生痴迷游戏并非好事，父母要适当引导和干预。"]
    for i in texts:
        r = sentiment_classifier.classify(i)
        print(i, r)
