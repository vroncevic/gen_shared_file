# -*- coding: UTF-8 -*-

'''
Module
    gen_shared_file_test.py
Copyright
    Copyright (C) 2019 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_shared_file is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_shared_file is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class TestGenSharedFile with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenSharedFIle.
Execute
    python3 -m unittest -v gen_shared_file_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from gen_shared_file import GenSharedFile
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_shared_file'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_shared_file/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenSharedFile(TestCase):
    '''
        Defines class TestGenSharedFile with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenSharedFIle.
        GenSharedFIle unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_wrong_args - Test wrong args.
                | test_generate_modules - Test generation of modules.
    '''
    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create (not None)'''
        generator: GenSharedFile = GenSharedFile()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        generator: GenSharedFile = GenSharedFile()
        self.assertFalse(generator.process())

    def test_wrong_args(self) -> None:
        '''Test wrong args'''
        sys.argv.clear()
        sys.argv.insert(0, '-d')
        sys.argv.insert(1, 'myipc')
        generator: GenSharedFile = GenSharedFile()
        self.assertFalse(generator.process())

    def test_generate_modules(self) -> None:
        '''Test generation of modules'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'myipc')
        generator: GenSharedFile = GenSharedFile()
        self.assertTrue(generator.process())


if __name__ == '__main__':
    main()
