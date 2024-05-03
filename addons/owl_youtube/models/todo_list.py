from odoo import api, fields, models

class OWLTodo(models.Model):
    _name = "owl.todo.list"
    _description = "OWL todo list app"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    completed = fields.Boolean(string="Completed")
    color = fields.Char(string="Color")
