from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "name"

    name = fields.Char(
        string="Name",
        required=True
    )
    property_ids = fields.One2many(
        comodel_name='estate.property',
        inverse_name='property_type_id',
        string='Properties'
    )
    sequence = fields.Integer(
        string='Sequence',
        default=1
    )
    offer_ids = fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_type_id',
        string='Offers'
    )
    offer_count = fields.Integer(
        string='Offers',
        compute='_compute_offer_count'
    )

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.property_ids.offer_ids)

    _sql_constraints = [
        (
            'check_name', 'UNIQUE(name)', 'The name must be unique'
        )
    ]