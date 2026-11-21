[![awesome-lead-generation](image/awesome-adops-automation.png)](https://github.com/adops-tool/awesome-adops-automation/pulls)

[![animated-line](https://github.com/readme-SVG/animated-line/blob/main/STORAGE/line-svg-3D444D.svg)](https://github.com/readme-SVG/animated-line) <!-- -SVG-Line- -->

**A curated list of code, SDKs, and pipelines that replace manual trafficking, QA, and reporting work with scripts.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

</div>

## Table of Contents

- [Ad Server APIs & Official SDKs](#ad-server-apis--official-sdks)
- [Campaign & Trafficking Automation](#campaign--trafficking-automation)
- [Ad Tag QA & Automated Testing](#ad-tag-qa--automated-testing)
- [Data Pipelines & ETL for Ad Data](#data-pipelines--etl-for-ad-data)
- [Reporting, SQL & BI Templates](#reporting-sql--bi-templates)
- [Workflow Orchestration & No-Code/Low-Code](#workflow-orchestration--no-codelow-code)
- [Learning Resources & Communities](#learning-resources--communities)
- [Contributing](#contributing)
- [License](#license)

---

## Ad Server APIs & Official SDKs

- [googleads-python-lib](https://github.com/googleads/googleads-python-lib) - Official Python client for the Google Ad Manager and legacy AdWords SOAP APIs.
- [google-ads-python](https://github.com/googleads/google-ads-python) - Official Python client library for the current Google Ads API.
- [googleads-java-lib](https://github.com/googleads/googleads-java-lib) - Official Java client for the Google Ad Manager and Google Ads APIs.
- [googleads-dotnet-lib](https://github.com/googleads/googleads-dotnet-lib) - Official .NET client for the Google Ad Manager and Google Ads APIs.
- [google-ads-php](https://github.com/googleads/google-ads-php) - Official PHP client library for the Google Ads API.
- [google-ads-ruby](https://github.com/googleads/google-ads-ruby) - Official Ruby client library for the Google Ads API.
- [google-ads-api](https://github.com/Opteo/google-ads-api) - Community-maintained Node.js client for the Google Ads API, useful where no official JS SDK exists.
- [adzerk-decision-sdk-js](https://github.com/adzerk/adzerk-decision-sdk-js) - Official JavaScript SDK for Kevel's real-time Decision API.
- [adzerk-decision-sdk-python](https://github.com/adzerk/adzerk-decision-sdk-python) - Official Python SDK for Kevel's Decision API.
- [adzerk-management-sdk-js](https://github.com/adzerk/adzerk-management-sdk-js) - Official JavaScript SDK for Kevel's Management API that automates campaign and flight setup.
- [kevel-decision-sdk-go](https://github.com/adzerk/kevel-decision-sdk-go) - Official Go SDK for Kevel's Decision API.
- [swift-package-manager-amazon-aps](https://github.com/amzn/swift-package-manager-amazon-aps) - Official Amazon Publisher Services (APS) bidding SDK distribution for iOS apps via Swift Package Manager.

---

## Campaign & Trafficking Automation

- [facebook-python-business-sdk](https://github.com/meta/facebook-python-business-sdk) - Official Python SDK for the Meta Marketing API that scripts campaign, ad set, and ad creation.
- [facebook-nodejs-business-sdk](https://github.com/meta/facebook-nodejs-business-sdk) - Official Node.js SDK for the Meta Marketing API.
- [facebook-java-business-sdk](https://github.com/meta/facebook-java-business-sdk) - Official Java SDK for the Meta Marketing API.
- [bulkdozer](https://github.com/google/bulkdozer) - Google's open-source tool for bulk trafficking and QA of Campaign Manager 360 entities from Google Sheets.
- [google-ads-scripts topic](https://github.com/topics/google-ads-scripts) - Curated GitHub topic collecting Google Ads Scripts for bid, budget, and account automation.
- [GoogleAdsScriptsStarter](https://github.com/JJPell/GoogleAdsScriptsStarter) - TypeScript starter project that compiles modern JS into Google Ads Scripts' ES3 runtime.
- [Prebid.js](https://github.com/prebid/Prebid.js) - Open-source header bidding library that automates setting up and managing programmatic demand partners.
- [prebid-server](https://github.com/prebid/prebid-server) - Server-side header bidding implementation that moves auction logic out of the browser.

---

## Ad Tag QA & Automated Testing

- [playwright](https://github.com/microsoft/playwright) - Cross-browser automation framework commonly used to script ad tag rendering, viewability, and click-through QA.
- [puppeteer](https://github.com/puppeteer/puppeteer) - Headless Chrome Node.js API used to automate ad tag loading tests and screenshot diffing.
- [VAST_Samples](https://github.com/InteractiveAdvertisingBureau/VAST_Samples) - IAB's official sample VAST tags for testing video ad server and player integrations.
- [VAST-Tester](https://github.com/IABTechLab/VAST-Tester) - IAB Tech Lab's tool for validating VAST tag responses against the spec.
- [videojs-ima](https://github.com/googleads/videojs-ima) - Google's IMA SDK plugin for Video.js, useful for building test players that exercise VAST/VPAID creatives.
- [googleads-ima-html5](https://github.com/googleads/googleads-ima-html5) - Official samples for the HTML5 IMA SDK, handy as a QA harness for video ad tags.
- [mitmproxy](https://github.com/mitmproxy/mitmproxy) - Scriptable HTTPS proxy used to capture and analyze ad request/response traffic and HAR-style data for tag debugging.
- [devtools-protocol](https://github.com/ChromeDevTools/devtools-protocol) - Chrome DevTools Protocol reference used to build custom network/HAR analyzers for ad tag QA.

---

## Data Pipelines & ETL for Ad Data

- [airbyte](https://github.com/airbytehq/airbyte) - Open-source ELT platform with pre-built connectors for Google Ads, Meta Marketing, and Ad Manager report exports.
- [dlt](https://github.com/dlt-hub/dlt) - Python ETL library whose verified sources include Google Ads and Facebook Ads extractors for loading into warehouses.
- [tap-googleads (Matatika)](https://github.com/Matatika/tap-googleads) - Meltano/Singer tap that extracts Google Ads reporting data for ELT pipelines.
- [dbt_google_ads](https://github.com/fivetran/dbt_google_ads) - dbt package that models and transforms Google Ads data loaded into a warehouse.
- [dbt_facebook_ads](https://github.com/fivetran/dbt_facebook_ads) - dbt package that transforms raw Meta Ads data into reporting-ready tables.
- [dbt_amazon_ads](https://github.com/fivetran/dbt_amazon_ads) - dbt package that models Amazon Ads data for unified ad spend reporting.
- [dbt_ad_reporting](https://github.com/fivetran/dbt_ad_reporting) - dbt package that unions multiple ad platform packages into a single blended ad reporting mart.
- [dbt-bigquery](https://github.com/dbt-labs/dbt-bigquery) - Official dbt adapter for running SQL transformations against BigQuery, the usual home for ad data warehouses.

---

## Reporting, SQL & BI Templates

- [ads-api-report-fetcher](https://github.com/google/ads-api-report-fetcher) - Google's "gaarf" tool that runs GAQL queries against Google Ads/Ad Manager and writes results straight to BigQuery, Sheets, or CSV.
- [community-connectors](https://github.com/googledatastudio/community-connectors) - Official Google repository of open-source Looker Studio (Data Studio) community connectors.
- [bigquery-utils](https://github.com/GoogleCloudPlatform/bigquery-utils) - Google Cloud's collection of reusable SQL scripts, UDFs, and views for BigQuery data warehouse operations.
- [Load Google Ad Manager data into BigQuery](https://cloud.google.com/bigquery/docs/doubleclick-publisher-transfer) - Google's official guide and sample SQL for analyzing Ad Manager log-level data transferred into BigQuery.
- [grafana](https://github.com/grafana/grafana) - Open-source dashboarding platform commonly used to build real-time pacing and spend dashboards on top of ad data warehouses.

---

## Workflow Orchestration & No-Code/Low-Code

- [n8n](https://github.com/n8n-io/n8n) - Open-source, self-hostable workflow automation tool with HTTP/webhook nodes used to stitch together ad platform APIs without heavy code.
- [airflow](https://github.com/apache/airflow) - Workflow orchestration platform used to schedule recurring ad data extraction, QA, and reporting DAGs.
- [apache-airflow-client-python](https://github.com/apache/airflow-client-python) - Official Python client for the Airflow REST API, useful for triggering AdOps DAGs from external scripts.
- [apps-script-samples](https://github.com/googleworkspace/apps-script-samples) - Google's official Apps Script samples, a frequent base for Sheets-driven trafficking and QA automations.

---

## Learning Resources & Communities

- [r/adops](https://www.reddit.com/r/adops/) - Reddit community where ad ops and programmatic practitioners discuss tooling, workflows, and automation.
- [AdMonsters](https://www.admonsters.com/) - Long-running publisher ad ops trade press covering ad tech operations and automation trends.
- [AdExchanger](https://www.adexchanger.com/) - Daily news and analysis on programmatic, ad tech, and the platforms AdOps teams automate against.
- [Google Ads Developer Blog](https://ads-developers.googleblog.com/) - Google's official blog for Ads/Ad Manager API releases, deprecations, and automation guidance.

---

## Contributing

Contributions are welcome. Before opening a pull request:

1. Confirm the resource is a real, verifiable GitHub repository, official SDK, or documented tool — no invented links.
2. Use the required list format: `- [Resource Name](https://url) - Concise 1-sentence description of what it automates.`
3. Add the entry to the most relevant section, keeping alphabetical or logical grouping within that section.
4. Keep descriptions factual and focused on the automation value, not marketing language.

## License

Released under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, the author(s) have waived all copyright and related rights to this work.

[![CC0](https://img.shields.io/badge/CC0-1.0-lightgrey?style=flat-square)](LICENSE)
