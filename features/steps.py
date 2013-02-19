from lettuce import *
from nose.tools import raises

@step(u'When I verify "([^"]*)"')
def when_i_verify(step, a_string):
	world.a_string = a_string

@step(u'Then I will get an error')
@raises(Exception)
def then_i_will_get_an_error(step):
	Approvals.verify(world.a_string)

