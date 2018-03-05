# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from edi.audiofile.interfaces import IAudiofile
from edi.audiofile.testing import EDI_AUDIOFILE_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class AudiofileIntegrationTest(unittest.TestCase):

    layer = EDI_AUDIOFILE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Audiofile')
        schema = fti.lookupSchema()
        self.assertEqual(IAudiofile, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Audiofile')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Audiofile')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IAudiofile.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Audiofile',
            id='Audiofile',
        )
        self.assertTrue(IAudiofile.providedBy(obj))
