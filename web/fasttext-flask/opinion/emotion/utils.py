# coding=utf-8 

import fasttext
import jieba
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

def interface_fasttext(sen):
	sen = split_sentence(sen)
	classifier = fasttext.load_model('opinion/emotion/fast.model.bin', label_prefix='__label__')
	texts = [sen]
	labels = classifier.predict(texts, k=1)
	print labels
	return labels

def split_sentence(sen):
	print type(sen)
	if isinstance(sen, unicode):
		sen = sen.encode()
	sen_split = jieba.cut(sen)
	print sen_split, type(sen_split)
	new_sen_list = []
	for se in sen_split:
		if se.encode().isalpha():
			new_sen_list.append(se.strip())
		else:
			se_list = list(se.strip())
			new_sen_list.append(' '.join(se_list))
	new_sen = ' '.join(new_sen_list)
	return new_sen

if __name__ == '__main__':

	interface_fasttext(u'对于未登录词，采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法')
	
	# split_sentence(u'对于未登录词，采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法')
