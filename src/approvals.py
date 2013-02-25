from src.filemanager import FileManager
from src.reporter import Reporter;

class Approvals:
	
	def __init__(self, file_mgr, rptr):
		global approved_string, file_manager, reporter
		approved_string = ""
		file_manager = file_mgr
		reporter = rptr
			
	@staticmethod
	def verify(text):
		Approvals(FileManager(), Reporter()).verify_text(text)
			
	def verify_text(self, text):
		approved_string = file_manager.load_approved_string()

		if approved_string != text:
			file_manager.save_approved_file(text)			
			reporter.report()
