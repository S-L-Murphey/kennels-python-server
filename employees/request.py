EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Danny Tamberelli",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Lori Beth Dunberg",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Elaine Benez",
      "locationId": 1
    },
    {
      "name": "George Costanza",
      "locationId": 2,
      "id": 5
    },
    {
      "name": "Jerry Seinfeld",
      "locationId": 1,
      "id": 6
    }
]

def get_all_employees():
    return EMPLOYEES


# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
