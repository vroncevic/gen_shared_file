# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class GenSharedFileSetup with attribute(s) and method(s).
     Generate module file generator_test.py by template and parameters.
'''

import sys

try:
    from gen_shared_file.pro.read_template import ReadTemplate
    from gen_shared_file.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2019, https://vroncevic.github.io/gen_shared_file'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_shared_file/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenSharedFileSetup(FileChecking):
    '''
        Defined class GenSharedFileSetup with attribute(s) and method(s).
        Generate module file generator_test.py by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (template, module).
                | __reader - reader API.
                | __writer - writer API.
                | __config - project setup in dict format.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_setup - generate module file setup.py.
                | __str__ - dunder method for GenSharedFileSetup.
    '''

    GEN_VERBOSE = 'GEN_SHARED_FILE::PRO::GEN_SETUP'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(GenSharedFileSetup.GEN_VERBOSE, verbose, 'init setup')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_setup(self, pro_name, verbose=False):
        '''
            Generate module generator_test.py.

            :param pro_name: project name.
            :type pro_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:pro_name', pro_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, setup_content = False, None
        verbose_message(
            GenSharedFileSetup.GEN_VERBOSE, verbose,
            'generating module', pro_name
        )
        template_file, module = 'generator_test.template', 'generator_test.py'
        if bool(template_file):
            setup_content = self.__reader.read(
                template_file, verbose=verbose
            )
            if setup_content:
                status = self.__writer.write(
                    setup_content, pro_name, module, verbose=verbose
                )
        return status

    def __str__(self):
        '''
            Dunder method for GenSharedFileSetup.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__reader), str(self.__writer)
        )
