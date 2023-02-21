from odoo import models, fields, api


class Customer(models.Model):
    _name = 'customer.customer'
    _description = 'customer.customer'

    name= fields.Char(string="new Customer")
