# coding=utf-8 

import fasttext
import jieba
import sys
import json
from kafka import KafkaConsumer
reload(sys)
sys.setdefaultencoding('utf-8')

kafka_list = ["10.120.17.73:9092"]

def read_from_kafka():
	consumer = KafkaConsumer('topic_name', bootstrap_servers=kafka_list, client_id='client_id1', group_id='group_id1')
	for msg in consumer:
		print msg, type(msg)


def interface_fasttext(sen):
	sen = split_sentence(sen)
	classifier = fasttext.load_model('token/fast.model.bin', label_prefix='__label__')
	texts = [sen]
	labels = classifier.predict(texts, k=1)
	print labels

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
	new_sen = new_sen.replace('  ', ' ')
	print new_sen, 'new_sen'
	return new_sen

if __name__ == '__main__':
	# interface_fasttext(' 沃 投 资 p 2 p 投 资 理 财 的 资 金 规 划 应 注 重 风 险 分 散 沃 投 资 p 2 p 投 资 理 财 的 资 金 规 划 应 注 重 风 险 分 散 在 p 2 p 理 财 投 资 的 资 金 规 划 上 , 业 内 人 士 建 议 应 注 重 风 险 分 散 。 具 体 操 作 可 在 三 方 面 考 虑 : 一 , 选 择 不 同 的 借 款 期 限 进 行 投 资 , 可 以 依 据 自 己 的 生 活 规 划 、 投 资 专 业 度 等 进 行 合 理 搭 配 , 既 能 避 免 集 中 风 险 也 能 保 持 一 定 的 现 金 流 ; 如 新 用 户 初 进 入 平 台 时 , 可 选 择 期 限 较 短 , 如 3 个 月 以 内 的 产 品 , 多 次 复 投 后 , 则 可 考 虑 将 部 分 资 金 配 置 在 期 限 较 长 的 产 品 上 ; 二 , 选 择 不 同 类 型 的 平 台 进 行 分 散 投 资 , 平 台 不 同 , 意 味 着 投 资 的 资 产 类 型 不 同 , 风 险 类 型 也 不 同 , 或 能 起 到 风 险 隔 离 作 用 ; 三 , 选 择 p 2 p 理 财 之 外 的 投 资 品 , 行 业 研 究 人 士 表 示 , p 2 p 理 财 总 体 来 说 属 于 高 风 险 、 高 收 益 投 资 品 , 投 资 人 不 应 该 只 关 注 这 一 类 型 , 而 是 全 面 配 置 闲 散 资 金 , 如 存 款 、 货 币 基 金 、 债 券 、 保 险 等 。 文 章 由 沃 投 资')
	# split_sentence(u'对于未登录词，采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法')

    read_from_kafka()









