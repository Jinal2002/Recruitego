# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from datetime import datetime

class JobHire(models.Model):
    _name = 'job.hire'
    _description = 'Job Hire'
    _rec_name = 'job_role_id'
    # _inherit = ['mail.thread']

    stage = fields.Selection([
                            ('new', 'New'),
                            ('hr_approve', 'Hr Approval'),
                            ('admin_approve', 'Admin Approval'),
                            ('done', 'Done'),
                            ('refuse', 'Refuse'),
                            ('cancelled', 'Cancelled'),
                            ], string='Stage', required=True, default='new',)

    urgency = fields.Selection([
                                ('normal', 'Normal'),
                                ('within one month', 'Within One Month'),
                                ('urgent', 'Urgent'),
                                ('immediate', 'Immediate'),
                                ], required=True)

    name = fields.Char(
        string="Number",
        required=True, copy=False, readonly=False)
        

    opening = fields.Integer(string="Number of Opening", required=True)
    reason = fields.Text(string="Reason of Post", required=True)
    join_date = fields.Date(string="Expected Joining")
    job_role_id = fields.Many2one('hr.job', string="Job Role", domain="[('department_id', '=', department_id)]")
    department_id = fields.Many2one('hr.department', string="Department", required=True)
    refuse_reason = fields.Text(string="Reason:", required=False, readonly=True)
    refuse_by = fields.Many2one('res.users',string="Refused By", readonly=True)

    def action_new(self):
        return self.write({'stage': 'new',
                            'refuse_reason': "",
                            'refuse_by': False})

    def action_hr_approve(self):
        return self.write({'stage': 'admin_approve'})

    def action_admin_approve(self):
        return self.write({'stage': 'done'})

    def action_refuse(self):
        return self.write({'stage': 'refuse'})

    def action_cancel(self):
        return self.write({'stage': 'cancelled'})

    def action_submit(self):
        return self.write({'stage': 'hr_approve'})

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('job.hire')
        return super().create(vals_list)
        # return self.write(vals_list)
        