import jieba
import re
import gensim
import os

def get_file_contents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()

    while line:
        str = str + line
        line = f.readline()
    # f.close()
    return str


# 过滤符号
def filter(str):
    str = jieba.lcut(str)
    result = []

    for tags in str:
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result

def out_stopword(list):
    stop = open('C:\\Users\\86139\\Desktop\\stopwords.txt','r+',encoding='utf-8')
    stopwords = []
    stopword = stop.readline()
    while stopword != '':
        stopwords.append(stopword)
        stopword = stop.readline().strip('\n')
    newlist = []

    # 去除停用词
    for key in list:
        if not(key in stopwords):
            newlist.append(key)

    return newlist 

def calc_similarity(text1,text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim


if __name__ == '__main__':
    path_1 = input("参考论文的绝对路径：")
    path_2 = input("待检察文件的绝对路径：")
    if not os.path.exists(path_1):
        print("文件不存在")
        exit()
    if not os.path.exists(path_2):
        print("文件不存在")
        exit()
    str1 = get_file_contents(path_1)
    str2 = get_file_contents(path_2)
    text1 = filter(str1)
    text2 = filter(str2)
    print(len(text1), len(text2))
    text1 = out_stopword(text1)
    text2 = out_stopword(text2)
    print(len(text1), len(text2))
    # similarity = cosine_similarity(text1, text2)
    similarity = calc_similarity(text1, text2)
    print("文章相似度： %.4f"%similarity)