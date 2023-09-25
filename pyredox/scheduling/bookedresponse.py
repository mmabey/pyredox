# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class BookedResponse(EventTypeAbstractModel):
    Meta_: BookedResponseMeta = Field(..., alias="Meta")
    Visits_: List[BookedResponseVisit] = Field(..., alias="Visits")


class BookedResponseMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[BookedResponseMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    IsIncomplete_: Union[bool, None] = Field(None, alias="IsIncomplete")
    Logs_: List[BookedResponseMetaLog] = Field(None, alias="Logs")
    Message_: BookedResponseMetaMessage = Field(None, alias="Message")
    Source_: BookedResponseMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: BookedResponseMetaTransmission = Field(None, alias="Transmission")


class BookedResponseMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class BookedResponseMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class BookedResponseMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class BookedResponseMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class BookedResponseMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class BookedResponseVisit(RedoxAbstractModel):
    AccountNumber_: Union[str, None] = Field(None, alias="AccountNumber")
    AdditionalStaff_: List[BookedResponseVisitAdditionalStaff] = Field(
        None, alias="AdditionalStaff"
    )
    AppointmentInfo_: List[BookedResponseVisitAppointmentInfo] = Field(
        None, alias="AppointmentInfo"
    )
    AttendingProvider_: BookedResponseVisitAttendingProvider = Field(
        None, alias="AttendingProvider"
    )
    CancelDateTime_: Union[str, None] = Field(None, alias="CancelDateTime")
    CancelReason_: Union[str, None] = Field(None, alias="CancelReason")
    ConsultingProvider_: BookedResponseVisitConsultingProvider = Field(
        None, alias="ConsultingProvider"
    )
    Diagnoses_: List[BookedResponseVisitDiagnosis] = Field(None, alias="Diagnoses")
    Duration_: float = Field(..., alias="Duration")
    Equipment_: List[BookedResponseVisitEquipment] = Field(None, alias="Equipment")
    Instructions_: List[str] = Field(None, alias="Instructions")
    LastUpdated_: Union[str, None] = Field(None, alias="LastUpdated")
    Location_: BookedResponseVisitLocation = Field(..., alias="Location")
    Patient_: BookedResponseVisitPatient = Field(..., alias="Patient")
    PatientClass_: Union[str, None] = Field(None, alias="PatientClass")
    Reason_: Union[str, None] = Field(None, alias="Reason")
    ReferringProvider_: BookedResponseVisitReferringProvider = Field(
        None, alias="ReferringProvider"
    )
    ScheduledDateTime_: Union[str, None] = Field(None, alias="ScheduledDateTime")
    Status_: Union[str, None] = Field(None, alias="Status")
    Type_: Union[str, None] = Field(None, alias="Type")
    VisitDateTime_: str = Field(..., alias="VisitDateTime")
    VisitNumber_: str = Field(..., alias="VisitNumber")
    VisitProvider_: BookedResponseVisitVisitProvider = Field(
        None, alias="VisitProvider"
    )


class BookedResponseVisitAdditionalStaff(RedoxAbstractModel):
    Address_: BookedResponseVisitAdditionalStaffAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    Duration_: Union[float, None] = Field(None, alias="Duration")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: BookedResponseVisitAdditionalStaffLocation = Field(
        None, alias="Location"
    )
    PhoneNumber_: BookedResponseVisitAdditionalStaffPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Role_: BookedResponseVisitAdditionalStaffRole = Field(None, alias="Role")
    StartDateTime_: Union[str, None] = Field(None, alias="StartDateTime")


class BookedResponseVisitAdditionalStaffAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class BookedResponseVisitAdditionalStaffLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        BookedResponseVisitAdditionalStaffLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        BookedResponseVisitAdditionalStaffLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class BookedResponseVisitAdditionalStaffLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitAdditionalStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class BookedResponseVisitAdditionalStaffRole(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class BookedResponseVisitAppointmentInfo(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    Value_: Union[str, None] = Field(None, alias="Value")


class BookedResponseVisitAttendingProvider(RedoxAbstractModel):
    Address_: BookedResponseVisitAttendingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: BookedResponseVisitAttendingProviderLocation = Field(
        None, alias="Location"
    )
    PhoneNumber_: BookedResponseVisitAttendingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class BookedResponseVisitAttendingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class BookedResponseVisitAttendingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        BookedResponseVisitAttendingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        BookedResponseVisitAttendingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class BookedResponseVisitAttendingProviderLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitAttendingProviderLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class BookedResponseVisitConsultingProvider(RedoxAbstractModel):
    Address_: BookedResponseVisitConsultingProviderAddress = Field(
        None, alias="Address"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: BookedResponseVisitConsultingProviderLocation = Field(
        None, alias="Location"
    )
    PhoneNumber_: BookedResponseVisitConsultingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class BookedResponseVisitConsultingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class BookedResponseVisitConsultingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        BookedResponseVisitConsultingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        BookedResponseVisitConsultingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class BookedResponseVisitConsultingProviderLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitConsultingProviderLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitConsultingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class BookedResponseVisitDiagnosis(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    DocumentedDateTime_: Union[str, None] = Field(None, alias="DocumentedDateTime")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class BookedResponseVisitEquipment(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    Duration_: Union[float, None] = Field(None, alias="Duration")
    StartDateTime_: Union[str, None] = Field(None, alias="StartDateTime")


class BookedResponseVisitLocation(RedoxAbstractModel):
    Department_: str = Field(..., alias="Department")
    DepartmentIdentifiers_: List[
        BookedResponseVisitLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[BookedResponseVisitLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class BookedResponseVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitPatient(RedoxAbstractModel):
    Demographics_: BookedResponseVisitPatientDemographics = Field(
        None, alias="Demographics"
    )
    Identifiers_: List[BookedResponseVisitPatientIdentifier] = Field(
        ..., alias="Identifiers"
    )
    Notes_: List[str] = Field(None, alias="Notes")


class BookedResponseVisitPatientDemographics(RedoxAbstractModel):
    Address_: BookedResponseVisitPatientDemographicsAddress = Field(
        None, alias="Address"
    )
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
    PhoneNumber_: BookedResponseVisitPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class BookedResponseVisitPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class BookedResponseVisitPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class BookedResponseVisitPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class BookedResponseVisitReferringProvider(RedoxAbstractModel):
    Address_: BookedResponseVisitReferringProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: BookedResponseVisitReferringProviderLocation = Field(
        None, alias="Location"
    )
    PhoneNumber_: BookedResponseVisitReferringProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class BookedResponseVisitReferringProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class BookedResponseVisitReferringProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        BookedResponseVisitReferringProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        BookedResponseVisitReferringProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class BookedResponseVisitReferringProviderLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitReferringProviderLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class BookedResponseVisitVisitProvider(RedoxAbstractModel):
    Address_: BookedResponseVisitVisitProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: BookedResponseVisitVisitProviderLocation = Field(None, alias="Location")
    PhoneNumber_: BookedResponseVisitVisitProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class BookedResponseVisitVisitProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class BookedResponseVisitVisitProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        BookedResponseVisitVisitProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        BookedResponseVisitVisitProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class BookedResponseVisitVisitProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitVisitProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class BookedResponseVisitVisitProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


BookedResponse.model_rebuild()
BookedResponseMeta.model_rebuild()
BookedResponseVisit.model_rebuild()
BookedResponseVisitAdditionalStaff.model_rebuild()
BookedResponseVisitAdditionalStaffLocation.model_rebuild()
BookedResponseVisitAttendingProvider.model_rebuild()
BookedResponseVisitAttendingProviderLocation.model_rebuild()
BookedResponseVisitConsultingProvider.model_rebuild()
BookedResponseVisitConsultingProviderLocation.model_rebuild()
BookedResponseVisitLocation.model_rebuild()
BookedResponseVisitPatient.model_rebuild()
BookedResponseVisitPatientDemographics.model_rebuild()
BookedResponseVisitReferringProvider.model_rebuild()
BookedResponseVisitReferringProviderLocation.model_rebuild()
BookedResponseVisitVisitProvider.model_rebuild()
BookedResponseVisitVisitProviderLocation.model_rebuild()
