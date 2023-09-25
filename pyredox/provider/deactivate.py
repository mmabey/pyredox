# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Deactivate(EventTypeAbstractModel):
    Meta_: DeactivateMeta = Field(..., alias="Meta")
    Providers_: List[DeactivateProvider] = Field(..., alias="Providers")


class DeactivateMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[DeactivateMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[DeactivateMetaLog] = Field(None, alias="Logs")
    Message_: DeactivateMetaMessage = Field(None, alias="Message")
    Source_: DeactivateMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: DeactivateMetaTransmission = Field(None, alias="Transmission")


class DeactivateMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class DeactivateMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class DeactivateMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class DeactivateMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class DeactivateMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class DeactivateProvider(RedoxAbstractModel):
    Demographics_: DeactivateProviderDemographics = Field(None, alias="Demographics")
    Identifiers_: List[DeactivateProviderIdentifier] = Field(..., alias="Identifiers")
    Qualifications_: List[DeactivateProviderQualification] = Field(
        None, alias="Qualifications"
    )
    Roles_: List[DeactivateProviderRole] = Field(None, alias="Roles")


class DeactivateProviderDemographics(RedoxAbstractModel):
    Addresses_: List[DeactivateProviderDemographicsAddress] = Field(
        None, alias="Addresses"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Languages_: List[str] = Field(None, alias="Languages")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: DeactivateProviderDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Sex_: Union[str, None] = Field(None, alias="Sex")


class DeactivateProviderDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    Use_: Union[str, None] = Field(None, alias="Use")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class DeactivateProviderDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class DeactivateProviderIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DeactivateProviderQualification(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    EndDate_: Union[str, None] = Field(None, alias="EndDate")
    Identifiers_: List[DeactivateProviderQualificationIdentifier] = Field(
        None, alias="Identifiers"
    )
    StartDate_: Union[str, None] = Field(None, alias="StartDate")


class DeactivateProviderQualificationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DeactivateProviderRole(RedoxAbstractModel):
    Availability_: List[DeactivateProviderRoleAvailability] = Field(
        None, alias="Availability"
    )
    Identifiers_: List[DeactivateProviderRoleIdentifier] = Field(
        None, alias="Identifiers"
    )
    Locations_: List[DeactivateProviderRoleLocation] = Field(None, alias="Locations")
    Organization_: DeactivateProviderRoleOrganization = Field(
        None, alias="Organization"
    )
    Services_: List[DeactivateProviderRoleService] = Field(None, alias="Services")
    Specialties_: List[DeactivateProviderRoleSpecialty] = Field(
        None, alias="Specialties"
    )


class DeactivateProviderRoleAvailability(RedoxAbstractModel):
    AvailableEndTime_: Union[str, None] = Field(None, alias="AvailableEndTime")
    AvailableStartTime_: Union[str, None] = Field(None, alias="AvailableStartTime")
    Days_: List[str] = Field(None, alias="Days")


class DeactivateProviderRoleIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DeactivateProviderRoleLocation(RedoxAbstractModel):
    Address_: DeactivateProviderRoleLocationAddress = Field(None, alias="Address")
    Description_: Union[str, None] = Field(None, alias="Description")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Identifiers_: List[DeactivateProviderRoleLocationIdentifier] = Field(
        None, alias="Identifiers"
    )
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: DeactivateProviderRoleLocationPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Status_: Union[str, None] = Field(None, alias="Status")


class DeactivateProviderRoleLocationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class DeactivateProviderRoleLocationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DeactivateProviderRoleLocationPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class DeactivateProviderRoleOrganization(RedoxAbstractModel):
    Address_: DeactivateProviderRoleOrganizationAddress = Field(None, alias="Address")
    Identifiers_: List[DeactivateProviderRoleOrganizationIdentifier] = Field(
        None, alias="Identifiers"
    )
    IsActive_: Union[str, None] = Field(None, alias="IsActive")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class DeactivateProviderRoleOrganizationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class DeactivateProviderRoleOrganizationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DeactivateProviderRoleService(RedoxAbstractModel):
    Description_: Union[str, None] = Field(None, alias="Description")
    Identifiers_: List[DeactivateProviderRoleServiceIdentifier] = Field(
        None, alias="Identifiers"
    )
    PhoneNumber_: DeactivateProviderRoleServicePhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Type_: Union[str, None] = Field(None, alias="Type")


class DeactivateProviderRoleServiceIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class DeactivateProviderRoleServicePhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class DeactivateProviderRoleSpecialty(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


Deactivate.model_rebuild()
DeactivateMeta.model_rebuild()
DeactivateProvider.model_rebuild()
DeactivateProviderDemographics.model_rebuild()
DeactivateProviderQualification.model_rebuild()
DeactivateProviderRole.model_rebuild()
DeactivateProviderRoleLocation.model_rebuild()
DeactivateProviderRoleOrganization.model_rebuild()
DeactivateProviderRoleService.model_rebuild()
