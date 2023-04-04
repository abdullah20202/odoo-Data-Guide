from odoo import api, fields, models


class MyModel(models.Model):
    _name = 'my.module.model'
    _description = 'My Module Model'

    boolean_field = fields.Boolean('Boolean Field')
    integer_field = fields.Integer('Integer Field')
    float_field = fields.Float('Float Field')
    char_field = fields.Char('Char Field')
    text_field = fields.Text('Text Field')
    date_field = fields.Date('Date Field')
    datetime_field = fields.Datetime('Datetime Field')
    binary_field = fields.Binary('Binary Field')
    selection_field = fields.Selection(
        [('option_1', 'Option 1'), ('option_2', 'Option 2')], 'Selection Field')
    reference_field = fields.Reference(
        [('res.partner', 'Partner'), ('res.users', 'User')], 'Reference Field')
    html_field = fields.Html('HTML Field')
    image_field = fields.Binary('Image Field')
    image_filename = fields.Char('Image Filename')
    attachment_field = fields.Binary('Attachment Field')
    attachment_filename = fields.Char('Attachment Filename')
    monetary_field = fields.Monetary(
        'Monetary Field', currency_field='currency_id')
    many2one_field = fields.Many2one('res.partner', 'Many2one Field')
    one2many_field = fields.One2many(
        'my.module.related', 'model_id', 'One2many Field')
    many2many_field = fields.Many2many(
        'my.module.related', 'my_module_model_related_rel', 'model_id', 'related_id', 'Many2many Field')
    related_field = fields.Char('Related Field' , related ='many2one_field.name')
    computed_field = fields.Float(
        'Computed Field', compute='_compute_field', store=True)
    encrypted_field = fields.Char('Encrypted Field' , cryptos="my_cryptos")

    currency_id = fields.Many2one('res.currency', 'Currency')

    @api.depends('integer_field', 'float_field')
    def _compute_field(self):
        for record in self:
            record.computed_field = record.integer_field * record.float_field




class MyRelated(models.Model):
    _name = 'my.module.related'
    _description = 'My Module Related'

    name = fields.Char('Name')
    model_id = fields.Many2one('my.module.model', 'Model')