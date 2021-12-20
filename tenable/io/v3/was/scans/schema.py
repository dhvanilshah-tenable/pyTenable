from marshmallow import Schema, fields, validate


class ScanStatusSchema(Schema):
    requested_action = fields.Str(
        validate=validate.OneOf(['stop'], error='Value not supported'),
        default='stop'
    )


class ScanReportSchema(Schema):
    content_type = fields.Str(
        allow_none=True,
        validate=validate.OneOf([
            'application/json',
            'application/pdf',
            'text/csv',
            'text/html',
            'text/xml'
        ]),
        default='application/json'
    )


class IteratorSchema(Schema):
    limit = fields.Int(
        allow_none=True,
        default=10,
        validate=validate.Range(min=0, max=200)
    )
    offset = fields.Int(
        allow_none=True,
        default=0
    )
    sort = fields.Str(
        allow_none=True
    )
