# -*- coding: utf-8 -*-
import json,base64,datetime
from decimal import *


def timesince(dt, default="just now"):
	"""
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """

	now = datetime.datetime.now()
	diff = now - dt

	#return diff

	periods = (
		(diff.days / 365, "年"),
		(diff.days / 30, "月"),
		(diff.days, "天"),
		(diff.seconds / 3600, "小时"),
		(diff.seconds / 60, "分钟"),
		(diff.seconds, "秒"),
	)

	for period, singular in periods:
		if period > 1:
			return "%d%s前" % (period, singular)

	return default

def moneyfmt(value, places=2, curr='', sep=',', dp='.', pos='', neg='-', trailneg=''):
	"""Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
	value = Decimal(value)
	q = Decimal(10) ** -places  # 2 places --> '0.01'
	sign, digits, exp = value.quantize(q).as_tuple()
	result = []
	digits = map(str, digits)
	build, next = result.append, digits.pop
	if sign:
		build(trailneg)
	for i in range(places):
		build(next() if digits else '0')
	build(dp)
	if not digits:
		build('0')
	i = 0
	while digits:
		build(next())
		i += 1
		if i == 3 and digits:
			i = 0
			build(sep)
	build(curr)
	build(neg if sign else pos)
	return ''.join(reversed(result))

def MoneyFmt(money):#货币格式化
    return moneyfmt(money, curr='￥')

def getURLfromSource(Sources,SourceName):#从指定源名获取地址
	Sources = json.loads(Sources)
	return Sources.get(SourceName,"")

def getbase64(str):
	bytesString = str.encode(encoding="utf-8")
	
	return base64.b64encode(bytesString).decode()

def getOrderStatus(status,type):
    if type == "style":
        OrderStatus = {'Delivered': 'success',
                       'WillRefurd': ' ',
                       'Refurded': ' ',
                       'Signed': ' ',
                       'Unpaid': 'danger', 'Paid': 'info',
                       'Cancel': ' ',
                       'Refurding': ' '}

        return OrderStatus[status]
    else:
        OrderStatus= {'Delivered': u'发货中',
         u'WillRefurd': '退货申请',
         'Refurded': '退货成功', 'Signed': '已签收',
         'Unpaid': '未付款', 'Paid': '已付款',
         'Cancel': '已取消',
         'Refurding': '退货中'}

        return OrderStatus[status]