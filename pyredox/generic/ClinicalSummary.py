# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import clinicalsummary
from ..abstract_base import GenericRedoxAbstractModel
from . import types as generic


class _ClinicalSummary(GenericRedoxAbstractModel):
    _redox_module = clinicalsummary


class DocumentGet(_ClinicalSummary):

    Document: generic.Document = Field(...)
    Meta: generic.Meta = Field(...)


class DocumentGetResponse(_ClinicalSummary):

    Data: str = Field(...)
    Document: generic.Document = Field(...)
    FileType: str = Field(...)
    Meta: generic.Meta = Field(...)


class DocumentQuery(_ClinicalSummary):

    Document: generic.Document = Field(None)
    Location: generic.Location = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class DocumentQueryResponse(_ClinicalSummary):

    Documents: List[generic.Document] = Field(...)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)


class PatientPush(_ClinicalSummary):

    AdvanceDirectives: List[generic.AdvanceDirective] = Field(None)
    AdvanceDirectivesText: Union[str, None] = Field(None)
    Allergies: List[generic.Allergy] = Field(None)
    AllergyText: Union[str, None] = Field(None)
    Encounters: List[generic.Encounter] = Field(None)
    EncountersText: Union[str, None] = Field(None)
    FamilyHistory: List[generic.FamilyHistory] = Field(None)
    FamilyHistoryText: Union[str, None] = Field(None)
    FunctionalStatus: generic.FunctionalStatus = Field(None)
    FunctionalStatusText: Union[str, None] = Field(None)
    Goals: List[generic.Goal] = Field(None)
    GoalsText: Union[str, None] = Field(None)
    Header: generic.Header = Field(None)
    HealthConcerns: List[generic.HealthConcern] = Field(None)
    HealthConcernsText: Union[str, None] = Field(None)
    Immunizations: List[generic.Immunization] = Field(None)
    ImmunizationText: Union[str, None] = Field(None)
    Insurances: List[generic.Insurance] = Field(None)
    InsurancesText: Union[str, None] = Field(None)
    MedicalEquipment: List[generic.MedicalEquipment] = Field(None)
    MedicalEquipmentText: Union[str, None] = Field(None)
    MedicalHistoryText: Union[str, None] = Field(None)
    Medications: List[generic.Medication] = Field(None)
    MedicationsText: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    NoteSections: List[generic.NoteSection] = Field(None)
    PlanOfCare: generic.PlanOfCare = Field(None)
    PlanOfCareText: Union[str, None] = Field(None)
    Problems: List[generic.Problem] = Field(None)
    ProblemsText: Union[str, None] = Field(None)
    Procedures: generic.Procedures = Field(None)
    ProceduresText: Union[str, None] = Field(None)
    ResolvedProblems: List[generic.ResolvedProblem] = Field(None)
    ResolvedProblemsText: Union[str, None] = Field(None)
    Results: List[generic.Result] = Field(None)
    ResultText: Union[str, None] = Field(None)
    SocialHistory: generic.SocialHistory = Field(None)
    SocialHistoryText: Union[str, None] = Field(None)
    VitalSigns: List[generic.VitalSign] = Field(None)
    VitalSignsText: Union[str, None] = Field(None)


class PatientQuery(_ClinicalSummary):

    Location: generic.Location = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)


