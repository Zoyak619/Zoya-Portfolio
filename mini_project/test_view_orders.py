from orders_db_app import view_orders_by_status
from unittest.mock import patch

# test view orders by status ID 

# happy case 
   
@patch("builtins.print")
def test_happy_view_order_by_status(mock_print):
    # Arrange
    status_id = 1 # exisitng data in sql table 

    #act
    view_orders_by_status(status_id)

    # assert
    mock_print.assert_any_call("order_id: 1, name: Sam Smith, status: preparing, courier: deliveroo")

@patch("builtins.print")
def test_happy_view_orders_multiple_matches(mock_print):
    # Arrange
    status_id = 2 # has multiple orders in the test 

    # act 
    view_orders_by_status(status_id)

    #assert
    mock_print.assert_any_call("order_id: 2, name: Fozia Iqbal, status: ready for collection, courier: uber eats")
    mock_print.assert_any_call("order_id: 3, name: Ryan Maddocks, status: ready for collection, courier: just eat")

# unhappy case

@patch("builtins.print")
def test_unhappy_view_order_by_inavlid_status(mock_print):
    # arrange
    status_id = 99 # status id num does not exist 

    # act
    view_orders_by_status(status_id)

    # assert
    mock_print.asssert_any_call("No orders with that status.")

# edge case 
@patch("builtins.print")
def test_edge_view_order_by_empty_status(mock_print):
    # arrange
    status_id = 4 # valid status but linked to no order 

    # act
    view_orders_by_status(status_id)

    # assert
    mock_print.assert_any_call("No orders found with that status.")
     
    