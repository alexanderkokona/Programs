from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])