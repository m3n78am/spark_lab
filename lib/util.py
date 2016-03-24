#!/usr/bin/env python

import sys

def parse(line):
	try:
		parts = line.split(",")
		class2,class3,name3,kdtId,goodsId,title = parts
	except:
		return None
	return (class2,name3,kdtId,goodsId,title)
	#return trainedData(class2,class3,name3,kdtId,goodsId,title)

class goods_order_obj():

	def __init__(self,line,delim=u"\001"):
		self.delim = delim
		self.dataMap = dict(zip(["order_id", "order_no", "kdt_id", "customer_id", "customer_name", "state", "feedback", "pay_time", "outer_transaction_number", "book_time", "buy_way", "buyer_id", "buyer_phone", "close_state", "customer_type", "stock_state", "order_type", "bank_pay", "refund_state", "express_state", "express_time", "pay_state", "pay", "postage", "real_pay", "is_free_postage", "feedback_time", "express_type"],self.parse(self.delim,line)))

	def parse(self,delim,line):
		try:
			parts = line.split(delim)
			order_id, order_no, kdt_id, customer_id, customer_name, state, feedback, pay_time, outer_transaction_number, book_time, buy_way, buyer_id, buyer_phone, close_state, customer_type, stock_state, order_type, bank_pay, refund_state, express_state, express_time, pay_state, pay, postage, real_pay, is_free_postage, feedback_time, express_type = parts
		except:
			return None
		return [order_id, order_no, kdt_id, customer_id, customer_name, state, feedback, pay_time, outer_transaction_number, book_time, buy_way, buyer_id, buyer_phone, close_state, customer_type, stock_state, order_type, bank_pay, refund_state, express_state, express_time, pay_state, pay, postage, real_pay, is_free_postage,feedback_time,express_type]






#for line in open("../test.dat"):
##for line in sys.stdin:
#	line = line.strip("\n")
#	x = goods_order_obj(line)
#	print x
