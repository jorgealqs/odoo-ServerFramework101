from odoo import fields, models, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(
        string="Name",
        required=True
    )
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(
        string="Date Availability",
        copy=False,
        default=lambda self: datetime.today() + timedelta(days=90)
    )
    expected_price = fields.Float(
        string="Expected Price",
        required=True
    )
    selling_price = fields.Float(
        string="Selling Price",
        readonly=True,
        copy=False
    )
    bedrooms = fields.Integer(
        string="Bedrooms",
        default=2
    )
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")
    active = fields.Boolean(string="Active")
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string="Status", required=True, default='new', copy=False)
    property_type_id = fields.Many2one(
        comodel_name='estate.property.type',
        string='Property Type',
    )
    buyer = fields.Many2one(
        comodel_name="res.partner",
        string="Buyer"
    )
    salesperson = fields.Many2one(
        comodel_name='res.users',
        string='Salesman',
        required=True,
        index=True,
        default=lambda self: self.env.user,
    )
    tag_ids = fields.Many2many(
        comodel_name="estate.property.tag",
        string="Tags"
    )
    offer_ids = fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_id',
        string='Offers'
    )
    total_area = fields.Integer(
        string="Total Area",
        default=0.00,
        compute="_compute_total_area"
    )
    best_price = fields.Float(
        string="Best Price",
        compute="_compute_best_price",
        readonly=True,
    )

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                prices = record.offer_ids.mapped('price')
                if prices:
                    record.best_price = max(prices)
                else:
                    record.best_price = 0.0  # O cualquier valor predeterminado que desees
            else:
                record.best_price = 0.0  # O cualquier valor predeterminado que desees si no hay ofertas


    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.onchange("garden")
    def _onchange_partner_id(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = "north"
            else:
                record.garden_area = False
                record.garden_orientation = False

    def action_sold_property(self):
        for record in self:
            if record.state == "canceled":
                raise UserError("A canceled property cannot be set as sold.")
            record.state = "sold"
    def action_cancel_properety(self):
        for record in self:
            if record.state == "sold":
                raise UserError("A sold property cannot be set as canceled.")
            record.state = "canceled"

