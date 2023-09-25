# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class NormalizationQueryResponse(EventTypeAbstractModel):
    Entries_: List[NormalizationQueryResponseEntry] = Field(..., alias="Entries")
    Meta_: NormalizationQueryResponseMeta = Field(..., alias="Meta")


class NormalizationQueryResponseEntry(RedoxAbstractModel):
    Category_: str = Field(..., alias="Category")
    Error_: NormalizationQueryResponseEntryError = Field(None, alias="Error")
    Normalization_: List[NormalizationQueryResponseEntryNormalization] = Field(
        None, alias="Normalization"
    )
    Status_: str = Field(..., alias="Status")
    Submitted_: NormalizationQueryResponseEntrySubmitted = Field(..., alias="Submitted")
    Transaction_: NormalizationQueryResponseEntryTransaction = Field(
        ..., alias="Transaction"
    )


class NormalizationQueryResponseEntryError(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Message_: Union[str, None] = Field(None, alias="Message")


class NormalizationQueryResponseEntryNormalization(RedoxAbstractModel):
    LexicalReference_: NormalizationQueryResponseEntryNormalizationLexicalReference = (
        Field(None, alias="LexicalReference")
    )
    Matches_: List[NormalizationQueryResponseEntryNormalizationMatch] = Field(
        None, alias="Matches"
    )
    Score_: NormalizationQueryResponseEntryNormalizationScore = Field(
        None, alias="Score"
    )


class NormalizationQueryResponseEntryNormalizationLexicalReference(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    DefaultCode_: Union[str, None] = Field(None, alias="DefaultCode")
    DefaultName_: Union[str, None] = Field(None, alias="DefaultName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NormalizationQueryResponseEntryNormalizationMatch(RedoxAbstractModel):
    Codes_: List[NormalizationQueryResponseEntryNormalizationMatchCode] = Field(
        None, alias="Codes"
    )
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Status_: Union[str, None] = Field(None, alias="Status")


class NormalizationQueryResponseEntryNormalizationMatchCode(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    MatchPriority_: Union[str, None] = Field(None, alias="MatchPriority")
    Variants_: List[
        NormalizationQueryResponseEntryNormalizationMatchCodeVariant
    ] = Field(None, alias="Variants")


class NormalizationQueryResponseEntryNormalizationMatchCodeVariant(RedoxAbstractModel):
    ExtendedProperties_: List[
        NormalizationQueryResponseEntryNormalizationMatchCodeVariantExtendedProperty
    ] = Field(None, alias="ExtendedProperties")
    Title_: Union[str, None] = Field(None, alias="Title")
    TitleStatus_: Union[str, None] = Field(None, alias="TitleStatus")
    TitleType_: Union[str, None] = Field(None, alias="TitleType")


class NormalizationQueryResponseEntryNormalizationMatchCodeVariantExtendedProperty(
    RedoxAbstractModel
):
    Category_: Union[str, None] = Field(None, alias="Category")
    Properties_: List[
        NormalizationQueryResponseEntryNormalizationMatchCodeVariantExtendedPropertyProperty
    ] = Field(None, alias="Properties")


class NormalizationQueryResponseEntryNormalizationMatchCodeVariantExtendedPropertyProperty(
    RedoxAbstractModel
):
    Property_: Union[str, None] = Field(None, alias="Property")
    Value_: Union[str, None] = Field(None, alias="Value")


class NormalizationQueryResponseEntryNormalizationScore(RedoxAbstractModel):
    Description_: Union[str, None] = Field(None, alias="Description")
    Value_: Union[float, None] = Field(None, alias="Value")


class NormalizationQueryResponseEntrySubmitted(RedoxAbstractModel):
    Category_: str = Field(..., alias="Category")
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    EntryID_: Union[str, None] = Field(None, alias="EntryID")


class NormalizationQueryResponseEntryTransaction(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    VendorID_: str = Field(..., alias="VendorID")


class NormalizationQueryResponseMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[NormalizationQueryResponseMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[NormalizationQueryResponseMetaLog] = Field(None, alias="Logs")
    Message_: NormalizationQueryResponseMetaMessage = Field(None, alias="Message")
    Source_: NormalizationQueryResponseMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: NormalizationQueryResponseMetaTransmission = Field(
        None, alias="Transmission"
    )


class NormalizationQueryResponseMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NormalizationQueryResponseMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class NormalizationQueryResponseMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class NormalizationQueryResponseMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NormalizationQueryResponseMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


NormalizationQueryResponse.model_rebuild()
NormalizationQueryResponseEntry.model_rebuild()
NormalizationQueryResponseEntryNormalization.model_rebuild()
NormalizationQueryResponseEntryNormalizationMatch.model_rebuild()
NormalizationQueryResponseEntryNormalizationMatchCode.model_rebuild()
NormalizationQueryResponseEntryNormalizationMatchCodeVariant.model_rebuild()
NormalizationQueryResponseEntryNormalizationMatchCodeVariantExtendedProperty.model_rebuild()
NormalizationQueryResponseMeta.model_rebuild()
