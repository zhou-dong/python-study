'''
naive bayes

p(a,b) = p(a) * p(b|a)
       = p(b) * p(a|b)

p(c,(x,y)) = p(x,y) * p(c|x,y)
           = p(c) * p(x,y|c)

p(c|x,y) = p(c) * p(x,y|c) / p(x,y)

not finish

'''

import numpy as np

def load_data_set():
    s1 = 'may dog has flea prblem please help'.split()
    s2 = 'maybe not take him to dog park stupid'.split()
    s3 = 'my dalmationi so cute i love him'.split()
    s4 = 'stop posting stupid worthless garbage'.split()
    s5 = 'mr licks ate my steak how to shop him'.split()
    s6 = 'quit buying worthless dog food stupid'.split()
    posting_list = [s1, s2, s3, s4, s5, s6]
    class_vec = [0, 1, 0, 1, 0, 1]
    return posting_list, class_vec

posting_list, class_vec = load_data_set()
def create_word_dict(posting_list=posting_list):
    result = {}
    for lst in posting_list:
        for word in lst:
            result[word] = result.get(word, 0) + 1
    return result

def get_words(index,posting_list=posting_list, class_vec=class_vec):
    result = {}
    for x in range(len(class_vec)):
        if class_vec[x] == index:
            continue
        for word in posting_list[x]:
            result[word] = result.get(word, 0) + 1
    return result

def negative_words():
    return get_words(0)

def positive_words():
    return get_words(1)

word_list = create_word_dict()
word_list_count = float(len(word_list))
def calculate_positive_weight(test_sentence):
    positives = positive_words()
    positive_count = float(len(positives))
    result = 1 ;
    for x in test_sentence.split():
        pxy = word_list.get(x, 0.1) / word_list_count
        pc = 0.5
        pc_xy = positives.get(x,0.1) / positive_count
        p = pc * pc_xy / pxy
        result = result * p
    return result

def calculate_nagative_weight(test_sentence):
    negatives = negative_words()
    negative_count = float(len(negatives))
    result = 1 ;
    for x in test_sentence.split():
        pxy = word_list.get(x, 0.1) / word_list_count
        pc = 0.5
        pc_xy = negatives.get(x,0.1) / negative_count
        p = pc * pc_xy / pxy
        result = result * p
    return result

def execute(test_sentence):
    print test_sentence,
    positive_score = calculate_positive_weight(test_sentence)
    negative_score = calculate_nagative_weight(test_sentence)
    print positive_score, negative_score,
    if positive_score > negative_score:
        print "positive"
    elif positive_score < negative_score:
        print "negative"
    else:
        print "sorry we do not know"

execute('my dog is so cute')
execute('stop your worthless dog')
