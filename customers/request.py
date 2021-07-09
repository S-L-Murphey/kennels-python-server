CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "email": "hannah@hall.com"
    },
    {
      "id": 2,
      "name": "Johnny Knoxville",
      "address": "1234 Elm Street",
      "email": "johnny@knoxville.com"
    },
    {
      "id": 3,
      "name": "Bam Margera",
      "address": "1818 West Chester Lane",
      "email": "bam@margera.com"
    },
    {
      "email": "memphis@raines.com",
      "name": "Memphis Raines",
      "id": 4
    }
  ]

def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the customers list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer