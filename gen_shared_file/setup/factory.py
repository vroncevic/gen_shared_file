# -*- coding: UTF-8 -*-

'''
Module
    factory.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Factory for creating the gen_shared_file bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_shared_file.setup.bundle import GenSharedFileBundle
from gen_shared_file.setup.options import GenSharedFileBundleOptions
from gen_shared_file.setup.registry import GenSharedFileBundleRegistry
from gen_shared_file.setup.dependencies import GenSharedFileBundleDependencies
from gen_shared_file.setup.opt_validator import GenSharedFileBundleOptionsValidator
from gen_shared_file.setup.keys import GenSharedFileBundleKeys
from gen_shared_file.core.service.engine import Service
from gen_shared_file.infrastructure.subprocessor import SubProcessor
from gen_shared_file.infrastructure.cli.engine import CLI
from gen_shared_file.infrastructure.cli.setup.bundle import CLIBundle
from gen_shared_file.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_shared_file.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_shared_file.infrastructure.command.command import CommandBundle
from gen_shared_file.infrastructure.command.gen_shared_file_command_definition import GenSharedFileCommandDefinition
from gen_shared_file.infrastructure.command.gen_shared_file_command_executor import GenSharedFileCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_shared_file'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_shared_file/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenSharedFileBundleFactory:
    '''
        Factory for creating the gen_shared_file bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_shared_file info file.
            :methods:
                | create_bundle - Creates the gen_shared_file bundle with optional pre-configured options.
    '''

    _info_file: str = 'gen_shared_file/infrastructure/config/gen_shared_file.cfg'

    @classmethod
    def create_bundle(cls, options: GenSharedFileBundleOptions | None = None) -> GenSharedFileBundle:
        '''
            Creates the gen_shared_file bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_shared_file bundle.
            :return: The gen_shared_file bundle.
            :exceptions:
                | ATSValueError: The gen_shared_file bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_shared_file bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_shared_file bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_shared_file bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_shared_file bundle must be provided and have proper values.
                | ATSTypeError:  The gen_shared_file bundle must be an instance of GenSharedFileBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenSharedFileBundleOptionsValidator.validate(options)

        info_file = options.get(GenSharedFileBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_shared_file_definition: GenSharedFileCommandDefinition = GenSharedFileCommandDefinition()

        gen_shared_file_bundle: CommandBundle = CommandBundle(
            definition=gen_shared_file_definition,
            executor=GenSharedFileCommandExecutor(gen_shared_file_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_shared_file_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenSharedFileBundleRegistry.create_bundle(
            dependencies=GenSharedFileBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
