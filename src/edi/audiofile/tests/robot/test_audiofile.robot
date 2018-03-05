# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.audiofile -t test_audiofile.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.audiofile.testing.EDI_AUDIOFILE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_audiofile.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Audiofile
  Given a logged-in site administrator
    and an add audiofile form
   When I type 'My Audiofile' into the title field
    and I submit the form
   Then a audiofile with the title 'My Audiofile' has been created

Scenario: As a site administrator I can view a Audiofile
  Given a logged-in site administrator
    and a audiofile 'My Audiofile'
   When I go to the audiofile view
   Then I can see the audiofile title 'My Audiofile'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add audiofile form
  Go To  ${PLONE_URL}/++add++Audiofile

a audiofile 'My Audiofile'
  Create content  type=Audiofile  id=my-audiofile  title=My Audiofile


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the audiofile view
  Go To  ${PLONE_URL}/my-audiofile
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a audiofile with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the audiofile title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
