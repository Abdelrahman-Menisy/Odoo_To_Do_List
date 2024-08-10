from odoo import models, fields


class ToDo(models.Model):
    _name = 'todo.task'
    _description = 'Task for Todo App'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="TaskName", required=1, tracking=1)
    description = fields.Char(string="Description")
    due_date = fields.Datetime(string="Due Date", required=1, tracking=1)
    status = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('initial', 'Initial')], default='initial', tracking=1)
    assign_to = fields.Many2one('res.users', string="Assigned To", required=1, tracking=1)

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exists in the database.')]

    def new_action(self):
        for rec in self:
            rec.status = 'new'

    def in_progress_action(self):
        for rec in self:
            rec.status = 'in_progress'

    def completed_action(self):
        for rec in self:
            rec.status = 'completed'

