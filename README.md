# Urban Grocers Project

## Project Description

This project contains automated API tests for the Urban Grocers application.

The objective is to verify the behavior of the name parameter when creating product kits through the Urban Grocers API. The test suite covers both positive and negative scenarios based on the requirements provided in the project specification.

## Tested Scenarios

### The following validations were automated:

1. Valid kit name with 1 character 
2. Valid kit name with 511 characters
3. Empty kit name
4. Kit name longer than 511 characters 
5. Special characters in the kit name 
6. Spaces in the kit name 
7. Numeric characters in the kit name 
8. Missing name parameter 
9. Invalid data type for name

## Technologies Used
- Python
- Pytest
- Requests
- Git
- GitHub
- PyCharm

## Project Structure

- .gitignore
- configuration.py – API URLs and endpoints
- create_kit_name_kit_test.py – Automated test cases
- data.py – Request bodies and test data
- README.md
- sender_stand_request.py – API request functions

## Running the Tests

1. Clone the repository.
2. Open the project in PyCharm.
3. Create and activate a virtual environment.
4. Install dependencies:

#### pip install requests pytest

5. Update the server URL in configuration.py.
6. Run the test suite:

pytest -v

## Notes

The automated tests compare the actual API behavior against the expected behavior defined in the documentation.

Some test cases may fail because the API behavior differs from the documented requirements. These failures represent defects identified during the QA testing process.