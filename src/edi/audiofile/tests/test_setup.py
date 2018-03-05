# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from edi.audiofile.testing import EDI_AUDIOFILE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that edi.audiofile is properly installed."""

    layer = EDI_AUDIOFILE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edi.audiofile is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edi.audiofile'))

    def test_browserlayer(self):
        """Test that IEdiAudiofileLayer is registered."""
        from edi.audiofile.interfaces import (
            IEdiAudiofileLayer)
        from plone.browserlayer import utils
        self.assertIn(IEdiAudiofileLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDI_AUDIOFILE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['edi.audiofile'])

    def test_product_uninstalled(self):
        """Test if edi.audiofile is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edi.audiofile'))

    def test_browserlayer_removed(self):
        """Test that IEdiAudiofileLayer is removed."""
        from edi.audiofile.interfaces import \
            IEdiAudiofileLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEdiAudiofileLayer, utils.registered_layers())
