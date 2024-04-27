from odoo import fields, models, api
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float(
        string="Price"
    )
    status = fields.Selection(
        string='Status',
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ],
        copy=False
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=True
    )
    property_id = fields.Many2one(
        comodel_name='estate.property',
        string='Property',
        required=True
    )
    validity = fields.Integer(
        string="Validity",
        default=7
    )
    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        store=True
    )

    @api.depends("validity", "date_deadline")
    def _compute_date_deadline(self):
        for record in self:
            if not record.create_date:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)
            else:
                create_date = fields.Datetime.from_string(record.create_date)
                deadline_date = create_date + timedelta(days=record.validity)
                record.date_deadline = deadline_date.date()

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                deadline_date = fields.Date.from_string(record.date_deadline)
                create_date = fields.Datetime.from_string(record.create_date)
                record.validity = (deadline_date - create_date.date()).days