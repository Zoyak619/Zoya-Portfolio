from valid_phone import get_valid_phone_num
from unittest.mock import patch

# test get valid number 
# happy case 

@patch("builtins.input")
def test_happy_valid_phone(mock_input):
    # arrange some test data
    mock_input.return_value = "07345678945"
    expected = "07345678945"

    # act on our function
    result = get_valid_phone_num()

    # assert the result was correct
       
    assert result == expected
    assert mock_input.call_count == 1

@patch("builtins.input")
def test_happy_phone_start_with_zero(mock_input):
    # test data
    mock_input.return_value= "07123456789"
    expected = "07123456789"
    
    # act on function
    result = get_valid_phone_num()

    # assert the results were correct
        
    assert result == expected
    assert mock_input.call_count == 1

# edge case 

@patch("builtins.input")
def test_unhappy_phone_with_none(mock_input):
    # test data
    mock_input.side_effect=None
    expected = False

    # act
    result = get_valid_phone_num()

    # assert the results were correct
    assert result == expected
    assert mock_input.call_count == 1

# uphappy case 

@patch("builtins.input")
def test_unhappy_phone_with_letters(mock_input):
    # test data
    mock_input.return_value = "0767y765468"
    expected = False

    # act on our function
    result = get_valid_phone_num()

    # assert the results was correct
    assert result == expected
    assert mock_input.call_count == 1

@patch("builtins.input")
def test_unhappy_phone_too_short(mock_input):
    # test data
    mock_input.return_value = "073664563"
    expected = False

    # act on our function
    result = get_valid_phone_num()

    # assert the results was correct
    assert result == expected
    assert mock_input.call_count == 1

@patch("builtins.input")
def test_unhappy_phone_too_long(mock_input):
    # test data
    mock_input.return_value = "073456789098"
    expected = False

    # act on our function
    result = get_valid_phone_num()

    # assert the results was correct
    assert result == expected
    assert mock_input.call_count == 1