class PatientQueryResponse(_ClinicalSummary):

    AdvanceDirectives: List[generic.AdvanceDirective] = Field(None)
    AdvanceDirectivesText: Union[str, None] = Field(None)
    Allergies: List[generic.Allergy] = Field(None)
    AllergyText: Union[str, None] = Field(None)
    Encounters: List[generic.Encounter] = Field(None)
    EncountersText: Union[str, None] = Field(None)
    FamilyHistory: List[generic.FamilyHistory] = Field(None)
    FamilyHistoryText: Union[str, None] = Field(None)
    FunctionalStatus: generic.FunctionalStatus = Field(None)
    FunctionalStatusText: Union[str, None] = Field(None)
    Goals: List[generic.Goal] = Field(None)
    GoalsText: Union[str, None] = Field(None)
    Header: generic.Header = Field(None)
    HealthConcerns: List[generic.HealthConcern] = Field(None)
    HealthConcernsText: Union[str, None] = Field(None)
    Immunizations: List[generic.Immunization] = Field(None)
    ImmunizationText: Union[str, None] = Field(None)
    Insurances: List[generic.Insurance] = Field(None)
    InsurancesText: Union[str, None] = Field(None)
    MedicalEquipment: List[generic.MedicalEquipment] = Field(None)
    MedicalEquipmentText: Union[str, None] = Field(None)
    Medications: List[generic.Medication] = Field(None)
    MedicationsText: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    PlanOfCare: generic.PlanOfCare = Field(None)
    PlanOfCareText: Union[str, None] = Field(None)
    Problems: List[generic.Problem] = Field(None)
    ProblemsText: Union[str, None] = Field(None)
    Procedures: generic.Procedures = Field(None)
    ProceduresText: Union[str, None] = Field(None)
    ResolvedProblems: List[generic.ResolvedProblem] = Field(None)
    ResolvedProblemsText: Union[str, None] = Field(None)
    Results: List[generic.Result] = Field(None)
    ResultText: Union[str, None] = Field(None)
    SocialHistory: generic.SocialHistory = Field(None)
    SocialHistoryText: Union[str, None] = Field(None)
    VitalSigns: List[generic.VitalSign] = Field(None)
    VitalSignsText: Union[str, None] = Field(None)


class VisitPush(_ClinicalSummary):

    AdmissionDiagnosis: List[generic.AdmissionDiagnosis] = Field(None)
    AdmissionDiagnosisText: Union[str, None] = Field(None)
    AdvanceDirectives: List[generic.AdvanceDirective] = Field(None)
    AdvanceDirectivesText: Union[str, None] = Field(None)
    Allergies: List[generic.Allergy] = Field(None)
    AllergyText: Union[str, None] = Field(None)
    Assessment: generic.Assessment = Field(None)
    AssessmentText: Union[str, None] = Field(None)
    ChiefComplaintText: Union[str, None] = Field(None)
    DischargeDiagnosis: List[generic.DischargeDiagnosis] = Field(None)
    DischargeDiagnosisText: Union[str, None] = Field(None)
    DischargeMedications: List[generic.DischargeMedication] = Field(None)
    DischargeMedicationsText: Union[str, None] = Field(None)
    Encounters: List[generic.Encounter] = Field(None)
    EncountersText: Union[str, None] = Field(None)
    FamilyHistory: List[generic.FamilyHistory] = Field(None)
    FamilyHistoryText: Union[str, None] = Field(None)
    FunctionalStatus: generic.FunctionalStatus = Field(None)
    FunctionalStatusText: Union[str, None] = Field(None)
    Goals: List[generic.Goal] = Field(None)
    GoalsText: Union[str, None] = Field(None)
    Header: generic.Header = Field(None)
    HealthConcerns: List[generic.HealthConcern] = Field(None)
    HealthConcernsText: Union[str, None] = Field(None)
    HistoryOfPresentIllnessText: Union[str, None] = Field(None)
    Immunizations: List[generic.Immunization] = Field(None)
    ImmunizationText: Union[str, None] = Field(None)
    InstructionsText: Union[str, None] = Field(None)
    Insurances: List[generic.Insurance] = Field(None)
    InsurancesText: Union[str, None] = Field(None)
    InterventionsText: Union[str, None] = Field(None)
    MedicalEquipment: List[generic.MedicalEquipment] = Field(None)
    MedicalEquipmentText: Union[str, None] = Field(None)
    MedicalHistoryText: Union[str, None] = Field(None)
    Medications: List[generic.Medication] = Field(None)
    MedicationsAdministered: List[generic.MedicationsAdministered] = Field(None)
    MedicationsAdministeredText: Union[str, None] = Field(None)
    MedicationsText: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    NoteSections: List[generic.NoteSection] = Field(None)
    ObjectiveText: Union[str, None] = Field(None)
    PhysicalExamText: Union[str, None] = Field(None)
    PlanOfCare: generic.PlanOfCare = Field(None)
    PlanOfCareText: Union[str, None] = Field(None)
    Problems: List[generic.Problem] = Field(None)
    ProblemsText: Union[str, None] = Field(None)
    Procedures: generic.Procedures = Field(None)
    ProceduresText: Union[str, None] = Field(None)
    ReasonForReferralText: Union[str, None] = Field(None)
    ReasonForVisit: List[generic.ReasonForVisit] = Field(None)
    ReasonForVisitText: Union[str, None] = Field(None)
    ResolvedProblems: List[generic.ResolvedProblem] = Field(None)
    ResolvedProblemsText: Union[str, None] = Field(None)
    Results: List[generic.Result] = Field(None)
    ResultText: Union[str, None] = Field(None)
    ReviewOfSystemsText: Union[str, None] = Field(None)
    SocialHistory: generic.SocialHistory = Field(None)
    SocialHistoryText: Union[str, None] = Field(None)
    SubjectiveText: Union[str, None] = Field(None)
    VitalSigns: List[generic.VitalSign] = Field(None)
    VitalSignsText: Union[str, None] = Field(None)


