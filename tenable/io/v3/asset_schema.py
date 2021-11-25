"""
Asset API Endpoints Schemas
"""
from marshmallow import Schema, ValidationError, fields
from marshmallow import validate as v
from marshmallow.decorators import post_dump, pre_load


class AssignTagsAssetSchema(Schema):
    """
    Assign Tags API Schema
    """

    assets = fields.List(fields.UUID())
    tags = fields.List(fields.UUID())
    action = fields.String(validate=v.OneOf(["add", "remove"]))


class ImportAssetSchema(Schema):
    """
    Import Asset API Schema
    """

    assets = fields.List(fields.Dict(), validate=v.Length(min=1))
    source = fields.String()

    @pre_load
    def transform_assets(
        self, data, **kwargs
    ):  # pylint: disable=no-self-use, unused-argument
        """
        Transform a Tuple of Assets into a List of Assets and validate each Asset.
        """
        data["assets"] = list(data.get("assets", []))

        if len(data["assets"]) < 1:
            raise ValidationError("Provide at least one asset")

        for asset in data["assets"]:
            if not (
                asset.get("fqdn")
                or asset.get("ipv4")
                or asset.get("netbios_name")
                or asset.get("mac_address")
            ):
                raise ValidationError(
                    (
                        "Each asset object requires a value for at least one of the following"
                        " properties: fqdn, ipv4, netbios_name, mac_address."
                    )
                )
        return data


class MoveAssetSchema(Schema):
    """
    Move Asset API Schema
    """

    source = fields.UUID()
    destination = fields.UUID()
    targets = fields.List(fields.IPv4())

    @post_dump
    def post_serialization(
        self, data, **kwargs
    ):  # pylint: disable=no-self-use, unused-argument
        """
        Convert a list of target assets into a comma-separated string.
        """
        data["targets"] = ",".join(data.get("targets", []))
        return data
