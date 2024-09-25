# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _

class JobRequest(models.Model):
    _inherit = 'hr.job'

    request_count = fields.Integer(
        string='Job Request Count',
        compute='_compute_request_count')
    job_ids = fields.One2many('job.hire', "job_role_id")

    @api.depends('department_id')  # Adjust based on the relationship to job.hire
    def _compute_request_count(self):
        for job in self:
            # Replace 'job.hire' with the actual model name, and adjust the domain accordingly
            job.request_count = self.env['job.hire'].search_count([('job_role_id', '=', job.id)])

    def action_open_requests(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'job.hire',
            'name': _('Request'),
            'context': {
                'default_res_model': self._name,
                'default_res_id': self.ids[0],
            },
            'view_mode': 'tree',
            'views': [
                (self.env.ref('recruitego.view_job_hire_tree').id, 'tree')
            ],
            'search_view_id': self.env.ref('recruitego.job_hire_view_search').ids,
            'domain': [
                  ('id', 'in', self.job_ids.ids),
            ],
        }