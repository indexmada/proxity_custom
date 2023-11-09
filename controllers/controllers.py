# -*- coding: utf-8 -*-
from odoo import http

# class ProxityCustom(http.Controller):
#     @http.route('/proxity_custom/proxity_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proxity_custom/proxity_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proxity_custom.listing', {
#             'root': '/proxity_custom/proxity_custom',
#             'objects': http.request.env['proxity_custom.proxity_custom'].search([]),
#         })

#     @http.route('/proxity_custom/proxity_custom/objects/<model("proxity_custom.proxity_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proxity_custom.object', {
#             'object': obj
#         })