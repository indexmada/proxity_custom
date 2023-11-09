# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
	_inherit = "res.partner"

	price_diff_total = fields.Float(string="Total Gain", compute="compute_price_diff")
	price_perte_total = fields.Float(string="Total Perte", compute="compute_price_perte")

	def compute_price_perte(self):
		for record in self:
			pos_order_ids = self.env['pos.order'].search([('partner_id', '=', record.id), ('state', 'in', ['paid', 'done', 'invoiced'])]).filtered(lambda x: x.perte_total > 0)
			result = sum(o.perte_total for o in pos_order_ids)
			record.price_perte_total = result

	def compute_price_diff(self):
		for record in self:
			pos_order_ids = self.env['pos.order'].search([('partner_id', '=', record.id), ('state', 'in', ['paid', 'done', 'invoiced'])]).filtered(lambda x: x.price_diff > 0)
			result = sum(o.price_diff for o in pos_order_ids)
			record.price_diff_total = result

	@api.multi
	def open_price_diff_partner(self):
		context = self._context.copy()
		pos_order_ids = self.env['pos.order'].search([('partner_id', '=', self.id), ('state', 'in', ['paid', 'done', 'invoiced'])]).filtered(lambda x: x.price_diff > 0)
		return {
            'type': 'ir.actions.act_window',
            'name': 'Gain',
            'res_model': 'pos.order',
            'views': [(self.env.ref('proxity_custom.pos_display_gain').id, 'tree')],
            'domain': [('id', 'in', pos_order_ids.ids)],
            'target': 'current',
        }

	@api.multi
	def open_price_perte_partner(self):
		context = self._context.copy()
		pos_order_ids = self.env['pos.order'].search([('partner_id', '=', self.id), ('state', 'in', ['paid', 'done', 'invoiced'])]).filtered(lambda x: x.perte_total > 0)
		return {
            'type': 'ir.actions.act_window',
            'name': 'Perte',
            'res_model': 'pos.order',
            'views': [(self.env.ref('proxity_custom.pos_display_perte').id, 'tree')],
            'domain': [('id', 'in', pos_order_ids.ids)],
            'target': 'current',
        }