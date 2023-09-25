# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Activate(EventTypeAbstractModel):
    Meta_: ActivateMeta = Field(..., alias="Meta")
    Providers_: List[ActivateProvider] = Field(..., alias="Providers")


class ActivateMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[ActivateMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[ActivateMetaLog] = Field(None, alias="Logs")
    Message_: ActivateMetaMessage = Field(None, alias="Message")
    Source_: ActivateMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: ActivateMetaTransmission = Field(None, alias="Transmission")


class ActivateMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class ActivateMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class ActivateMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class ActivateMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class ActivateMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class ActivateProvider(RedoxAbstractModel):
    Demographics_: ActivateProviderDemographics = Field(None, alias="Demographics")
    Identifiers_: List[ActivateProviderIdentifier] = Field(..., alias="Identifiers")
    Qualifications_: List[ActivateProviderQualification] = Field(
        None, alias="Qualifications"
    )
    Roles_: List[ActivateProviderRole] = Field(None, alias="Roles")


class ActivateProviderDemographics(RedoxAbstractModel):
    Addresses_: List[ActivateProviderDemographicsAddress] = Field(
        None, alias="Addresses"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Languages_: List[str] = Field(None, alias="Languages")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: ActivateProviderDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Sex_: Union[str, None] = Field(None, alias="Sex")


class ActivateProviderDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    Use_: Union[str, None] = Field(None, alias="Use")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class ActivateProviderDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class ActivateProviderIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ActivateProviderQualification(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    EndDate_: Union[str, None] = Field(None, alias="EndDate")
    Identifiers_: List[ActivateProviderQualificationIdentifier] = Field(
        None, alias="Identifiers"
    )
    StartDate_: Union[str, None] = Field(None, alias="StartDate")


class ActivateProviderQualificationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ActivateProviderRole(RedoxAbstractModel):
    Availability_: List[ActivateProviderRoleAvailability] = Field(
        None, alias="Availability"
    )
    Identifiers_: List[ActivateProviderRoleIdentifier] = Field(
        None, alias="Identifiers"
    )
    Locations_: List[ActivateProviderRoleLocation] = Field(None, alias="Locations")
    Organization_: ActivateProviderRoleOrganization = Field(None, alias="Organization")
    Services_: List[ActivateProviderRoleService] = Field(None, alias="Services")
    Specialties_: List[ActivateProviderRoleSpecialty] = Field(None, alias="Specialties")


class ActivateProviderRoleAvailability(RedoxAbstractModel):
    AvailableEndTime_: Union[str, None] = Field(None, alias="AvailableEndTime")
    AvailableStartTime_: Union[str, None] = Field(None, alias="AvailableStartTime")
    Days_: List[str] = Field(None, alias="Days")


class ActivateProviderRoleIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ActivateProviderRoleLocation(RedoxAbstractModel):
    Address_: ActivateProviderRoleLocationAddress = Field(None, alias="Address")
    Description_: Union[str, None] = Field(None, alias="Description")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Identifiers_: List[ActivateProviderRoleLocationIdentifier] = Field(
        None, alias="Identifiers"
    )
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: ActivateProviderRoleLocationPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Status_: Union[str, None] = Field(None, alias="Status")


class ActivateProviderRoleLocationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class ActivateProviderRoleLocationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ActivateProviderRoleLocationPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class ActivateProviderRoleOrganization(RedoxAbstractModel):
    Address_: ActivateProviderRoleOrganizationAddress = Field(None, alias="Address")
    Identifiers_: List[ActivateProviderRoleOrganizationIdentifier] = Field(
        None, alias="Identifiers"
    )
    IsActive_: Union[str, None] = Field(None, alias="IsActive")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class ActivateProviderRoleOrganizationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class ActivateProviderRoleOrganizationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ActivateProviderRoleService(RedoxAbstractModel):
    Description_: Union[str, None] = Field(None, alias="Description")
    Identifiers_: List[ActivateProviderRoleServiceIdentifier] = Field(
        None, alias="Identifiers"
    )
    PhoneNumber_: ActivateProviderRoleServicePhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Type_: Union[str, None] = Field(None, alias="Type")


class ActivateProviderRoleServiceIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ActivateProviderRoleServicePhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class ActivateProviderRoleSpecialty(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


Activate.model_rebuild()
ActivateMeta.model_rebuild()
ActivateProvider.model_rebuild()
ActivateProviderDemographics.model_rebuild()
ActivateProviderQualification.model_rebuild()
ActivateProviderRole.model_rebuild()
ActivateProviderRoleLocation.model_rebuild()
ActivateProviderRoleOrganization.model_rebuild()
ActivateProviderRoleService.model_rebuild()
