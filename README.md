# axrail

TASK:
You are tasked to code the vending machine logic out using Python Programming Language. In your code, you can have a few drinks as your items with any price (no coin). The customer should be able to insert any notes to buy his preferred drinks. The outcome is to release the least amount of notes back to the customer.

APPROACH
  1. Commqand Line
    a) Create a vending machine object to handle to process.
    b) Plan out flow for vending machine process:
      i  )Insert Money
      ii )Display Items available
      iii)Select Item
      iv ) revieve item and balance.
    c) Create Logic for getting least amount of changed:
      - used greedy algoritm
    d) To be Improved:
      - a way to insert money by notes.
      - persistent data using external file or db.(dictionary is used in this test to show the logic)
      - creating UI using django (in the django branch, incomplete)