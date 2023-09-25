# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Deplete(EventTypeAbstractModel):
    Items_: List[DepleteItem] = Field(..., alias="Items")
    Meta_: DepleteMeta = Field(..., alias="Meta")
    Patient_: DepletePatient = Field(None, alias="Patient")
    Visit_: DepleteVisit = Field(None, alias="Visit")


class DepleteItem(RedoxAbstractModel):
    Description_: Union[str, None] = Field(None, alias="Description")
    Identifiers_: List[DepleteItemIdentifier] = Field(..., alias="Identifiers")
    Location_: DepleteItemLocation = Field(None, alias="Location")
    LotNumber_: Union[str, None] = Field(None, alias="LotNumber")
    Notes_: Union[str, None] = Field(None, alias="Notes")
    OrderingProvider_: DepleteItemOrderingProvider = Field(
        None, alias="OrderingProvider"
    )
    Procedure_: DepleteItemProcedure = Field(None, alias="Procedure")
    Quantity_: Union[float, None] = Field(None, alias="Quantity")
    SerialNumber_: Union[str, None] = Field(None, alias="SerialNumber")
    Type_: Union[str, None] = Field(None, alias="Type")
    Units_: Union[str, None] = Field(None, alias="Units")
    UsedQuantity_: Union[float, None] = Field(None, alias="UsedQuantity")
    Vendor_: DepleteItemVendor = Field(None, alias="Vendor")
    WastedQuantity_: Union[float, None] = Field(None, alias="WastedQuantity")


class DepleteItemIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class DepleteItemLocation(RedoxAbstractModel):
    Bin_: Union[str, None] = Field(None, alias="Bin")
    Department_: Union[str, None] = Field(None, alias="Department")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    ID_: Union[str, None] = Field(None, alias="ID")


class DepleteItemOrderingProvider(RedoxAbstractModel):
    Address_: DepleteItemOrderingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: DepleteItemOrderingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: DepleteItemOrderingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class DepleteItemOrderingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class DepleteItemOrderingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        DepleteItemOrderingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        DepleteItemOrderingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class DepleteItemOrderingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DepleteItemOrderingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DepleteItemOrderingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class DepleteItemProcedure(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Modifier_: Union[str, None] = Field(None, alias="Modifier")


class DepleteItemVendor(RedoxAbstractModel):
    CatalogNumber_: Union[str, None] = Field(None, alias="CatalogNumber")
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class DepleteMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[DepleteMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[DepleteMetaLog] = Field(None, alias="Logs")
    Message_: DepleteMetaMessage = Field(None, alias="Message")
    Source_: DepleteMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: DepleteMetaTransmission = Field(None, alias="Transmission")


class DepleteMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class DepleteMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class DepleteMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class DepleteMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class DepleteMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class DepletePatient(RedoxAbstractModel):
    Demographics_: DepletePatientDemographics = Field(None, alias="Demographics")
    Identifiers_: List[DepletePatientIdentifier] = Field(None, alias="Identifiers")
    Notes_: List[str] = Field(None, alias="Notes")


class DepletePatientDemographics(RedoxAbstractModel):
    Address_: DepletePatientDemographicsAddress = Field(None, alias="Address")
    Citizenship_: List[str] = Field(None, alias="Citizenship")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    DeathDateTime_: Union[str, None] = Field(None, alias="DeathDateTime")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    IsDeceased_: Union[bool, None] = Field(None, alias="IsDeceased")
    IsHispanic_: Union[bool, None] = Field(None, alias="IsHispanic")
    Language_: Union[str, None] = Field(None, alias="Language")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MaritalStatus_: Union[str, None] = Field(None, alias="MaritalStatus")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: DepletePatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class DepletePatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class DepletePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class DepletePatientIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DepleteVisit(RedoxAbstractModel):
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


Deplete.model_rebuild()
DepleteItem.model_rebuild()
DepleteItemOrderingProvider.model_rebuild()
DepleteItemOrderingProviderLocation.model_rebuild()
DepleteMeta.model_rebuild()
DepletePatient.model_rebuild()
DepletePatientDemographics.model_rebuild()
