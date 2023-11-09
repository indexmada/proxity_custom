# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductPricelist(models.Model):
	_inherit = "product.pricelist"

	is_proxity_pricelist = fields.Boolean("Carte Proxity")