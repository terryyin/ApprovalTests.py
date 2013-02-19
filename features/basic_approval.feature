Feature: basic scenario
	In order to play with ApprovalTests.py
	As a developer
	I will verify basic text
	
Scenario: No approved yet
	When I verify "hello world"
	Then I will get an error
	