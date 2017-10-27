# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, TechVent.net
#    Copyright (C) 2015-2016 TechVent (<http://www.techvent.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# $Revision: 62 $:

{
    'name': 'Vehicle Maintenance',
    'description': 'Vehicle Maintenance',
    'version': '1.0',
    'author': 'TechVent',
    'website': "www.TechVent.Net",
    'depends': ['base','sale'],
    'data': [

        # Inherit View
        'views/mntmenu.xml',
        'views/mntvehicle.xml',
        'views/mntvendor.xml',
        'views/mntvehiclemade.xml',
        'views/mnttype.xml',
        'views/mntvehiclemodel.xml',
        'views/mntactivity.xml',
        
        #'views/user.xml',        
        #'views/user_type.xml',
        #'views/user_position.xml',
        
        # Report
        #'views/report_activity.xml',
        
        # Report Tag Initialization    
        #'ss_reports.xml',    
        
        
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'category': 'Employees',
    'summary' : '<Module Summary>',
    'sequence': 2,
    'price':50,
    'currency':'USD',
    'contributors': '<Module Contributors>',
    'maintainer': '<Module Maintainer>',
    
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
