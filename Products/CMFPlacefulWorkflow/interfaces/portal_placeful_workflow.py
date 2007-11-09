# -*- coding: utf-8 -*-
## CMFPlacefulWorkflow
## Copyright (C)2005 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
Placeful Workflow tool interface.
"""
__version__ = "$Revision$"
# $Source: /cvsroot/ingeniweb/CMFPlacefulWorkflow/interfaces/portal_placeful_workflow.py,v $
# $Id$
__docformat__ = 'restructuredtext'

from Interface import Attribute, Interface

_marker = []


class portal_workflow_policy(Interface):
    '''
    '''
    id = Attribute('id', 'Must be set to "portal_workflow_policy"')

    # security.declarePublic('getMaxChainLength')
    def getMaxChainLength(self):
        """Return the max workflow chain length"""

    # security.declarePublic('getMaxChainLength')
    def setMaxChainLength(self, max_chain_length):
        """Set the max workflow chain length"""


class WorkflowPolicyDefinition(Interface):
    '''
    '''

    pass