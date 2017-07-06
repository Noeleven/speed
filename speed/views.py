from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.cache import cache_page
from django.template import loader
import time
import json
import datetime
import random
from speed.models import *

# Create your views here.
def index(request):
	return render(request, 'index.html', locals())

# 服务性能
def perRun(request):
	return render(request, 'perRun.html', locals())

def perAjax(request):
	origin = Ints.objects.all()[:10]
	datas = []
	for x in origin:
		tmp = {
			'int':x.method,
			'ver':x.version,
			'des':x.des,
			'ci':x.cType.des,
			'time':random.randint(0, 5100),
			'num':random.randint(1000,300000),
		}
		datas.append(tmp)
	return render(request, 'perAjax.html', locals())

# 单接口page
def single(request):
	iid = request.GET['id']
	inter = Ints.objects.get(id=iid)
	time = random.randint(40,1000)
	num = random.randint(4000,50000)
	return render(request, 'single.html', locals())

# 错误首页
def errPage(request):
	code = request.GET['code']
	yysd = []
	intd = []
	yys = ['电信', '联通', '移动', '其他']
	wlzs = ['4G', '3G', 'WIFI', '2G', '其他']
	origin = Ints.objects.all()[:50]
	start = time.time()
	for x in yys:
		for y in wlzs:
			tmp = {
				'yys':x,
				'wlzs':y,
				'code':code,
				'num':random.randint(0, 1000),
			}
			yysd.append(tmp)
	sec = time.time()
	print(sec-start)
	for x in origin:
		tmp = {
			'int':x.method,
			'ver':x.version,
			'des':x.des,
			'type':x.sType,
			'code':code,
			'num':random.randint(0,500),
		}
		intd.append(tmp)
	end = time.time()
	print(end-sec)
	return render(request, 'errPage.html', locals())

def errAjax(request):
	data = request.GET['data']
	errType = netErr.objects.all()
	datas = []
	for x in errType:
		tmp = {
			'code':x.code,
			'des':x.des,
			'num':random.randint(10,20000)
		}
		datas.append(tmp)
	return render(request, 'errAjax.html', locals())

# 错误趋势
def errRun(request):
	a = 1
	return render(request, 'errRun.html', locals())

# 错误地域分布
def errMap(request):
	a = 1
	return render(request, 'errMap.html', locals())

# 错误请求列表
def errList(request):
	myyys = request.GET.get('type1')
	mywlzs = request.GET.get('type2')
	iid = request.GET.get('id')
	yys = ['电信', '联通', '移动', '其他']
	wlzs = ['4G', '3G', 'WIFI', '2G', '其他']
	origin = Ints.objects.all()[:50]
	datas = []
	if myyys:
		for x in origin:
			tmp = {
				'int':x.method,
				'des':x.des,
				'createTime':(datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0,100000))).strftime('%Y-%m-%d %H:%M:%S'),
				'yys':myyys,
				'wlzs':mywlzs,
				'phone':'13' + str(random.randint(100000000,999999999)),
				'userId':random.randint(000000000,999999999),
				'sertime':random.randint(300,4500),
				'netime':random.randint(300,15000),
				'code':random.choice(['200', '301', '404', '500', '403'])
			}
			datas.append(tmp)
	elif iid:
		target = Ints.objects.get(method=iid)
		for x in range(random.randint(1,30)):
			tmp={
				'int':target.method,
				'des':target.des,
				'createTime':(datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0,100000))).strftime('%Y-%m-%d %H:%M:%S'),
				'yys':random.choice(yys),
				'wlzs':random.choice(wlzs),
				'phone':'13' + str(random.randint(100000000,999999999)),
				'userId':random.randint(000000000,999999999),
				'sertime':random.randint(300,4500),
				'netime':random.randint(300,15000),
				'code':random.choice(['200', '301', '404', '500', '403'])
			}
			datas.append(tmp)
	else:
		pass

	return render(request, 'errList.html', locals())

