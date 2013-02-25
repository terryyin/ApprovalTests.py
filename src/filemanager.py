class FileManager():
		
	def load_approved_string(self):
		f = file("test.approved.txt",'r')
		approved_string = f.read()
		f.close()
		return approved_string
	
	def save_approved_file(self,text):
		f = file("test.received.txt",'w')
		f.write(text)
		f.close()
