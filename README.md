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

Symantec Control Compliance Suite (CCS) REST API Samples

-----------------------------------------------------------------------------------------------------------------------

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

Use this API to create an asset (What is an asset?) or multiple assets in the Control Compliance Suite asset system. This API can be used only to create assets for agentless data collection method of Control Compliance Suite.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_create_asset_for_agentless_data_collection_only

Usage: 
> `python CreateAssets.py -param ??`

Sample:
>  `python CreateAssets.py #`

-----------------------------------------------------------------------------------------------------------------------

## Create Job
[CreateJob.py](CreateJob.py)

*Desc*

Usage: 
> `python CreateJob.py -param ??`

Sample:
>  `python CreateJob.py #`

-----------------------------------------------------------------------------------------------------------------------

## Create Tokens
[CreateTokens.py](CreateTokens.py)

*Desc*

Usage: 
> `python CreateTokens.py -param ??`

Sample:
>  `python CreateTokens.py #`

-----------------------------------------------------------------------------------------------------------------------

## Delete Assets
[DeleteAssets.py](DeleteAssets.py)

*Desc*

Usage: 
> `python DeleteAssets.py -param ??`

Sample:
>  `python DeleteAssets.py #`

-----------------------------------------------------------------------------------------------------------------------

## Delete Job
[DeleteJob.py](DeleteJob.py)

*Desc*

Usage: 
> `python DeleteJob.py -param ??`

Sample:
>  `python DeleteJob.py #`

-----------------------------------------------------------------------------------------------------------------------

## Delete Standards
[DeleteStandards.py](DeleteStandards.py)

*Desc*

Usage: 
> `python DeleteStandards.py -param ??`

Sample:
>  `python DeleteStandards.py #`

-----------------------------------------------------------------------------------------------------------------------

## Get All Assets By Asset Group ID
[GetAllAssetsByAssetGroupID.py](GetAllAssetsByAssetGroupID.py)

*Desc*

Usage: 
> `python GetAllAssetsByAssetGroupID.py -param ??`

Sample:
>  `python GetAllAssetsByAssetGroupID.py #`

-----------------------------------------------------------------------------------------------------------------------

## Get Asset Details By ID
[GetAssetDetailsByID.py](GetAssetDetailsByID.py)

*Desc*

Usage: 
> `python GetAssetDetailsByID.py -param ??`

Sample:
>  `python GetAssetDetailsByID.py #`

-----------------------------------------------------------------------------------------------------------------------

## Get Asset Group Details By ID
[GetAssetGroupDetailsByID.py](GetAssetGroupDetailsByID.py)

*Desc*

Usage: 
> `python GetAssetGroupDetailsByID.py -param ??`

Sample:
>  `python GetAssetGroupDetailsByID.py #`

-----------------------------------------------------------------------------------------------------------------------

## Get Evaluation Raw Results
[GetEvaluationRawResults.py](GetEvaluationRawResults.py)

*Desc*

Usage: 
> `python GetEvaluationRawResults.py -param ??`

Sample:
>  `python GetEvaluationRawResults.py #`

-----------------------------------------------------------------------------------------------------------------------

## Get Evaluation Report
[GetEvaluationReport.py](GetEvaluationReport.py)

*Desc*

Usage: 
> `python GetEvaluationReport.py -param ??`

Sample:
>  `python GetEvaluationReport.py #`

-----------------------------------------------------------------------------------------------------------------------

## Get Latest N Job Runs
[GetLatestNJobRuns.py](GetLatestNJobRuns.py)

*Desc*

Usage: 
> `python GetLatestNJobRuns.py -param ??`

Sample:
>  `python GetLatestNJobRuns.py #`

-----------------------------------------------------------------------------------------------------------------------

## Get Remediation Ticket Details By ID
[GetRemediationTicketDetailsByID.py](GetRemediationTicketDetailsByID.py)

*Desc*

Usage: 
> `python GetRemediationTicketDetailsByID.py -param ??`

Sample:
>  `python GetRemediationTicketDetailsByID.py #`

-----------------------------------------------------------------------------------------------------------------------

## Perform Job Operation
[PerformJobOperation.py](PerformJobOperation.py)

*Desc*

Usage: 
> `python PerformJobOperation.py -param ??`

Sample:
>  `python PerformJobOperation.py #`

-----------------------------------------------------------------------------------------------------------------------

## Search Assets
[SearchAssets.py](SearchAssets.py)

*Desc*

Usage: 
> `python SearchAssets.py -param ??`

Sample:
>  `python SearchAssets.py #`

-----------------------------------------------------------------------------------------------------------------------

## Search Assets Group
[SearchAssetsGroup.py](SearchAssetsGroup.py)

*Desc*

Usage: 
> `python SearchAssetsGroup.py -param ??`

Sample:
>  `python SearchAssetsGroup.py #`

-----------------------------------------------------------------------------------------------------------------------

## Search Job By ID
[SearchJobByID.py](SearchJobByID.py)

*Desc*

Usage: 
> `python SearchJobByID.py -param ??`

Sample:
>  `python SearchJobByID.py #`

-----------------------------------------------------------------------------------------------------------------------

## Search Job By Name
[SearchJobByName.py](SearchJobByName.py)

*Desc*

Usage: 
> `python SearchJobByName.py -param ??`

Sample:
>  `python SearchJobByName.py #`

-----------------------------------------------------------------------------------------------------------------------

## Search Job By Name
[SearchJobByName.py](SearchJobByName.py)

*Desc*

Usage: 
> `python SearchJobByName.py -param ??`

Sample:
>  `python SearchJobByName.py #`

-----------------------------------------------------------------------------------------------------------------------

## Search Remediation Tickets
[SearchRemediationTickets.py](SearchRemediationTickets.py)

*Desc*

Usage: 
> `python SearchRemediationTickets.py -param ??`

Sample:
>  `python SearchRemediationTickets.py #`

-----------------------------------------------------------------------------------------------------------------------

## Search Standards
[SearchStandards.py](SearchStandards.py)

*Desc*

Usage: 
> `python SearchStandards.py -param ??`

Sample:
>  `python SearchStandards.py #`

-----------------------------------------------------------------------------------------------------------------------

## Update Job
[UpdateJob.py](UpdateJob.py)

*Desc*

Usage: 
> `python UpdateJob.py -param ??`

Sample:
>  `python UpdateJob.py #`

-----------------------------------------------------------------------------------------------------------------------

## Update Remediation Ticket
[UpdateRemediationTicket.py](UpdateRemediationTicket.py)

*Desc*

Usage: 
> `python UpdateRemediationTicket.py -param ??`

Sample:
>  `python UpdateRemediationTicket.py #`

-----------------------------------------------------------------------------------------------------------------------

## Change Log

See [CHANGELOG](CHANGELOG.md).

-----------------------------------------------------------------------------------------------------------------------

## License

See [License](LICENSE).