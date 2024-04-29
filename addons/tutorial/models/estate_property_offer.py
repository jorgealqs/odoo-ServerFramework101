from odoo import fields, models, api, _
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError



class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"

    DEFAULT_VALIDITY_DAYS = 7
    OFFER_ACCEPTED='offer_accepted'

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
        default=DEFAULT_VALIDITY_DAYS
    )
    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        store=True
    )
    property_type_id  = fields.Many2one(
        comodel_name='estate.property.type',
        string='Property Type',
    )

    _sql_constraints = [
        (
            'check_price', 'CHECK(price > 0)', 'The price must be positive'
        )
    ]
    @api.constrains('date_deadline')
    def _check_date_deadline(self):
        for record in self:
            if record.date_deadline < fields.Date.today():
                raise ValidationError("The end date cannot be set in the past")

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

    def action_offer_accept(self):
        for record in self:
            if record.property_id.offer_ids.filtered(lambda o: o.status == 'accepted' and o.id != record.id):
                raise UserError("This property already has an accepted offer.")
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id.id
            record.property_id.state = self.OFFER_ACCEPTED

    def action_offer_refuse(self):
        for record in self:
            record.status = "refused"