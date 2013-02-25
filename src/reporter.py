from src.approvalerror import ApprovalError

class Reporter:
	def report(self):
		raise ApprovalError("not approved yet")
