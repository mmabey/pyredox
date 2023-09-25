# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class SignOn(EventTypeAbstractModel):
    EmailAddress_: Union[str, None] = Field(None, alias="EmailAddress")
    Expiration_: str = Field(..., alias="Expiration")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    IssuedAt_: str = Field(..., alias="IssuedAt")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Locale_: Union[str, None] = Field(None, alias="Locale")
    Meta_: SignOnMeta = Field(..., alias="Meta")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    Name_: Union[str, None] = Field(None, alias="Name")
    Order_: SignOnOrder = Field(None, alias="Order")
    Patient_: SignOnPatient = Field(None, alias="Patient")
    PhoneNumber_: SignOnPhoneNumber = Field(None, alias="PhoneNumber")
    ProviderSpecialty_: Union[str, None] = Field(None, alias="ProviderSpecialty")
    Subject_: str = Field(..., alias="Subject")
    TimeZone_: Union[str, None] = Field(None, alias="TimeZone")
    UserId_: Union[str, None] = Field(None, alias="UserId")
    Visit_: SignOnVisit = Field(None, alias="Visit")


class SignOnMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[SignOnMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    SessionBaseURL_: Union[str, None] = Field(None, alias="SessionBaseURL")
    SessionID_: Union[str, None] = Field(None, alias="SessionID")
    Source_: SignOnMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")


class SignOnMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class SignOnMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class SignOnOrder(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")


class SignOnPatient(RedoxAbstractModel):
    Demographics_: SignOnPatientDemographics = Field(None, alias="Demographics")
    Identifiers_: List[SignOnPatientIdentifier] = Field(None, alias="Identifiers")


class SignOnPatientDemographics(RedoxAbstractModel):
    Address_: SignOnPatientDemographicsAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: SignOnPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Sex_: Union[str, None] = Field(None, alias="Sex")


class SignOnPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class SignOnPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class SignOnPatientIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class SignOnPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class SignOnVisit(RedoxAbstractModel):
    Location_: SignOnVisitLocation = Field(None, alias="Location")
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class SignOnVisitLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[SignOnVisitLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[SignOnVisitLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class SignOnVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class SignOnVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


SignOn.model_rebuild()
SignOnMeta.model_rebuild()
SignOnPatient.model_rebuild()
SignOnPatientDemographics.model_rebuild()
SignOnVisit.model_rebuild()
SignOnVisitLocation.model_rebuild()
