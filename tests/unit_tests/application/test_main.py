from unittest.mock import patch

from formation_devops.application import main


@patch('formation_devops.application.main.do_cleaning')
def test_main_script_calls_other_functions(do_cleaning):
    main.run()
    assert do_cleaning.called
