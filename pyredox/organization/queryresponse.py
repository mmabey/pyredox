# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class QueryResponse(EventTypeAbstractModel):
    Directory_: str = Field(..., alias="Directory")
    Meta_: QueryResponseMeta = Field(..., alias="Meta")
    Organizations_: List[QueryResponseOrganization] = Field(..., alias="Organizations")
    Paging_: QueryResponsePaging = Field(None, alias="Paging")


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


class QueryResponseOrganization(RedoxAbstractModel):
    Active_: bool = Field(..., alias="Active")
    Address_: QueryResponseOrganizationAddress = Field(None, alias="Address")
    Aliases_: List[str] = Field(None, alias="Aliases")
    Contacts_: List[QueryResponseOrganizationContact] = Field(None, alias="Contacts")
    Identifiers_: List[QueryResponseOrganizationIdentifier] = Field(
        None, alias="Identifiers"
    )
    ManagingOrg_: Union[str, None] = Field(None, alias="ManagingOrg")
    Name_: str = Field(..., alias="Name")
    PartOf_: QueryResponseOrganizationPartOf = Field(None, alias="PartOf")
    Type_: QueryResponseOrganizationType = Field(None, alias="Type")


class QueryResponseOrganizationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class QueryResponseOrganizationContact(RedoxAbstractModel):
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: QueryResponseOrganizationContactPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Purpose_: Union[str, None] = Field(None, alias="Purpose")


class QueryResponseOrganizationContactPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Work_: Union[str, None] = Field(None, alias="Work")


class QueryResponseOrganizationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrganizationPartOf(RedoxAbstractModel):
    Identifier_: QueryResponseOrganizationPartOfIdentifier = Field(
        None, alias="Identifier"
    )


class QueryResponseOrganizationPartOfIdentifier(RedoxAbstractModel):
    System_: Union[str, None] = Field(None, alias="System")
    Type_: Union[str, None] = Field(None, alias="Type")
    Value_: Union[str, None] = Field(None, alias="Value")


class QueryResponseOrganizationType(RedoxAbstractModel):
    System_: Union[str, None] = Field(None, alias="System")
    Value_: Union[str, None] = Field(None, alias="Value")


class QueryResponsePaging(RedoxAbstractModel):
    Count_: Union[float, None] = Field(None, alias="Count")
    Index_: Union[float, None] = Field(None, alias="Index")


QueryResponse.model_rebuild()
QueryResponseMeta.model_rebuild()
QueryResponseOrganization.model_rebuild()
QueryResponseOrganizationContact.model_rebuild()
QueryResponseOrganizationPartOf.model_rebuild()
