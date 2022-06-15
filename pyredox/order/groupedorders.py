# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class GroupedOrders(EventTypeAbstractModel):

    Meta: "GroupedOrdersMeta" = Field(...)
    Orders: List["GroupedOrdersOrder"] = Field(...)
    Patient: "GroupedOrdersPatient" = Field(...)
    Visit: "GroupedOrdersVisit" = Field(None)


class GroupedOrdersMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["GroupedOrdersMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["GroupedOrdersMetaLog"] = Field(None)
    Message: "GroupedOrdersMetaMessage" = Field(None)
    Source: "GroupedOrdersMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "GroupedOrdersMetaTransmission" = Field(None)


class GroupedOrdersMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class GroupedOrdersMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class GroupedOrdersMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class GroupedOrdersMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class GroupedOrdersMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class GroupedOrdersOrder(RedoxAbstractModel):

    ApplicationOrderID: Union[str, None] = Field(None)
    ClinicalInfo: List["GroupedOrdersOrderClinicalInfo"] = Field(None)
    CollectionDateTime: Union[str, None] = Field(None)
    Comments: Union[str, None] = Field(None)
    Diagnoses: List["GroupedOrdersOrderDiagnosis"] = Field(None)
    ID: str = Field(...)
    Notes: List[str] = Field(None)
    OrderingFacility: "GroupedOrdersOrderOrderingFacility" = Field(None)
    Priority: Union[str, None] = Field(None)
    Procedure: "GroupedOrdersOrderProcedure" = Field(None)
    Provider: "GroupedOrdersOrderProvider" = Field(None)
    ResultCopyProviders: List["GroupedOrdersOrderResultCopyProvider"] = Field(None)
    Specimen: "GroupedOrdersOrderSpecimen" = Field(None)
    Status: str = Field(...)
    TransactionDateTime: Union[str, None] = Field(None)


class GroupedOrdersOrderClinicalInfo(RedoxAbstractModel):

    Abbreviation: Union[str, None] = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Units: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class GroupedOrdersOrderDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersOrderOrderingFacility(RedoxAbstractModel):

    Address: "GroupedOrdersOrderOrderingFacilityAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class GroupedOrdersOrderOrderingFacilityAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersOrderProcedure(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class GroupedOrdersOrderProvider(RedoxAbstractModel):

    Address: "GroupedOrdersOrderProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "GroupedOrdersOrderProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "GroupedOrdersOrderProviderPhoneNumber" = Field(None)


class GroupedOrdersOrderProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersOrderProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersOrderProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class GroupedOrdersOrderResultCopyProvider(RedoxAbstractModel):

    Address: "GroupedOrdersOrderResultCopyProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "GroupedOrdersOrderResultCopyProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "GroupedOrdersOrderResultCopyProviderPhoneNumber" = Field(None)


class GroupedOrdersOrderResultCopyProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersOrderResultCopyProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersOrderResultCopyProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class GroupedOrdersOrderSpecimen(RedoxAbstractModel):

    BodySite: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Source: Union[str, None] = Field(None)


class GroupedOrdersPatient(RedoxAbstractModel):

    Demographics: "GroupedOrdersPatientDemographics" = Field(None)
    Identifiers: List["GroupedOrdersPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class GroupedOrdersPatientDemographics(RedoxAbstractModel):

    Address: "GroupedOrdersPatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "GroupedOrdersPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class GroupedOrdersPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class GroupedOrdersPatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class GroupedOrdersVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "GroupedOrdersVisitAttendingProvider" = Field(None)
    ConsultingProvider: "GroupedOrdersVisitConsultingProvider" = Field(None)
    Guarantor: "GroupedOrdersVisitGuarantor" = Field(None)
    Insurances: List["GroupedOrdersVisitInsurance"] = Field(None)
    Location: "GroupedOrdersVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    ReferringProvider: "GroupedOrdersVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class GroupedOrdersVisitAttendingProvider(RedoxAbstractModel):

    Address: "GroupedOrdersVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "GroupedOrdersVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "GroupedOrdersVisitAttendingProviderPhoneNumber" = Field(None)


class GroupedOrdersVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class GroupedOrdersVisitConsultingProvider(RedoxAbstractModel):

    Address: "GroupedOrdersVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "GroupedOrdersVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "GroupedOrdersVisitConsultingProviderPhoneNumber" = Field(None)


class GroupedOrdersVisitConsultingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersVisitConsultingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersVisitConsultingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class GroupedOrdersVisitGuarantor(RedoxAbstractModel):

    Address: "GroupedOrdersVisitGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "GroupedOrdersVisitGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "GroupedOrdersVisitGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "GroupedOrdersVisitGuarantorSpouse" = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersVisitGuarantorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersVisitGuarantorEmployer(RedoxAbstractModel):

    Address: "GroupedOrdersVisitGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class GroupedOrdersVisitGuarantorEmployerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersVisitGuarantorPhoneNumber(RedoxAbstractModel):

    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class GroupedOrdersVisitGuarantorSpouse(RedoxAbstractModel):

    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class GroupedOrdersVisitInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "GroupedOrdersVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "GroupedOrdersVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "GroupedOrdersVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class GroupedOrdersVisitInsuranceCompany(RedoxAbstractModel):

    Address: "GroupedOrdersVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class GroupedOrdersVisitInsuranceCompanyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersVisitInsuranceInsured(RedoxAbstractModel):

    Address: "GroupedOrdersVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["GroupedOrdersVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class GroupedOrdersVisitInsuranceInsuredAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersVisitInsuranceInsuredIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class GroupedOrdersVisitInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersVisitReferringProvider(RedoxAbstractModel):

    Address: "GroupedOrdersVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "GroupedOrdersVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "GroupedOrdersVisitReferringProviderPhoneNumber" = Field(None)


class GroupedOrdersVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class GroupedOrdersVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class GroupedOrdersVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


GroupedOrders.update_forward_refs()
GroupedOrdersMeta.update_forward_refs()
GroupedOrdersOrder.update_forward_refs()
GroupedOrdersOrderOrderingFacility.update_forward_refs()
GroupedOrdersOrderProvider.update_forward_refs()
GroupedOrdersOrderResultCopyProvider.update_forward_refs()
GroupedOrdersPatient.update_forward_refs()
GroupedOrdersPatientDemographics.update_forward_refs()
GroupedOrdersVisit.update_forward_refs()
GroupedOrdersVisitAttendingProvider.update_forward_refs()
GroupedOrdersVisitConsultingProvider.update_forward_refs()
GroupedOrdersVisitGuarantor.update_forward_refs()
GroupedOrdersVisitGuarantorEmployer.update_forward_refs()
GroupedOrdersVisitInsurance.update_forward_refs()
GroupedOrdersVisitInsuranceCompany.update_forward_refs()
GroupedOrdersVisitInsuranceInsured.update_forward_refs()
GroupedOrdersVisitReferringProvider.update_forward_refs()
