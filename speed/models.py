from django.db import models
from django.contrib import admin

# Create your models here.
class CategoryType(models.Model):
	cType = models.CharField(max_length=100, blank=True)
	des = models.CharField(max_length=100, blank=True)
	modifyTime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.cType


class BuType(models.Model):
	bType = models.CharField(max_length=100, blank=True)
	des = models.CharField(max_length=100, blank=True)
	modifyTime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.bType


class secondType(models.Model):
	sType = models.CharField(max_length=100, blank=True)
	des = models.CharField(max_length=100, blank=True)
	modifyTime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.sType


class Ints(models.Model):
	method = models.CharField(max_length=100)
	version = models.CharField(max_length=20, blank=True)
	des = models.CharField(max_length=200, blank=True)
	cType = models.ForeignKey(CategoryType, blank=True)
	sType = models.ForeignKey(secondType, blank=True)
	bType = models.ForeignKey(BuType, blank=True)
	inuse_choice = (
		('0', '弃用'),
		('1', '在用'),
		('2', '未配置'),
	)
	inuse = models.CharField(max_length=1, choices=inuse_choice, default='1')
	modifyTime = models.DateField(auto_now=True)


class PerData(models.Model):
	methodId = models.CharField(max_length=10)
	serverTime = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	NetTime = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	code = models.CharField(max_length=100, blank=True)
	userId = models.CharField(max_length=100, blank=True)
	deviceToken = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=100, blank=True)
	phoneType = models.CharField(max_length=100, blank=True)
	os = models.CharField(max_length=100, blank=True)
	ci = models.CharField(max_length=100, blank=True)
	lo = models.CharField(max_length=100, blank=True)
	la = models.CharField(max_length=100, blank=True)
	ot = models.CharField(max_length=100, blank=True)
	nt = models.CharField(max_length=100, blank=True)
	prov = models.CharField(max_length=100, blank=True)
	ver = models.CharField(max_length=100, blank=True)
	tec = models.CharField(max_length=100, blank=True)
	timeStamp = models.CharField(max_length=100, blank=True)
	recordTime = models.DateTimeField(blank=True)
	modifyTime = models.DateTimeField(auto_now=True)


class ServerData(models.Model):
	request = models.CharField(max_length=1000, blank=True)
	method = models.CharField(max_length=1000, blank=True)
	params = models.CharField(max_length=100, blank=True)
	response = models.CharField(max_length=100, blank=True)
	recordTime = models.DateTimeField(blank=True)
	modifyTime = models.DateTimeField(auto_now=True)


class netErr(models.Model):
	code = models.CharField(blank=True, max_length=100)
	des = models.CharField(blank=True, max_length=100)

class feel(models.Model):
	name = models.CharField(blank=True, max_length=100)
	url = models.CharField(blank=True, max_length=100)
	plat = models.CharField(blank=True, max_length=100)


class IntsAdmin(admin.ModelAdmin):
	list_display = ('method', 'version', 'des', 'cType', 'sType', 'bType', 'inuse', 'modifyTime')
	list_per_page = 30
	search_fields = ['method', 'version', 'des', 'cType__cType', 'sType__sType', 'bType__bType', 'inuse', 'modifyTime']

class CategoryTypeAdmin(admin.ModelAdmin):
	list_display = ('cType', 'des', 'modifyTime')
	list_per_page = 30
	search_fields = ['cType', 'des', 'modifyTime']

class BuTypeAdmin(admin.ModelAdmin):
	list_display = ('bType', 'des', 'modifyTime')
	list_per_page = 30
	search_fields = ['bType', 'des', 'modifyTime']

class secondTypeAdmin(admin.ModelAdmin):
	list_display = ('sType', 'des', 'modifyTime')
	list_per_page = 30
	search_fields = ['sType', 'des', 'modifyTime']

class netErrAdmin(admin.ModelAdmin):
	list_display = ('code', 'des')
	list_per_page = 30
	search_fields = ['code', 'des']

class feelAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'plat')
	list_per_page = 30
	search_fields = ['name', 'url', 'plat']

admin.site.register(Ints, IntsAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
admin.site.register(BuType, BuTypeAdmin)
admin.site.register(secondType, secondTypeAdmin)
admin.site.register(netErr, netErrAdmin)
admin.site.register(feel, feelAdmin)
