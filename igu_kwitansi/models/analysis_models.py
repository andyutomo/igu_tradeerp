# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tradeTest (models.Model):
    _name="trade.test"
    _description = "Test Module"
    name = fields.Char("Test Model")
    itemcode = fields.Char("Item Code")

class tradeSalesAnalysis (models.Model):
    _name = "trade.sales"
    _description = "Sales Analysis"
    name = fields.Char("Data")
    docentry = fields.Char("Doc Entry")
    docnum  = fields.Char("Doc Num")
    doctype = fields.Char("Doc Type")
    objtype = fields.Char("Object Type")
    groupname = fields.Char("Group Name")
    cardcode = fields.Char("Card Code")
    address = fields.Char("Delivery Address")
    address2 = fields.Char("Bill Address")
    customer  = fields.Char("Customer")
    customer_company = fields.Char("Customer Company")
    docdate = fields.Date("Doc Date")
    imonth = fields.Char("Month(s)")
    moyear= fields.Char("Month(s)")
    iyear = fields.Char("Year(s)")
    sls_in_trx = fields.Char("Sales Person In Transaction")
    slg_in_trx = fields.Char("Sales Group in Transaction")
    sls_in_mtr = fields.Char("Sales Person In Master BP")
    slg_in_mtr = fields.Char("Sales Group in Master")
    itemcode = fields.Char("Item Code")
    itemname = fields.Char("Item Name")
    uom =  fields.Char("UoM")
    u_group = fields.Char("Item Groups")
    u_spegroup = fields.Char("Trading / Special Groups")    
    u_subgroup = fields.Char("Sub Group")
    u_category = fields.Char("Storage Category")
    u_country = fields.Char("Country")
    u_spec = fields.Char("Spec")
    u_grading = fields.Char("Grade")
    u_brand = fields.Char("Brand")
    u_cutting = fields.Char("Cutting")
    quantity = fields.Float("Quantity")
    price = fields.Float("Price")
    linetotal = fields.Float("Line Total")
