# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PosOrderLine(models.Model):
	_inherit = "pos.order.line"

	price_diff = fields.Float(string="Difference de Prix", compute="compute_price_diff", store=True)

	perte_total = fields.Float(string="Perte", compute="compute_price_total_perte", store=True)

	@api.depends("order_id.pricelist_id" ,"order_id.pricelist_id.is_proxity_pricelist", "order_id.pricelist_id.item_ids", "order_id.pricelist_id.item_ids.applied_on", "order_id.pricelist_id.item_ids.product_id", "order_id.pricelist_id.item_ids.product_tmpl_id",  "order_id.pricelist_id.item_ids.compute_price", "order_id.pricelist_id.item_ids.fixed_price", "order_id.pricelist_id.item_ids.percent_price", "product_id.lst_price", "price_unit")
	def compute_price_total_perte(self):
		for rec in self:
			if rec.product_id.lst_price == rec.price_unit:
				pricelist_perte_ids = self.env['product.pricelist'].search([('active', '=', True), ('is_proxity_pricelist', '=', True)])
				pricelist_item_ids = pricelist_perte_ids.item_ids.filtered(lambda x: rec.product_id == x.product_id and x.applied_on == '0_product_variant') or pricelist_perte_ids.item_ids.filtered(lambda x: rec.product_id.product_tmpl_id == x.product_id.product_tmpl_id and x.applied_on == '1_product') or pricelist_perte_ids.item_ids.filtered(lambda x: x.applied_on not in ['0_product_variant', '1_product'])

				pricelist_item_id = pricelist_item_ids[0] if pricelist_item_ids else False
				if pricelist_item_id:
					if pricelist_item_id.compute_price == 'fixed':
						rec.perte_total = (rec.price_unit - pricelist_item_id.fixed_price)*rec.qty
					elif pricelist_item_id.compute_price == 'percentage':
						rec.perte_total = pricelist_item_id.percent_price * rec.price_unit * rec.qty / 100
					else:
						rec.perte_total = 0
				else: 
					rec.perte_total = 0
			else:
				rec.perte_total = 0

	@api.depends("product_id.lst_price", "price_unit", "order_id.pricelist_id.is_proxity_pricelist")
	def compute_price_diff(self):
		for record in self:
			if record.order_id.pricelist_id.is_proxity_pricelist:
				record.price_diff = (record.product_id.lst_price - record.price_unit) * record.qty
			else:
				record.price_diff = 0

class PosOrder(models.Model):
	_inherit = "pos.order"

	price_diff = fields.Float(string="Difference de Prix", compute="compute_price_diff_order", store=True)
	perte_total = fields.Float(string="Perte", compute="compute_price_total_perte", store=True)

	@api.depends("lines.perte_total")
	def compute_price_total_perte(self):
		for record in self:
			record.perte_total = sum(x.perte_total for x in record.lines)

	@api.depends("lines.price_diff")
	def compute_price_diff_order(self):
		for record in self:
			record.price_diff = sum(x.price_diff for x in record.lines)