class VisitQuery(_ClinicalSummary):

    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class VisitQueryResponse(_ClinicalSummary):

    AdmissionDiagnosis: List[generic.AdmissionDiagnosis] = Field(None)
    AdmissionDiagnosisText: Union[str, None] = Field(None)
    AdvanceDirectives: List[generic.AdvanceDirective] = Field(None)
    AdvanceDirectivesText: Union[str, None] = Field(None)
    Allergies: List[generic.Allergy] = Field(None)
    AllergyText: Union[str, None] = Field(None)
    Assessment: generic.Assessment = Field(None)
    AssessmentText: Union[str, None] = Field(None)
    ChiefComplaintText: Union[str, None] = Field(None)
    DischargeDiagnosis: List[generic.DischargeDiagnosis] = Field(None)
    DischargeDiagnosisText: Union[str, None] = Field(None)
    DischargeMedications: List[generic.DischargeMedication] = Field(None)
    DischargeMedicationsText: Union[str, None] = Field(None)
    Encounters: List[generic.Encounter] = Field(None)
    EncountersText: Union[str, None] = Field(None)
    FamilyHistory: List[generic.FamilyHistory] = Field(None)
    FamilyHistoryText: Union[str, None] = Field(None)
    FunctionalStatus: generic.FunctionalStatus = Field(None)
    FunctionalStatusText: Union[str, None] = Field(None)
    Goals: List[generic.Goal] = Field(None)
    GoalsText: Union[str, None] = Field(None)
    Header: generic.Header = Field(None)
    HealthConcerns: List[generic.HealthConcern] = Field(None)
    HealthConcernsText: Union[str, None] = Field(None)
    HistoryOfPresentIllnessText: Union[str, None] = Field(None)
    Immunizations: List[generic.Immunization] = Field(None)
    ImmunizationText: Union[str, None] = Field(None)
    InstructionsText: Union[str, None] = Field(None)
    Insurances: List[generic.Insurance] = Field(None)
    InsurancesText: Union[str, None] = Field(None)
    InterventionsText: Union[str, None] = Field(None)
    MedicalEquipment: List[generic.MedicalEquipment] = Field(None)
    MedicalEquipmentText: Union[str, None] = Field(None)
    Medications: List[generic.Medication] = Field(None)
    MedicationsAdministered: List[generic.MedicationsAdministered] = Field(None)
    MedicationsAdministeredText: Union[str, None] = Field(None)
    MedicationsText: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    ObjectiveText: Union[str, None] = Field(None)
    PhysicalExamText: Union[str, None] = Field(None)
    PlanOfCare: generic.PlanOfCare = Field(None)
    PlanOfCareText: Union[str, None] = Field(None)
    Problems: List[generic.Problem] = Field(None)
    ProblemsText: Union[str, None] = Field(None)
    Procedures: generic.Procedures = Field(None)
    ProceduresText: Union[str, None] = Field(None)
    ReasonForReferralText: Union[str, None] = Field(None)
    ReasonForVisit: List[generic.ReasonForVisit] = Field(None)
    ReasonForVisitText: Union[str, None] = Field(None)
    ResolvedProblems: List[generic.ResolvedProblem] = Field(None)
    ResolvedProblemsText: Union[str, None] = Field(None)
    Results: List[generic.Result] = Field(None)
    ResultText: Union[str, None] = Field(None)
    ReviewOfSystemsText: Union[str, None] = Field(None)
    SocialHistory: generic.SocialHistory = Field(None)
    SocialHistoryText: Union[str, None] = Field(None)
    SubjectiveText: Union[str, None] = Field(None)
    VitalSigns: List[generic.VitalSign] = Field(None)
    VitalSignsText: Union[str, None] = Field(None)