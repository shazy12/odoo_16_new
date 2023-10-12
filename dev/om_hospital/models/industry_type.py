from odoo import api, fields, models

class InudtryType(models.Model):
    _name= "industrytype"

    industry_type  = fields.Char(string='Name', required=True)