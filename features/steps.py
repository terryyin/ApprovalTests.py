from lettuce import *
from nose.tools import raises
from os import remove

from src.approvalerror import ApprovalError
from src.approvals import Approvals

class ApprovalsForTest:
	@staticmethod
	def init_verified_string():	
		ApprovalsForTest.cleanup_test_files()
		ApprovalsForTest.init_verified_file()

	@staticmethod
	def cleanup_test_files():
		try:
			remove("test.approved.txt")
			remove("test.received.txt")
		except OSError:
			print("ok")

	@staticmethod
	def init_verified_file():
		approved_text = "hello world"
		ApprovalsForTest.init_approved_file(approved_text)

	@staticmethod
	def init_not_verified_file():
		not_approved_text = "not approved"
		ApprovalsForTest.init_approved_file(not_approved_text)
		
	@staticmethod
	def init_approved_file(text):
		f = file("test.approved.txt",'w')
		f.write(text)
		f.close()
		
	@staticmethod	
	def init_string_not_verified():	
		ApprovalsForTest.cleanup_test_files()
		ApprovalsForTest.init_not_verified_file()
			
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
	ApprovalsForTest.init_verified_string()

@step(u'Given "([^"]*)" is not verified')
def given_a_string_is_not_verified(step, a_string):
    ApprovalsForTest.init_string_not_verified()
	
@step(u'Then There is no error')
def then_there_is_no_error(step):
	Approvals.verify(world.a_string)
	
@step(u'And There is no received file')
@raises(IOError)
def and_there_is_no_received_file(step):
    assert file("test.received.txt")
	

