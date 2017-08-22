# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tradeTransType (models.Model):
    _name="trade.transtype"
    _description = "Transaction Type SAP"
    name = fields.Char("Transaction Type")
    transgroup = fields.Char("Transaction Group")
    code = fields.Char("Transaction Code")

class tradeOJDT (models.Model):
    _name="trade.ojdt"
    _description = "Journal Entry Header"
    transid = fields.Integer ()
    name = fields.Char("Jurnal Entry Name")
    number = fields.Integer("Number")
    transtype = fields.Many2one ( "trade.transtype")
    baseref = fields.Integer("Base Ref")
    memo  = fields.Char("Memo")
    ref1 = fields.Char("Ref 1")
    ref2 = fields.Char("ref 2")
    createdby = fields.Integer("Source Transaction")
    duedate = fields.Date("Due Date")
    refdate = fields.Date("Ref Date")
    u_trans_no = fields.Char("Trans No")

class tradeJDT1 (models.Model) :
    _name = "trade.jdt1"
    _description = "Jurnal Entry Line"
    name = fields.Char("Number")
    transid = fields.Integer("Transid ")
    refdate = fields.Date("Ref Date")
    line_id = fields.Integer("Line Id")
    account = fields.Char("Account")
    account_name = fields.Char("Account Name")
    credit = fields.Float("Credit")
    debit = fields.Float("Debit")
    fccredit = fields.Float("FC Credit")
    fcdebit = fields.Float("FC Debit")
    fccurrency = fields.Char("Currency")
    shortname = fields.Char("Short Name")
    contraact = fields.Char("Cont Act")
    linememo = fields.Char("Line Memo")
    transtype = fields.Many2one("trade.transtype")
    profitcode = fields.Char("Dept Code")
    orccode2 = fields.Char("Orc Code")

class tradeOINM (models.Model):
    _name = "trade.oinm"
    _description = "Stock Movement"
    name = fields.Char("Trans Num")
    transtype = fields.Many2one ("trade.transtype")
    createdby = fields.Char("Source Transaction")
    doclinenum = fields.Integer ("Line Number")
    docdate = fields.Date ("Doc Date")
    cardcode = fields.Char("Partner Code")
    ref1 = fields.Char("Ref 1")
    comment = fields.Char("Comment")
    jrnlmemo = fields.Char("Jurnal Memo")
    itemcode = fields.Char("Item Code")
    itemname = fields.Char("Item Name")
    dscription = fields.Char("Item Description")
    inqty = fields.Float("In Qty")
    outqty = fields.Float("Out Qty")
    price = fields.Float("Price")
    currency = fields.Char("Currency")
    calcprice = fields.Float("Calculated Price")