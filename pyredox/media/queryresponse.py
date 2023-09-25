# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class QueryResponse(EventTypeAbstractModel):
    Media_: List[QueryResponseMedium] = Field(None, alias="Media")
    Meta_: QueryResponseMeta = Field(..., alias="Meta")


class QueryResponseMedium(RedoxAbstractModel):
    CreationDateTime_: Union[str, None] = Field(None, alias="CreationDateTime")
    DocumentDescription_: Union[str, None] = Field(None, alias="DocumentDescription")
    DocumentID_: Union[str, None] = Field(None, alias="DocumentID")
    DocumentType_: Union[str, None] = Field(None, alias="DocumentType")
    FileContents_: Union[str, None] = Field(None, alias="FileContents")
    FileName_: Union[str, None] = Field(None, alias="FileName")
    FileType_: Union[str, None] = Field(None, alias="FileType")
    Patient_: QueryResponseMediumPatient = Field(None, alias="Patient")
    ServiceDateTime_: Union[str, None] = Field(None, alias="ServiceDateTime")
    Visit_: QueryResponseMediumVisit = Field(None, alias="Visit")


class QueryResponseMediumPatient(RedoxAbstractModel):
    Identifiers_: List[QueryResponseMediumPatientIdentifier] = Field(
        None, alias="Identifiers"
    )


class QueryResponseMediumPatientIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseMediumVisit(RedoxAbstractModel):
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class QueryResponseMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[QueryResponseMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[QueryResponseMetaLog] = Field(None, alias="Logs")
    Message_: QueryResponseMetaMessage = Field(None, alias="Message")
    Source_: QueryResponseMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: QueryResponseMetaTransmission = Field(None, alias="Transmission")


class QueryResponseMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class QueryResponseMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class QueryResponseMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class QueryResponseMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class QueryResponseMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


QueryResponse.model_rebuild()
QueryResponseMedium.model_rebuild()
QueryResponseMediumPatient.model_rebuild()
QueryResponseMeta.model_rebuild()
