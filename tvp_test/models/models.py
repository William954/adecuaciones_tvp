# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrExpenses(models.Model):
    _inherit = 'hr.expense'

    @api.depends('sheet_id', 'sheet_id.account_move_id', 'sheet_id.state')
    def _compute_state(self):
        for expense in self:
            if not expense.sheet_id or expense.sheet_id.state == 'draft':
                expense.state = "draft"
            elif expense.sheet_id.state == "cancel":
                expense.state = "refused"
            elif expense.sheet_id.state == "finance_app" or expense.sheet_id.state == "post":
                expense.state = "finance_app"
            elif not expense.sheet_id.account_move_id:
                expense.state = "reported"
            else:
                expense.state = "done"
    
