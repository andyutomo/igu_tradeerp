# -*- coding: utf-8 -*-
from odoo import http

# class Addons/iguTradeerp/(http.Controller):
#     @http.route('/addons/igu_tradeerp//addons/igu_tradeerp//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/igu_tradeerp//addons/igu_tradeerp//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/igu_tradeerp/.listing', {
#             'root': '/addons/igu_tradeerp//addons/igu_tradeerp/',
#             'objects': http.request.env['addons/igu_tradeerp/.addons/igu_tradeerp/'].search([]),
#         })

#     @http.route('/addons/igu_tradeerp//addons/igu_tradeerp//objects/<model("addons/igu_tradeerp/.addons/igu_tradeerp/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/igu_tradeerp/.object', {
#             'object': obj
#         })