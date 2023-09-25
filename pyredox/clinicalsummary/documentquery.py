# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class DocumentQuery(EventTypeAbstractModel):
    Document_: DocumentQueryDocument = Field(None, alias="Document")
    Location_: DocumentQueryLocation = Field(None, alias="Location")
    Meta_: DocumentQueryMeta = Field(..., alias="Meta")
    Patient_: DocumentQueryPatient = Field(..., alias="Patient")
    Visit_: DocumentQueryVisit = Field(None, alias="Visit")


class DocumentQueryDocument(RedoxAbstractModel):
    EndDate_: Union[str, None] = Field(None, alias="EndDate")
    StartDate_: Union[str, None] = Field(None, alias="StartDate")
    Types_: List[DocumentQueryDocumentType] = Field(None, alias="Types")


class DocumentQueryDocumentType(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class DocumentQueryLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")


class DocumentQueryMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[DocumentQueryMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[DocumentQueryMetaLog] = Field(None, alias="Logs")
    Message_: DocumentQueryMetaMessage = Field(None, alias="Message")
    Source_: DocumentQueryMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: DocumentQueryMetaTransmission = Field(None, alias="Transmission")


class DocumentQueryMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class DocumentQueryMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class DocumentQueryMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class DocumentQueryMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class DocumentQueryMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class DocumentQueryPatient(RedoxAbstractModel):
    Identifiers_: List[DocumentQueryPatientIdentifier] = Field(..., alias="Identifiers")


class DocumentQueryPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class DocumentQueryVisit(RedoxAbstractModel):
    EndDateTime_: Union[str, None] = Field(None, alias="EndDateTime")
    ID_: Union[str, None] = Field(None, alias="ID")
    StartDateTime_: Union[str, None] = Field(None, alias="StartDateTime")


DocumentQuery.model_rebuild()
DocumentQueryDocument.model_rebuild()
DocumentQueryMeta.model_rebuild()
DocumentQueryPatient.model_rebuild()
