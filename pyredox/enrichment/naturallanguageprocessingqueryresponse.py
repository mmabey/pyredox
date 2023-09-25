# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class NaturalLanguageProcessingQueryResponse(EventTypeAbstractModel):
    Entries_: List[NaturalLanguageProcessingQueryResponseEntry] = Field(
        ..., alias="Entries"
    )
    Meta_: NaturalLanguageProcessingQueryResponseMeta = Field(..., alias="Meta")
    Transaction_: NaturalLanguageProcessingQueryResponseTransaction = Field(
        ..., alias="Transaction"
    )


class NaturalLanguageProcessingQueryResponseEntry(RedoxAbstractModel):
    Category_: NaturalLanguageProcessingQueryResponseEntryCategory = Field(
        ..., alias="Category"
    )
    Concept_: NaturalLanguageProcessingQueryResponseEntryConcept = Field(
        ..., alias="Concept"
    )
    Text_: NaturalLanguageProcessingQueryResponseEntryText = Field(..., alias="Text")


class NaturalLanguageProcessingQueryResponseEntryCategory(RedoxAbstractModel):
    CertaintyScore_: float = Field(..., alias="CertaintyScore")
    Name_: str = Field(..., alias="Name")


class NaturalLanguageProcessingQueryResponseEntryConcept(RedoxAbstractModel):
    CertaintyScore_: float = Field(..., alias="CertaintyScore")
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class NaturalLanguageProcessingQueryResponseEntryText(RedoxAbstractModel):
    Contents_: str = Field(..., alias="Contents")
    Position_: NaturalLanguageProcessingQueryResponseEntryTextPosition = Field(
        ..., alias="Position"
    )


class NaturalLanguageProcessingQueryResponseEntryTextPosition(RedoxAbstractModel):
    BeginOffset_: float = Field(..., alias="BeginOffset")
    EndOffset_: float = Field(..., alias="EndOffset")


class NaturalLanguageProcessingQueryResponseMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[NaturalLanguageProcessingQueryResponseMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[NaturalLanguageProcessingQueryResponseMetaLog] = Field(
        None, alias="Logs"
    )
    Message_: NaturalLanguageProcessingQueryResponseMetaMessage = Field(
        None, alias="Message"
    )
    Source_: NaturalLanguageProcessingQueryResponseMetaSource = Field(
        None, alias="Source"
    )
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: NaturalLanguageProcessingQueryResponseMetaTransmission = Field(
        None, alias="Transmission"
    )


class NaturalLanguageProcessingQueryResponseMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NaturalLanguageProcessingQueryResponseMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class NaturalLanguageProcessingQueryResponseMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class NaturalLanguageProcessingQueryResponseMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NaturalLanguageProcessingQueryResponseMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class NaturalLanguageProcessingQueryResponseTransaction(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    Task_: NaturalLanguageProcessingQueryResponseTransactionTask = Field(
        ..., alias="Task"
    )
    VendorID_: str = Field(..., alias="VendorID")


class NaturalLanguageProcessingQueryResponseTransactionTask(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    Message_: Union[str, None] = Field(None, alias="Message")
    Status_: str = Field(..., alias="Status")


NaturalLanguageProcessingQueryResponse.model_rebuild()
NaturalLanguageProcessingQueryResponseEntry.model_rebuild()
NaturalLanguageProcessingQueryResponseEntryText.model_rebuild()
NaturalLanguageProcessingQueryResponseMeta.model_rebuild()
NaturalLanguageProcessingQueryResponseTransaction.model_rebuild()
