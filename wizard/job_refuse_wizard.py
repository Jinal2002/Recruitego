from odoo import models, fields, api

class JobRefuse(models.TransientModel):
	_name = 'job.refuse.wizard'
	_description = 'Refuse Wizard'

	refuse_reason = fields.Text(string="Reason:", required=True)
	refuse_by = fields.Many2one('res_users',string="Refused By")

	def action_refuse(self):
		parent_id = self.env.context.get('active_id')
		parent_record = self.env['job.hire'].browse(parent_id)

		parent_record.write({
							'refuse_reason': self.refuse_reason,
							'refuse_by': self.env.user.id,
							'stage': 'refuse'
							})