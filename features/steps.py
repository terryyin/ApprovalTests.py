from lettuce import *
from nose.tools import raises

class ApprovalError(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)

class Approvals:
	approved_string = ""
#for test purpose will be removed when added file support
	@staticmethod
	def init_verified_string(text):
		Approvals.approved_string = text
	
	@staticmethod
	def verify(text):
		if Approvals.approved_string != text:
			f = file("test.received.txt",'w')
			f.write(text)
			f.close()
			raise ApprovalError("not approved yet")

@step(u'When I verify "([^"]*)"')
def when_i_verify(step, a_string):
	world.a_string = a_string

@step(u'Then I will get an error')
@raises(ApprovalError)
def then_i_will_get_an_error(step):
	Approvals.verify(world.a_string)
	
@step(u'And I get a received file')
def and_i_get_a_received_file(step):
    assert file("test.received.txt")

@step(u'Given "([^"]*)" is verified')
def given_a_string_is_verified(step, a_string):
	Approvals.init_verified_string(a_string)
	
@step(u'Then There is no error')
def then_there_is_no_error(step):
	Approvals.verify(world.a_string)
	

