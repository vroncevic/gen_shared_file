# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenSharedFileBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_shared_file.setup.bundle import GenSharedFileBundle
from gen_shared_file.setup.factory import GenSharedFileBundleFactory


class TestGenSharedFileBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenSharedFileBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenSharedFileBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_shared_file/infrastructure/config/gen_shared_file.cfg'}
        bundle = GenSharedFileBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenSharedFileBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenSharedFileBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenSharedFileBundleFactory.get_version(), '1.0.3')
