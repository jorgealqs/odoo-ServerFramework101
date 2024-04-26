from odoo import fields, models
from datetime import datetime, timedelta

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