# 错误详情
def errDetail(request):
	userId = request.GET.get('userId')
	phone = request.GET.get('phone')
	inter = request.GET.get('int')
	sertime = request.GET.get('sertime')
	netime = request.GET.get('netime')
	time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	code = random.choice(['200', '301', '404', '500', '403'])

	return render(request, 'errDetail.html', locals())

# 网络性能
def netMap(request):
	provices = ['上海', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '北京', '天津', '重庆', '香港', '澳门']

	datas = []

	for x in provices:
		tmp = {
			'provice':x,
			'netTime':random.randint(0, 6000),
			}
		datas.append(tmp)
	return render(request, 'netMap.html', locals())

def netAjax(request):
	city = request.GET['city']
	yys = ['电信', '联通', '移动', '其他']
	wlzs = ['4G', '3G', 'WIFI', '2G', '其他']
	datas = []
	for x in yys:
		for y in wlzs:
			tmp = {
				'yys':x,
				'wlzs':y,
				'netTime':random.randint(0, 3000),
			}
			datas.append(tmp)
	return render(request, 'netAjax.html', locals())

def netSpeed(request):
	return render(request, 'netSpeed.html', locals())

# 用户查询
def userSearch(request):
	return render(request, 'userSearch.html', locals())

def userAjax(request):
	userId = request.GET.get('userId')
	phone = request.GET.get('phone')
	datas = []
	for x in range(random.randint(1,8)):
		tmp = {
			'userId':userId,
			'phone':phone,
			'phoneType':random.choice(['iPhone6','iPhone7 Plus','xiaomi5']),
			'deviceToken':random.randint(400000,800000),
			'num':random.randint(10,80),
		}
		datas.append(tmp)
	return render(request, 'userAjax.html', locals())

# 接口一览
def allInts(request):
	origin = Ints.objects.all()[:100]
	datas = []
	for x in origin:
		tmp = {
			'int':x.method,
			'ver':x.version,
			'des':x.des,
			'type':x.sType,
			'time':random.randint(0, 5100),
			'num':random.randint(1000,300000),
		}
		datas.append(tmp)
	return render(request, 'allInts.html', locals())

# 品类分类
def history(request):
	userId = request.GET.get('userId')
	phone = request.GET.get('phone')
	phoneType = request.GET.get('phoneType')
	deviceToken = request.GET.get('deviceToken')
	num = int(request.GET.get('num'))
	datas = []
	yys = ['电信', '联通', '移动', '其他']
	wlzs = ['4G', '3G', 'WIFI', '2G', '其他']
	origin = Ints.objects.all()[:40]
	for x in range(num):
		y = random.choice(origin)
		tmp = {
			'userId':userId,
			'phone':phone,
			'createTime':(datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0,100000))).strftime('%Y-%m-%d %H:%M:%S'),
			'code':200,
			'int':y.method,
			'des':y.des,
			'phoneType':phoneType,
			'sertime':random.randint(30,3000),
			'netime':random.randint(30,5000),
		}
		datas.append(tmp)
	return render(request, 'history.html', locals())

# 品类分类
def ciType(request):
	origin = CategoryType.objects.all()
	datas = []
	version = ['7.10.0', '7.9.8', '7.9.7']
	channel = ['IOS', 'Android', 'H5']
	for x in origin:
		tmp = {
			'type':x.des,
			# 'num':random.randint(5,25),
			# 'sertime':random.randint(30,2500),
			# 'intNum':random.randint(15,30),
			# 'time':random.randint(40,5000),
			# 'version':random.choice(version),
			# 'channel':random.choice(channel),
		}
		datas.append(tmp)
	return render(request, 'ciType.html', locals())

