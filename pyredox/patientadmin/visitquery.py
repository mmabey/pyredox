# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class VisitQuery(EventTypeAbstractModel):
    Departments_: List[str] = Field(None, alias="Departments")
    Facilities_: List[str] = Field(None, alias="Facilities")
    Meta_: VisitQueryMeta = Field(..., alias="Meta")
    PatientClasses_: List[str] = Field(None, alias="PatientClasses")
    Patients_: List[VisitQueryPatient] = Field(None, alias="Patients")
    VisitNumbers_: List[str] = Field(None, alias="VisitNumbers")
    VisitStartDateTime_: Union[str, None] = Field(None, alias="VisitStartDateTime")
    VisitStatuses_: List[str] = Field(None, alias="VisitStatuses")


class VisitQueryMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[VisitQueryMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[VisitQueryMetaLog] = Field(None, alias="Logs")
    Message_: VisitQueryMetaMessage = Field(None, alias="Message")
    Source_: VisitQueryMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: VisitQueryMetaTransmission = Field(None, alias="Transmission")


class VisitQueryMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class VisitQueryMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class VisitQueryMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class VisitQueryMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class VisitQueryMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class VisitQueryPatient(RedoxAbstractModel):
    Identifiers_: List[VisitQueryPatientIdentifier] = Field(None, alias="Identifiers")


class VisitQueryPatientIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


VisitQuery.model_rebuild()
VisitQueryMeta.model_rebuild()
VisitQueryPatient.model_rebuild()
