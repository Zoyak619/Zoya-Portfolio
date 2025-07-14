from orders_db_app import view_orders_by_status
from unittest.mock import patch

# test view orders by status ID 

# happy case 

def test_happy_view_orders_status_with_results():
    # arrange some test data
    status_id = 1

    # act on our function
    result = view_orders_by_status(status_id)

    # assert the result was correct
       
    assert result is None
   