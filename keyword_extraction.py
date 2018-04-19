# encoding: utf-8
""" TextRank算法提取文本关键词
1、将待抽取关键词的文本进行分词、去停用词、筛选词性
2、以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
3、计算图中节点的PageRank，注意是无向带权图
"""

import codecs
from jieba import posseg
import jieba.analyse



def extract_keywords(sentence, topK=10, algorithm='textrank', withWeight=False):
    """
    使用TextRank算法从句子中提取关键词
    Parameter:
        - topK: return how many top keywords. `None` for all possible words.
        - algorithm: textrank, tfidf
        - withWeight: if True, return a list of (word, weight);
                      if False, return a list of words.
        - allowPOS: the allowed POS list eg. ['ns', 'n', 'vn', 'v'].
                    if the POS of w is not in this list, it will be filtered.
        - withFlag: if True, return a list of pair(word, weight) like posseg.cut
                    if False, return a list of words
    """
    jieba.load_userdict('userdict.txt')

    jieba.analyse.set_stop_words('stopword.txt')  # 加载自定义停用词表
    if algorithm == 'textrank':
        keywords = jieba.analyse.textrank(sentence, topK=topK, withWeight=withWeight, allowPOS=('n','nz','v','vd','vn','l','a','d'))  # TextRank关键词提取，词性筛选
    else:
        keywords = jieba.analyse.extract_tags(sentence, topK=topK, withWeight=withWeight, allowPOS=('n','nz','v','vd','vn','l','a','d'))
    return keywords


if __name__ == '__main__':
    sentence = '士兰微[600460]公司是中国集成电路设计行业的领先企业，已掌握和拥有的技术可从事中高端产品的开发，核心技术在中国同行业中处于较高水平，具有明显的竞争优势。公司经过近5年的持续技术攻关，已经在自己的芯片生产线上全部实现了功率器件、模拟电路、传感器等关键集成电路和器件的研发与批量生产。而在入股安路科技后，也快速切入芯片市场，目前是国内唯一一家全面掌握了核心技术的芯片厂家'
    keywords = extract_keywords(sentence, topK=5, withWeight=True, algorithm='tfidf')
    print(keywords)

    sentence = '兆易创新主要业务为闪存芯片及其衍生产品、微控制器产品的研发、技术支持和销售。其中主要的业务是32位MCU开发，公司研发了中国本土第一个32位MCU，主要客户市场是工业级和消费级市场。同时，兆易创新也是国内存储器及物联网芯片产业的龙头企业，受益于AI芯片带来的数据大量提升，其强调芯云端结合及需要云端更大的存储能力，会进一步对存储器的要求更高，加快存储器芯片需求增长'
    keywords = extract_keywords(sentence, topK=5, withWeight=True, algorithm='tfidf')
    print(keywords)


