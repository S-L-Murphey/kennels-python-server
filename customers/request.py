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
      "address": "2021 Eleanor Avenue",
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

def create_customer(customer):
    # Get the id value of the last location in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    customer["id"] = new_id

    # Add the location dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
