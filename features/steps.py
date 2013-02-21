from lettuce import *
from nose.tools import raises
from os import remove

class ApprovalError(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)
		
class Approvals:
	approved_string = ""

	@staticmethod
	def init_verified_string():	
		try:
			remove("test.approved.txt")
			remove("test.received.txt")
		except OSError:
			print("ok")
		
		f = file("test.approved.txt",'w')
		f.write("hello world")
		f.close()
		
	
	@staticmethod	
	def init_string_not_verified():	
		try:
			remove("test.approved.txt")
			remove("test.received.txt")
		except OSError:
			print("ok")
						
		f = file("test.approved.txt",'w')
		f.write("hello")
		f.close()
		
	@staticmethod
	def save_file(text):
		f = file("test.received.txt",'w')
		f.write(text)
		f.close()
	
	@staticmethod
	def verify(text):
		f = file("test.approved.txt",'r')
		Approvals.approved_string = f.read()
		f.close()
		
		if Approvals.approved_string != text:
			Approvals.save_file(text)			
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
	Approvals.init_verified_string()

@step(u'Given "([^"]*)" is not verified')
def given_a_string_is_not_verified(step, a_string):
    Approvals.init_string_not_verified()
	
@step(u'Then There is no error')
def then_there_is_no_error(step):
	Approvals.verify(world.a_string)
	
@step(u'And There is no received file')
@raises(IOError)
def and_there_is_no_received_file(step):
    assert file("test.received.txt")
	

