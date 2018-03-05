# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.audiofile


class EdiAudiofileLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=edi.audiofile)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.audiofile:default')


EDI_AUDIOFILE_FIXTURE = EdiAudiofileLayer()


EDI_AUDIOFILE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_AUDIOFILE_FIXTURE,),
    name='EdiAudiofileLayer:IntegrationTesting'
)


EDI_AUDIOFILE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_AUDIOFILE_FIXTURE,),
    name='EdiAudiofileLayer:FunctionalTesting'
)


EDI_AUDIOFILE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_AUDIOFILE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EdiAudiofileLayer:AcceptanceTesting'
)
