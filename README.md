# CCS API Samples

[![Symantec](https://img.shields.io/badge/tag-symantec-yellow.svg)](https://www.symantec.com/)
[![CCS](https://img.shields.io/badge/tag-ccs-yellow.svg)](https://www.symantec.com/products/control-compliance-suite)
[![Python](https://img.shields.io/badge/language-python-blue.svg)](https://www.python.org/)
|
[![GitHub contributors](https://img.shields.io/github/contributors/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/graphs/contributors/)
|
[![GitHub issues](https://img.shields.io/github/issues/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/pull/)

**Symantec Control Compliance Suite**

[Symantec Control Compliance Suite](https://www.symantec.com/products/control-compliance-suite) (CCS) REST API Samples

-----------------------------------------------------------------------------------------------------------------------

- [CCS API Samples](#CCS-API-Samples)
  - [Setup](#setup)
  - [CHANGELOG](CHANGELOG.md)
  - [License](LICENSE)

**Scripts**

  - [Create Assets](#Create-Assets)
  - [Create Job](#Create-Job)
  - [Create Tokens](#Create-Tokens)
  - [Delete Assets](#Delete-Assets)
  - [Delete Job](#Delete-Job)
  - [Delete Standards](#Delete-Standards)
  - [Get All Assets By Asset Group ID](#Get-All-Assets-By-Asset-Group-ID)
  - [Get Asset Details By ID](#Get-Asset-Details-By-ID)
  - [GetAssetGroupDetailsByID](#Get-Asset-Group-Details-By-ID)
  - [Get Evaluation Raw Results](#Get-Evaluation-Raw-Results)
  - [Get Evaluation Report](#Get-Evaluation-Report)
  - [Get Latest N Job Runs](#Get-Latest-N-Job-Runs)
  - [Get Remediation Ticket Details By ID](#Get-Remediation-Ticket-Details-By-ID)
  - [Perform Job Operation](#Perform-Job-Operation)
  - [Search Assets](#Search-Assets)
  - [Search Assets Group](#Search-Assets-Group)
  - [Search Job By ID](#Search-Job-By-ID)
  - [Search Job By Name](#Search-Job-By-Name)
  - [Search Remediation Tickets](#Search-Remediation-Tickets)
  - [Search Standards](#Search-Standards)
  - [Update Job](#Update-Job)
  - [Update Remediation Ticket](#Update-Remediation-Ticket)

-----------------------------------------------------------------------------------------------------------------------

## Setup

Refer to Symantec CCS API documentation at: https://apidocs.symantec.com/home/CCS

-----------------------------------------------------------------------------------------------------------------------

**Code Files**

-----------------------------------------------------------------------------------------------------------------------

## Create Assets

[CreateAssets.py](CreateAssets.py)

Use this API to create an asset or multiple assets in the Control Compliance Suite asset system. This API can be used only to create assets for agentless data collection method of Control Compliance Suite.

Update some variables in the top of the script first.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_create_asset_for_agentless_data_collection_only

Usage:
> `python CreateAssets.py`

Sample:
> `python CreateAssets.py`

-----------------------------------------------------------------------------------------------------------------------

## Create Job

[CreateJob.py](CreateJob.py)

Use this API to create a job in which a technical standard is used for data collection and evaluation.

Update some variables in the top of the script first.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_create_job_for_data_collection_and_evaluation

Usage:
> `python CreateJob.py`

Sample:
> `python CreateJob.py`

-----------------------------------------------------------------------------------------------------------------------

## Create Tokens

[CreateTokens.py](CreateTokens.py)

Create a Token for use in subsequent API calls.

Update some variables in the top of the script first.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_using_token_based_authentication_for_control_compliance_suite_restful_apis

Usage:
> `python CreateTokens.py`

Sample:
> `python CreateTokens.py #`

-----------------------------------------------------------------------------------------------------------------------

## Delete Assets

[DeleteAssets.py](DeleteAssets.py)

Use this API to delete an asset or a list of assets from the Control Compliance Suite asset system.

Update some variables in the top of the script first.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_delete_asset

Usage:
> `python DeleteAssets.py`

Sample:
> `python DeleteAssets.py`

-----------------------------------------------------------------------------------------------------------------------

## Delete Job

[DeleteJob.py](DeleteJob.py)

Use this API to delete a specified job and the associated job data from the SQL store or from the Control Compliance Suite directory.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_delete_job

Usage:
> `python DeleteJob.py`

Sample:
> `python DeleteJob.py`

-----------------------------------------------------------------------------------------------------------------------

## Delete Standards

[DeleteStandards.py](DeleteStandards.py)

Use this API to delete a specified standard or a list of standards from the Control Compliance Suite system. You can delete up to 10 standards per request.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_delete_standards

Usage:
> `python DeleteStandards.py`

Sample:
> `python DeleteStandards.py`

-----------------------------------------------------------------------------------------------------------------------

## Get All Assets By Asset Group ID

[GetAllAssetsByAssetGroupID.py](GetAllAssetsByAssetGroupID.py)

Use this API to retrieve the details of all the assets that belong to a specific asset group in the Control Compliance Suite 12.5 asset system. Provide asset group GUID in input request to retrieve the asset details.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_get_all_assets_by_asset_group_id

Usage:
> `python GetAllAssetsByAssetGroupID.py`

Sample:
> `python GetAllAssetsByAssetGroupID.py`

-----------------------------------------------------------------------------------------------------------------------

## Get Asset Details By ID

[GetAssetDetailsByID.py](GetAssetDetailsByID.py)

Use this API to retrieve the details of an asset in the Control Compliance Suite 12.5 asset system. Provide asset GUID in input request to retrieve the asset details.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_get_asset_details_by_id

Usage:
> `python GetAssetDetailsByID.py`

Sample:
> `python GetAssetDetailsByID.py`

-----------------------------------------------------------------------------------------------------------------------

## Get Asset Group Details By ID

[GetAssetGroupDetailsByID.py](GetAssetGroupDetailsByID.py)

Use this API to retrieve the details of an asset group in the Control Compliance Suite 12.5 asset system. Provide asset group GUID in input request to retrieve the asset group details.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_get_asset_group_details_by_asset_group_id

Usage:
> `python GetAssetGroupDetailsByID.py`

Sample:
> `python GetAssetGroupDetailsByID.py`

-----------------------------------------------------------------------------------------------------------------------

## Get Evaluation Raw Results

[GetEvaluationRawResults.py](GetEvaluationRawResults.py)

Use this API to get evaluation results in raw JSON format for a specified standard and a specified asset in Control Compliance Suite 12.5.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_api_for_evaluation_results_service

Usage:
> `python GetEvaluationRawResults.py`

Sample:
> `python GetEvaluationRawResults.py`

-----------------------------------------------------------------------------------------------------------------------

## Get Evaluation Report

[GetEvaluationReport.py](GetEvaluationReport.py)

Use this API to download a report that is generated for the evaluation of a specified standard against a specified asset in Control Compliance Suite 12.5.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_get_evaluation_reports

Usage:
> `python GetEvaluationReport.py`

Sample:
> `python GetEvaluationReport.py`

-----------------------------------------------------------------------------------------------------------------------

## Get Latest N Job Runs

[GetLatestNJobRuns.py](GetLatestNJobRuns.py)

Use this API to retrieve the list of latest runs for a specified job in Control Compliance Suite 12.5.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_get_latest_job_runs

Usage:
> `python GetLatestNJobRuns.py`

Sample:
> `python GetLatestNJobRuns.py`

-----------------------------------------------------------------------------------------------------------------------

## Get Remediation Ticket Details By ID

[GetRemediationTicketDetailsByID.py](GetRemediationTicketDetailsByID.py)

Use this API to retrieve the details of a Control Compliance Suite remediation ticket. To retrieve ticket details, provide the display number of the ticket in input request.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_get_remediation_ticket_details_by_ticket_number

Usage:
> `python GetRemediationTicketDetailsByID.py`

Sample:
> `python GetRemediationTicketDetailsByID.py`

-----------------------------------------------------------------------------------------------------------------------

## Perform Job Operation

[PerformJobOperation.py](PerformJobOperation.py)

Use this API to perform any of the following job operations:
- Executing a job immediately
- Stopping a running job

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_job_operation

Usage:
> `python PerformJobOperation.py`

Sample:
> `python PerformJobOperation.py`

-----------------------------------------------------------------------------------------------------------------------

## Search Assets

[SearchAssets.py](SearchAssets.py)

Use this API to retrieve the list of assets in the Control Compliance Suite 12.5 asset system.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_search_assets

Usage:
> `python SearchAssets.py`

Sample:
> `python SearchAssets.py`

-----------------------------------------------------------------------------------------------------------------------

## Search Assets Group

[SearchAssetsGroup.py](SearchAssetsGroup.py)

Use this API to retrieve the list of asset groups in the Control Compliance Suite 12.5 asset system.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_search_asset_group

Usage:
> `python SearchAssetsGroup.py`

Sample:
> `python SearchAssetsGroup.py`

-----------------------------------------------------------------------------------------------------------------------

## Search Job By ID

[SearchJobByID.py](SearchJobByID.py)

Use this API to search a job in Control Compliance Suite by providing the JobID in the request. Successful completion of the request returns job properties and configuration details of the following types of jobs:

- Collection-Evaluation-Reporting (CER) Job
- Data Collection Job
- Evaluation Job

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_search_job_by_id

Usage:
> `python SearchJobByID.py`

Sample:
> `python SearchJobByID.py`

-----------------------------------------------------------------------------------------------------------------------

## Search Job By Name

[SearchJobByName.py](SearchJobByName.py)

Use this API to search a job in Control Compliance Suite by providing the exact job name in the request. Successful completion of the request returns job properties and configuration details of the following types of jobs:

- Collection-Evaluation-Reporting (CER) Job
- Data Collection Job
- Evaluation Job

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_search_job_by_name

Usage:
> `python SearchJobByName.py`

Sample:
> `python SearchJobByName.py`

-----------------------------------------------------------------------------------------------------------------------

## Search Remediation Tickets

[SearchRemediationTickets.py](SearchRemediationTickets.py)

Use this API to retrieve the list of remediation tickets in Control Compliance Suite (CCS) 12.5.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_search_remediation_tickets

Usage:
> `python SearchRemediationTickets.py`

Sample:
> `python SearchRemediationTickets.py`

-----------------------------------------------------------------------------------------------------------------------

## Search Standards

[SearchStandards.py](SearchStandards.py)

Use this API to retrieve the list of standards in the Control Compliance Suite 12.5 Standards Manager.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_search_standards

Usage:
> `python SearchStandards.py`

Sample:
> `python SearchStandards.py`

-----------------------------------------------------------------------------------------------------------------------

## Update Job

[UpdateJob.py](UpdateJob.py)

Use this API to update a job in which a technical standard is used for data collection and evaluation. (See About Jobs)

You can update the following jobs with this API:
- Collection-Evaluation Job
- Data Collection Job
- Evaluation Job

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_update_job_for_data_collection_and_evaluation

Usage:
> `python UpdateJob.py`

Sample:
> `python UpdateJob.py`

-----------------------------------------------------------------------------------------------------------------------

## Update Remediation Ticket

[UpdateRemediationTicket.py](UpdateRemediationTicket.py)

Use this API to update Control Compliance Suite remediation ticket details.

You can update any of or all the following details in an input request for a single ticket at a time:
- Ticket state (from 1 to 5)
- Description
- Ticket priority
- Details of user to whom the ticket is assigned for remediation

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_update_remediation_ticket_details

Usage:
> `python UpdateRemediationTicket.py`

Sample:
> `python UpdateRemediationTicket.py`

-----------------------------------------------------------------------------------------------------------------------

## Change Log

See [CHANGELOG](CHANGELOG.md).

-----------------------------------------------------------------------------------------------------------------------

## License

See [License](LICENSE).
