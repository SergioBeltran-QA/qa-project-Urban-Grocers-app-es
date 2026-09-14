# Urban Grocers API Testing

Automated REST API testing project developed during the TripleTen QA Engineering Bootcamp.

## Project Overview

The project validates the `name` parameter used when creating product kits in the Urban Grocers application. The automated suite covers valid inputs, boundary values, missing parameters, and invalid data types based on the documented requirements.

## Test Coverage

Nine positive and negative scenarios were automated:

1. Valid kit name containing 1 character
2. Valid kit name containing 511 characters
3. Empty kit name
4. Kit name longer than 511 characters
5. Kit name containing special characters
6. Kit name containing spaces
7. Kit name containing numbers
8. Request without the `name` parameter
9. Invalid data type for `name`

## QA Skills Demonstrated

- REST API testing
- Test-case design
- Equivalence partitioning
- Boundary value analysis
- Positive and negative testing
- JSON payload validation
- HTTP status-code validation
- Defect identification
- Automated assertions
- Reusable API request functions

## Technologies

- Python
- pytest
- Requests
- REST APIs
- JSON
- Git and GitHub
- PyCharm

## Project Structure

- `configuration.py` — server URL and API endpoints
- `data.py` — request bodies and test data
- `sender_stand_request.py` — reusable API request functions
- `create_kit_name_kit_test.py` — automated test scenarios and assertions
- `.gitignore` — excluded local files
- `README.md` — project documentation

## Running the Tests

1. Clone the repository:

```bash
git clone https://github.com/SergioBeltran-QA/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
python -m pip install pytest requests
```

4. Start an Urban Grocers test server through TripleTen and replace `URL_SERVICE` in `configuration.py` with the current server URL.

5. Execute the suite:

```bash
python -m pytest -v
```

## Interpreting the Results

Each test compares the actual API response with the documented expected behavior. A failed assertion may reveal a discrepancy between the implementation and the requirements and should be investigated as a potential defect.

## Notes

The TripleTen server URL stored in the project is temporary and may no longer be active. All names, phone numbers, addresses, and other values are fictional test data.

## Author

**Sergio Beltrán**  
Junior QA Engineer specializing in web, mobile, API, and database testing.

- [GitHub Profile](https://github.com/SergioBeltran-QA)
- [LinkedIn](https://www.linkedin.com/in/sergio-beltr%C3%A1n-/)
