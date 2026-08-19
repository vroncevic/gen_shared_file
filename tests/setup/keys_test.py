# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenSharedFileBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_shared_file.setup.keys import GenSharedFileBundleKeys


class TestGenSharedFileBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenSharedFileBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenSharedFileBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenSharedFileBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenSharedFileBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenSharedFileBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenSharedFileBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenSharedFileBundleKeys.OPTION_INFO_FILE, opts)
