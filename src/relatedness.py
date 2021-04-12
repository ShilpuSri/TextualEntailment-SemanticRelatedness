from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import pandas as pd
from nltk.wsd import lesk

 
def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
 
    if tag.startswith('V'):
        return 'v'
 
    if tag.startswith('J'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None

def find_contradiction(sentence1,sentence2):
    c = 0
    for s1 in sentence1:
        for s2 in sentence2: 
            if (((s1 == "not") or (s1=="no") or (s1 == "none")) or ((s2 == "not") or (s2=="no") or (s2 == "none"))):
                c = c+1
                return c
 
def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    contradiction=find_contradiction(word_tokenize(sentence1),word_tokenize(sentence2))
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
   
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
  
 
    # Remove the nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    score, count = 0.0, 0
    s_list = []
    count_none = 0
    for synset in synsets1:
         best = [synset.wup_similarity(ss) for ss in synsets2]
         b = pd.Series(best).max()
         s_list.append(b)
    scorelist = []
    for s in s_list:
       if s <= 1.0:
           count_none = count_none + 1
           scorelist.append(count_none)
    if contradiction == 1:
        score = sum_list(s_list)/max(scorelist) - 1
    else:
        score = sum_list(s_list)/max(scorelist)
    return score

def sum_list(l):
    sum = 0
    for x in l:
        if x<= 1.0:
             sum += x
    return sum


