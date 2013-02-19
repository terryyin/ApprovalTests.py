from lettuce import *
from nose.tools import raises

@step(u'When I verify "([^"]*)"')
def when_i_verify(step, new_string):
	world.new_string = new_string

@step(u'Then I will get a error')
@raises(Exception)
def then_i_will_get_a_error(step):
	verify(world.new_string)
	
def verify(text):
	raise Exception
	