# -*- coding: utf-8 -*-
from odoo import http

# class TvpTest(http.Controller):
#     @http.route('/tvp_test/tvp_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tvp_test/tvp_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tvp_test.listing', {
#             'root': '/tvp_test/tvp_test',
#             'objects': http.request.env['tvp_test.tvp_test'].search([]),
#         })

#     @http.route('/tvp_test/tvp_test/objects/<model("tvp_test.tvp_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tvp_test.object', {
#             'object': obj
#         })