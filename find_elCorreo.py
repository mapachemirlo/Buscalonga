#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para aderir a Django.
#Claudio Herrera

#año 2011

import sys
import re
import string
import httplib
import urllib2
import re

def StripTags(text):
	finished = 0
	while not finished:
		finished = 1
		start = text.find("<")
		if start >= 0:
			stop = text[start:].find(">")
			if stop >= 0:
				text = text[:start] + text[start+stop+1:]
				finished = 0
	return text
if len(sys.argv) != 2:
	print "\nExtrayendo emails con dos buscadores\n"
	print "\nUsando : ./goog-mail.py <domain-name>\n"
	sys.exit(1)


domain_name=sys.argv[1]
d={}
page_counter = 0
#Podriamos cambiar el valor de la cantidad de paginas, en 50 es poco si los resultados van de 10 en 10 menos en duck.
try:
	while page_counter < 100 :
		results = 'http://groups.google.com/groups?q='+str(domain_name)+'&hl=en&lr=&1e=UTF-8&start='+repr(page_counter) + '&sa=N'

		request = urllib2.Request(results)
		request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)')
		opener = urllib2.build_opener()
		text = opener.open(request).read()
		emails = (re.findall('([\w\.\-]+@'+domain_name+')',StripTags(text)))
		for email in emails:
			d[email]=1
			uniq_emails=d.keys()
		page_counter = page_counter +10
except IOError:
	print "No se pudo conectar a los grupitos"+""

#Vamos con el pato
page_counter = 0
try:
	while page_counter < 100 :
		results = 'https://duckduckgo.com/?q='+str(domain_name)+'duckduckgo&t=h_&ia=web'

		request = urllib2.Request(results)
		request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)')
		opener = urllib2.build_opener()
		text = opener.open(request).read()
		emails = (re.findall('([\w\.\-]+@'+domain_name+')',StripTags(text)))
		for email in emails:
			d[email]=1
			uniq_emails=d.keys()
		page_counter = page_counter +10
except IOError:
	print "No se pudo conectar con los patos"+""


page_counter_web=0
try:
	print "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+""
	print "+       El grandioso buscador & sus grupos:"+""
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n"+""

	while page_counter_web < 100 :
		results_web = 'http://www.google.com/search?q=%40'+str(domain_name)+'&hl=en&lr=UTF-8&start=' + repr(page_counter_web) + '&sa=N'
		request_web = urllib2.Request(results_web)
		request_web.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)')
		opener_web = urllib2.build_opener()
		text = opener_web.open(request_web).read()
		emails_web = (re.findall('([\w\.\-]+@'+domain_name+')',StripTags(text)))
		for email_web in emails_web:
			d[email_web]=1
			uniq_emails_web=d.keys()
		page_counter_web = page_counter_web +10

except IOError:
	print "No se puede conectar, lo lamento!"+""
for uniq_emails_web in d.keys():
	print uniq_emails_web+""




























