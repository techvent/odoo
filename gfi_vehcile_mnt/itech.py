# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Itech REsources
#    Copyright (C) 2015-2016 Itech Resources (<http://www.itechresources.net>).
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


from openerp import models 
from openerp import fields
from openerp import api


# Vehicle Made
class Vehicle_Made(models.Model):
    _name = 'gfi.mntvehiclemade'
    #_inherit = ['mail.thread', 'ir.needaction_mixin']
        
    name=fields.Char(string="Vehicle Made",required=True)    
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Type is Duplicate'),
    ]

# Vehicle Model
class Vehicle_Model(models.Model):
    _name = 'gfi.mntvehiclemodel'
    #_inherit = ['mail.thread', 'ir.needaction_mixin']
        
    name=fields.Char(string="Vehicle Model",required=True)    
    vehiclemade=fields.Many2one('gfi.mntvehiclemade', 'Vehicle Made')
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Type is Duplicate'),
    ]
    
        
# Maintenance Type 
class Mnt_Type(models.Model):
    _name = 'gfi.mnttype'
    #_inherit = ['mail.thread', 'ir.needaction_mixin']
        
    name=fields.Char(string="Maintenance Type",required=True)
    remarks=fields.Char(string="Remarks")    
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Type is Duplicate'),
    ]
    
# Maintenance Vendor
class MntVendor_Class(models.Model):
    _name = 'gfi.mntvendor'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    name=fields.Char(string="Vendor",required=True)   
    address=fields.Char(string="Address")
    phone=fields.Char(string="Phone")
    remarks=fields.Char(string="Remarks")
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Vendor Name is Duplicate'),
    ]
    
# Vehicle 
class Vehicle_Class(models.Model):
    _name = 'gfi.mntvehicle'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    name=fields.Char(string="Registration #") 
    model=fields.Many2one('gfi.mntvehiclemodel', 'Vehicle Model')
    engine=fields.Char(string="Engine #")
    chassis=fields.Char(string="Chassis #")
    horsepower=fields.Char(string="Horse Power")
    color=fields.Char(string="Color")
    belong_to=fields.Char(string="Belongs to")
    model_year=fields.Integer(string="Year of Model")
    
    
    driver_cnic=fields.Char(string="Driver CNIC")
    driver_license=fields.Char(string="Driver License #")
    driver_license_exp=fields.Date(string="Driver License Expiry") 
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Vehicle # is Duplicate'),
    ]
    


# Work Requsition Master
class MntActivity_Class(models.Model):
    _name = 'gfi.mntactivity'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    #name=fields.Char("name")
    datetime=fields.Datetime(string="Date Time" ,required="True", default=fields.Date.today())
    vehicle=fields.Many2one('gfi.mntvehicle', 'Vehicle')
    vendor=fields.Many2one('gfi.mntvendor', 'Vendor')
    type=fields.Many2one('gfi.mnttype', 'Maintenance Type')   
    remarks=fields.Char('Remarks')
    desc=fields.Html('Description')
    expense=fields.Integer('Expense')
            
    mntactivity_line_ids=fields.One2many('gfi.mntactivity.line','mntactivity_line_id','Maintenance Activity Lines')
    

    
# Work Requsition Details / Line Items
class MntActivity_line(models.Model):
    _name='gfi.mntactivity.line'
    
    mntactivity_line_id=fields.Many2one('gfi.mntactivity', 'Maintenance Activity Lines ', ondelete="cascade")
    type=fields.Many2one('gfi.mnttype', 'Maintenance Type')   
    particulars=fields.Char('Particulars')
    remarks=fields.Char('Remarks')
    expense=fields.Integer('Expense')

        
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
