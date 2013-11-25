
from desktop.lib.django_util import render

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from data_demo.forms import DataUploadForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from data_demo import settings

from django.contrib.sessions.backends.db import SessionStore

import thread
import urllib
import os
import time

s = SessionStore ()
s['viz_type'] = 'bar_v'
base_path = settings.STATIC_URL
#base_path = '/home/rama/Desktop/CloudMajorProject/data_demo/src/data_demo/static'
base_path = '.'
delim = ','


def index(request):
  return render('index.html', request, dict())
  
def data_upload (request):
	print 'Uploading data..'
	if request.method == 'POST':
		s ['file_format'] = request.POST ['file_format']
		if s['file_format'] == 'tsv':
			delim = '\t'
		form = DataUploadForm (request.POST, request.FILES)
		if form.is_valid ():	
			if 'file_desc' in request.POST:
				file_desc = request.POST ['file_desc'].strip ()
				if len (file_desc) > 0:
					s['file_desc'] = file_desc
			print 'saving file...'
			data_file = request.FILES ['data_file']
			thread.start_new_thread (store_uploaded_file, (data_file,) )
		return redirect ('/data_demo/choose_viz/')
	else:
		form = DataUploadForm ()
	#return render_to_response ('data_upload.html', {'form' : form}, context_instance = RequestContext (request))
	return render ('data_upload.html', request, {'form' : form})
  
def store_uploaded_file (data_file):
	print 'File stored'
	data_file_path = default_storage.save (base_path + '/uploads/' + data_file.name, ContentFile (data_file.read()))
	fileName = data_file_path
	s['data_file_name'] = data_file.name
	command = "hdfs dfs -put %s /user/hdfs/" % fileName
	os.system (command)
	
	
	print 'File %s stored at %s' % (data_file.name, data_file_path)    
  
def choose_viz (request):
	return render ('choose_viz.html', request, dict ())
	
def visualization (request):
	s['viz_type'] = '' + request.GET ['viz']
	data_file_name = s['data_file_name']
	
	#accessing from HDFS
	webhdfs = request.fs
	
	time.sleep (1)
	
	data_file = webhdfs.open ('./user/hdfs/' + data_file_name, 'r')
	
	header = data_file.read ().split('\n')[0].split ('\t')
	print header
	data_file.close ()
	no_of_columns = len (header)
	print data_file_name
	data_file_name = 'http://localhost:8000/filebrowser/download/user/hdfs/' + data_file_name
	
	if no_of_columns > 2:
		if s['viz_type'] == 'bar_v':
			return render ('stacked_bar_v.html', request, {'data_file_name' : data_file_name, 'file_format' : s['file_format']})
		if s['viz_type'] == 'bar_h':
			return render ('stacked_bar_h.html', request, {'data_file_name' : data_file_name, 'file_format' : s['file_format']})
	else:
		if s['viz_type'] == 'bar_v':
			return render ('bar_v.html', request, {'data_file_name' : data_file_name, 'file_format' : s['file_format']})
		if s['viz_type'] == 'bar_h':
			return render ('bar_h.html', request, {'data_file_name' : data_file_name, 'file_format' : s['file_format']})
		if s['viz_type'] == 'pie':
			return render ('pie.html', request, {'data_file_name' : data_file_name, 'file_format' : s['file_format']})
		if s['viz_type'] == 'line':
			return render ('line_chart.html', request, {'data_file_name' : data_file_name, 'file_format' : s['file_format']})
		if s['viz_type'] == 'word_cloud':
			return render ('word_cloud.html', request, {'data_file_name' : data_file_name, 'file_format' : s['file_format']})
