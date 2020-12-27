# Week 10 - Testing and TDD

### Known Issues with Task 2

- Had problems asserting database entries
  - Unable to figure out how to assert based on an auto incrementing ID value
  - When executing a test to add a user, was unable to then remove that user as part of the test
  - When attempting to delete a user, had to guess on the ID value to remove and then assert based on that. Feels like I'm missing something, must be another way
  - Tests work when using the existing database, calling Task 2 done; will not be using Flask for Assignment, to figure out how to alter tests to use a test-database would perhaps take a large amount of time and out of scope for this week's tasks, time best spent elsewhere

## Task 1

(Contained in subdirectory "task_1")

- Create a basic class in app.py that has several functions (e.g. calculator)
- Create a file called tests.py
- Write Unit Tests in tests.py that test the following:
  - The class in app.py is instantiated properly
  - All functions in app.py have at least 1 associated  unit test
  - Include a setUp() method with appropriate code
- Upload app.py and tests.py to new GitHub repo

## Task 2

- Create a Selenium script that performs Functional tests on the front-end of an application
- Must include:
  - setUp and tearDown() methods
  - At least 1 test per route/URL endpoint
  - At least 2 different Unit Test assertions e.g. AssertIn and AssertEquals
- Upload selenium_script.py alongside application code to GitHub (ensure you include an updated requirements.txt file)