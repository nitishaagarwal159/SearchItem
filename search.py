from flask import Flask,jsonify,request
import PyPDF2
import json
import re
from PyPDF2 import PdfFileMerger , PdfFileReader
app = Flask(__name__)

@app.route('/search',methods=['POST'])
def rea():
	data = json.loads(request.data)
	path = data['path']
	item = data['item']
	pdf_file = open(path,'rb')
	read_pdf = PyPDF2.PdfFileReader(pdf_file)
	pages = read_pdf.getNumPages()
	pageObj = read_pdf.getPage(0)
	text = pageObj.extractText()
	for i in range(1,pages):
		pageObj = read_pdf.getPage(i)
		text += pageObj.extractText()
	text +='\0'	
	if re.search("(\W)"+item+"(\W)",text):
		return jsonify({'message':'1'})
	elif re.search("_"+item+"_",text) :
		return jsonify({'message':'2'})	
	elif re.match(item+"(\W)",text):
		return jsonify({'message':'3'})
	elif re.match(item+"_",text):
		return jsonify({'message':'4'})	
	else:
		return jsonify({'message':'0'})			
	#if item in text:
	#	return jsonify({'message':'1'})
	#else :
	#	return jsonify({'message':'0'})	
	
@app.route('/hello',methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})	

if __name__ == '__main__':
	app.run(debug=True,port=5000)		 			
	