def ciAjax(request):
	mtype = request.GET.get('type')
	mver = request.GET.get('version')
	mchan = request.GET.get('channel')
	datas = []
	pageName = ['详情页', '选择团期','填写订单页','更换机票','更换酒店','提交订单']
	for x in pageName:
		ints = []
		y = random.randint(1,6)
		for y in range(1,y):
			sertime = random.randint(1,8000)
			netTime = random.randint(1,8000)
			ii = Ints.objects.get(id=random.randint(1,100))
			itmp = {
				'method':ii.method,
				'des':ii.des,
				'sertime':sertime,
				'netTime':netTime,
				'netper':netTime / 150,
				'serper':sertime / 150,
				}
			ints.append(itmp)

		tmp = {
			'des':x,
			'ints':ints,
			}
		datas.append(tmp)
	print(datas)
	return render(request, 'ciAjax.html', locals())

# 用户感知品类排名
def feelPage(request):
	origin = feel.objects.filter(plat='PC')
	datas = []
	for x in origin:
		tmp = {
			'id':x.id,
			'name':x.name,
			'url':x.url,
			'plat':x.plat,
			'score':random.randint(50,99),
			'fid':'fid' + str(random.randint(11111,55555))
		}
		datas.append(tmp)
	return render(request, 'feelPage.html', locals())

def wapPage(request):
	origin = feel.objects.filter(plat='M站')
	datas = []
	for x in origin:
		tmp = {
			'id':x.id,
			'name':x.name,
			'url':x.url,
			'plat':x.plat,
			'score':random.randint(50,99),
			'fid':'fid' + str(random.randint(11111,55555))
		}
		datas.append(tmp)
	return render(request, 'feelPage.html', locals())

def feelAjax(request):
	# 综合评分 = 各项评分平均得分 单项评分 = 100 - 实际数值 * 40 / 该项全网平均值
	nid = request.GET.get('id')
	score = request.GET.get('score')
	origin = feel.objects.get(id=nid)
	value = [random.randint(50,99) for x in range(7)]
	index = {
		'dns':round(random.random(),3),
		'con':round(random.random(),3),
		'server':round(random.random(),3),
		'download':round(random.random(),3),
		'wp':round(random.random(),3),
		'dp':round(random.random() + 0.5,3),
		'fp':round(random.random() + 2,3),
		'lp':round(random.random() + 4,3),
		'req':random.randint(50000,130000),
		'size':round(random.random()*2000, 2),
		'ssl':round(random.random(),3),
		'score':score,
	}
	return render(request, 'feelAjax.html', locals())

def appPage(request):
	datas = []
	cis = CategoryType.objects.all()
	return render(request, 'appPage.html', locals())

def appAjax(request):
	tid = request.GET.get('id')
	datas = []
	opration = ['门票频道页','门票详情页','时间价格表页','首页','调起支付页']
	ver = ['7.9.8','7.9.6','7.9.7','7.9.5','7.10.0']
	activity = ['com.bumptech.glide.manager.RequestManagerFragment','com.gift.android.activity.splash.WelcomeActivity','com.lvmama.special.activity.SpecialDetailBaseActivity','QuestionDetailsViewController','HomeSearchViewController']
	cis = CategoryType.objects.all()
	for x in range(random.randint(3,6)):
		tmp = {
			'name':random.choice(opration),
			'activity':random.choice(activity),
			'wt':random.randint(30,2000),
			'ft':random.randint(30,2000),
			'version':random.choice(ver),
		}
		datas.append(tmp)
	return render(request, 'appAjax.html', locals())

def appAjax2(request):
	name = request.GET.get('name')
	return render(request, 'appAjax2.html', locals())

# 用户感知报警地图
def warnMap(request):
	return render(request, 'warnMap.html', locals())

def warnAjax(request):
	data = request.GET.get('data')
	index = {
		'dns':round(random.random(),3),
		'con':round(random.random(),3),
		'server':round(random.random(),3),
		'download':round(random.random(),3),
		'wp':round(random.random(),3),
		'dp':round(random.random() + 0.5,3),
		'fp':round(random.random() + 2,3),
		'lp':round(random.random() + 4,3),
		'req':random.randint(50000,130000),
		'size':round(random.random()*2000, 2),
	}
	return render(request, 'warnAjax.html', locals())
