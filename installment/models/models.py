# -*- coding: utf-8 -*-

from odoo import models, fields , api


class Installment(models.Model):
    _name = 'installment.installment'
    _description = 'installment.installment'

    name = fields.Char(string='Installment', readonly=True)
    id = fields.Integer(required=True)
    reference = fields.Char()
    state = fields.Selection(
        srting='type',
        selection=[('draft', 'Draft'), ('Open', 'open'), ('Paid', 'paid')]
    )
    date = fields.Datetime(default=lambda self: fields.Datetime.now())

    customer = fields.Many2one('customer.customer', required=True)
    journal = fields.Many2one('journal.journal', required=True)
    account = fields.Many2one('account.account', required=True)
    analytical_account = fields.Many2one('analyticalaccount.analyticalaccount')
    analytical_tags = fields.Many2many('analyticaltags.analyticaltags')

    amount = fields.Float(required=True)
    notes = fields.Text()

    @api.onchange()
    def create_customer(self):
        print("Create Customer")

    @api.onchange()
    def create_payment(self):
        print("Create Payment")

    @api.onchange()
    def create_settlement(self):
        print("Create Settlement")

    @api.onchange()
    def form_submit(self):
        print("Form Submitted")

    @api.onchange()
    def form_reset(self):
        print("Form reset")

    @api.onchange()
    def manager_invoice(self):
        print("Manager Invoice")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
