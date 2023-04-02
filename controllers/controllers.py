# -*- coding: utf-8 -*-
# from odoo import http


# class OdooDataGuied(http.Controller):
#     @http.route('/odoo_data_guide/odoo_data_guide', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_data_guide/odoo_data_guide/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_data_guide.listing', {
#             'root': '/odoo_data_guide/odoo_data_guide',
#             'objects': http.request.env['odoo_data_guide.odoo_data_guide'].search([]),
#         })

#     @http.route('/odoo_data_guide/odoo_data_guide/objects/<model("odoo_data_guide.odoo_data_guide"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_data_guide.object', {
#             'object': obj
#         })
