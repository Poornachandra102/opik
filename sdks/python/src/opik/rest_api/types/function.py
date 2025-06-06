# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_object_schema import JsonObjectSchema


class Function(UniversalBaseModel):
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    strict: typing.Optional[bool] = None
    parameters: typing.Optional[JsonObjectSchema] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
