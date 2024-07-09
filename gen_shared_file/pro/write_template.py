# -*- coding: UTF-8 -*-

'''
Module
    write_template.py
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
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for write a template content with parameters to a file.
'''

import sys
from typing import List, Dict, Optional
from datetime import date
from os import getcwd, chmod, mkdir
from string import Template

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_shared_file'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_shared_file/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileCheck):
    '''
        Defines class WriteTemplate with attribute(s) and method(s).
        Creates an API for write a template content with parameters to a file.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
            :methods:
                | __init__ - Initials WriteTemplate constructor.
                | write - write a template content with parameters to a file.
    '''

    _GEN_VERBOSE = 'GEN_SHARED_FILE::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials WriteTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :excptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init writer'])

    def write(
        self,
        template_content: Dict[str, str],
        pro_name: Optional[str],
        verbose: bool = False
    ) -> bool:
        '''
            Write setup content to file.

            :param template_content: Template content
            :type template_content: <Dict[str, str]>
            :param pro_name: Project name | None
            :type pro_name: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exception: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('dict:template_content', template_content),
            ('str:pro_name', pro_name)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(template_content):
            raise ATSValueError('missing template content')
        if not bool(pro_name):
            raise ATSValueError('missing project name')
        module_pro_dir: str = f'{getcwd()}/{pro_name}/'
        mkdir(module_pro_dir)
        status: bool = False
        for module_name, module_content in template_content.items():
            template: Template = Template(module_content)
            module_path: str = f'{module_pro_dir}{module_name}'
            with open(module_path, 'w', encoding='utf-8') as module_file:
                module_file.write(template.substitute({
                    'PRO_NAME': pro_name,
                    'YEAR': f'{str(date.today().year)}'
                }))
                chmod(module_path, 0o644)
                self.check_path(module_path, verbose)
                self.check_mode('w', verbose)
                self.check_format(
                    module_path, module_path.split('.')[1], verbose
                )
                if self.is_file_ok():
                    status = True
        return status
