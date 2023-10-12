from odoo import api, fields, models

class  ResPartnerExtended(models.Model):
    _inherit = 'res.partner'

    custom_field = fields.Char(string='Custom Field')
    password = fields.Char(string='password')