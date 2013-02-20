Feature: basic scenario
	In order to play with ApprovalTests.py
	As a developer
	I will verify basic text
	
Scenario: No approved yet
	When I verify "hello world"
	Then I will get an error
	And I get a received file
	
Scenario: approved
	Given "hello world" is verified
	When I verify "hello world"
	Then There is no error

