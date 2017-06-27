# -*- coding: utf-8 -*-

from django.conf.urls import url
from speed.views import *

urlpatterns = [
	url(r'^$', index, name='index'),	# 服务耗时趋势图
	url(r'^perRun$', perRun, name='perRun'),	# 服务耗时趋势图
	url(r'^netMap$', netMap, name='netMap'),	# 网络地图
	url(r'^netAjax$', netAjax, name='netAjax'),	# 错误率趋势
	url(r'^netSpeed$', netSpeed, name='netSpeed'),	# 错误率趋势
	url(r'^perAjax$', perAjax, name='perAjax'),	# 数据列表
	url(r'^allInts$', allInts, name='allInts'),	# 接口search查询页
	url(r'^single$', single, name='single'),	# single页
	url(r'^errRun$', errRun, name='errRun'),	# 错误趋势
	url(r'^errMap$', errMap, name='errMap'),	# 错误率地图
	url(r'^errAjax$', errAjax, name='errAjax'),	# 单接口错误列表
	url(r'^errPage$', errPage, name='errPage'),	#
	url(r'^errList$', errList, name='errList'),	#
	url(r'^errDetail$', errDetail, name='errDetail'),	#
	url(r'^userSearch$', userSearch, name='userSearch'),	#
	url(r'^userAjax$', userAjax, name='userAjax'),	# 错误信息页history
	url(r'^history$', history, name='history'),	#
	url(r'^ciType$', ciType, name='ciType'),	#
	url(r'^ciAjax$', ciAjax, name='ciAjax'),	#
	url(r'^feelPage$', feelPage, name='feelPage'),	#
	url(r'^wapPage$', wapPage, name='wapPage'),	#
	url(r'^appPage$', appPage, name='appPage'),	#
	url(r'^feelAjax$', feelAjax, name='feelAjax'),	#
	url(r'^warnMap$', warnMap, name='warnMap'),	#
	url(r'^warnAjax$', warnAjax, name='warnAjax'),	#
	url(r'^appAjax$', appAjax, name='appAjax'),	# appAjax
	url(r'^appAjax2$', appAjax2, name='appAjax2'),	# appAjax
]
