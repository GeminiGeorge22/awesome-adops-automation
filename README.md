<div align="center">

[![awesome-adops-automation](image/awesome-adops-automation.png)](https://github.com/adops-tool/awesome-adops-automation/pulls)

[![animated-line](https://github.com/readme-SVG/animated-line/blob/main/STORAGE/line-svg-3D444D.svg)](https://github.com/readme-SVG/animated-line) <!-- -SVG-Line- -->

**A curated list of code, SDKs, and pipelines that replace manual trafficking, QA, and reporting work with scripts.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

</div>

> Each entry is marked with the kind of resource it is: ![github](image/alg_R.png) open-source repository, ![web](image/alg_I.png) documentation, specification, or hosted tool. Dormant and archived projects are kept when they still explain an architecture — they are labeled as such.

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

*Official and community client libraries, plus references, for the ad servers and delivery platforms AdOps teams automate against.*

### Official SDKs

![github](image/alg_R.png) [googleads-python-lib](https://github.com/googleads/googleads-python-lib) - Official Python client for the Google Ad Manager and legacy AdWords SOAP APIs.

![github](image/alg_R.png) [google-ads-python](https://github.com/googleads/google-ads-python) - Official Python client library for the current Google Ads API.

![github](image/alg_R.png) [googleads-java-lib](https://github.com/googleads/googleads-java-lib) - Official Java client for the Google Ad Manager and Google Ads APIs.

![github](image/alg_R.png) [googleads-dotnet-lib](https://github.com/googleads/googleads-dotnet-lib) - Official .NET client for the Google Ad Manager and Google Ads APIs.

![github](image/alg_R.png) [google-ads-php](https://github.com/googleads/google-ads-php) - Official PHP client library for the Google Ads API.

![github](image/alg_R.png) [google-ads-ruby](https://github.com/googleads/google-ads-ruby) - Official Ruby client library for the Google Ads API.

![github](image/alg_R.png) [google-ads-api](https://github.com/Opteo/google-ads-api) - Community-maintained Node.js client for the Google Ads API, useful where no official JS SDK exists.

![github](image/alg_R.png) [adzerk-decision-sdk-js](https://github.com/adzerk/adzerk-decision-sdk-js) - Official JavaScript SDK for Kevel's real-time Decision API.

![github](image/alg_R.png) [adzerk-decision-sdk-python](https://github.com/adzerk/adzerk-decision-sdk-python) - Official Python SDK for Kevel's Decision API.

![github](image/alg_R.png) [adzerk-management-sdk-js](https://github.com/adzerk/adzerk-management-sdk-js) - Official JavaScript SDK for Kevel's Management API that automates campaign and flight setup.

![github](image/alg_R.png) [adzerk-management-sdk-ruby](https://github.com/adzerk/adzerk-management-sdk-ruby) - Official Ruby SDK for the Kevel Management API.

![github](image/alg_R.png) [swift-package-manager-amazon-aps](https://github.com/amzn/swift-package-manager-amazon-aps) - Official Amazon Publisher Services (APS) bidding SDK distribution for iOS apps via Swift Package Manager.

### Official API references

![web](image/alg_I.png) [Google Ad Manager API](https://support.google.com/admanager/answer/3088588?hl=en) - Ad Manager API for managing inventory, orders and reporting data programmatically.

![web](image/alg_I.png) [Google Ads API documentation](https://developers.google.com/google-ads/api/docs/get-started/introduction) - Programmatic interface for managing Google Ads accounts, campaigns, ads and Smart Bidding strategies.

![web](image/alg_I.png) [Meta Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview) - API for creating, managing and analyzing ads across Meta technologies.

---

## Campaign & Trafficking Automation

*Tools that script campaign creation, bulk trafficking and Google Ads / Ad Manager operations.*

### SDKs & scripts

![github](image/alg_R.png) [facebook-python-business-sdk](https://github.com/meta/facebook-python-business-sdk) - Official Python SDK for the Meta Marketing API that scripts campaign, ad set, and ad creation.

![github](image/alg_R.png) [facebook-nodejs-business-sdk](https://github.com/meta/facebook-nodejs-business-sdk) - Official Node.js SDK for the Meta Marketing API.

![github](image/alg_R.png) [facebook-java-business-sdk](https://github.com/meta/facebook-java-business-sdk) - Official Java SDK for the Meta Marketing API.

![github](image/alg_R.png) [free-google-ads-scripts](https://github.com/charlesbannister/free-google-ads-scripts) - Public repository of free Google Ads scripts from Shabba.io / Automating AdWords.com.

![github](image/alg_R.png) [OrbiAds GAM MCP](https://github.com/OrbiAds/Orbiads-GAM-MCP) - Hosted Google Ad Manager MCP server and CLI for inventory, trafficking and reporting with OAuth and confirm-before-write guardrails.

![github](image/alg_R.png) [Prebid.js](https://github.com/prebid/Prebid.js) - Open-source header bidding library that automates setting up and managing programmatic demand partners.

![github](image/alg_R.png) [prebid-server](https://github.com/prebid/prebid-server) - Server-side header bidding implementation that moves auction logic out of the browser.

### Web references

![web](image/alg_I.png) [Google Ads Scripts documentation](https://developers.google.com/google-ads/scripts/docs/getting-started) - Documentation for Google Ads Scripts, JavaScript automation that runs inside the Google Ads interface.

---

## Ad Tag QA & Automated Testing

*Frameworks, validators and proxies that automate ad tag rendering, VAST validity and traffic analysis.*

### Automation frameworks

![github](image/alg_R.png) [playwright](https://github.com/microsoft/playwright) - Cross-browser automation framework commonly used to script ad tag rendering, viewability, and click-through QA.

![github](image/alg_R.png) [puppeteer](https://github.com/puppeteer/puppeteer) - Headless Chrome Node.js API used to automate ad tag loading tests and screenshot diffing.

![github](image/alg_R.png) [mitmproxy](https://github.com/mitmproxy/mitmproxy) - Scriptable HTTPS proxy used to capture and analyze ad request/response traffic and HAR-style data for tag debugging.

![github](image/alg_R.png) [devtools-protocol](https://github.com/ChromeDevTools/devtools-protocol) - Chrome DevTools Protocol reference used to build custom network/HAR analyzers for ad tag QA.

### VAST / video tag QA

![github](image/alg_R.png) [VAST_Samples](https://github.com/InteractiveAdvertisingBureau/VAST_Samples) - IAB's official sample VAST tags for testing video ad server and player integrations.

![github](image/alg_R.png) [VAST-Tester](https://github.com/IABTechLab/VAST-Tester) - IAB Tech Lab's tool for validating VAST tag responses against the spec.

![github](image/alg_R.png) [vast-tag-xml-examples](https://github.com/admein-advertising/vast-tag-xml-examples) - Collection of VAST 2.0 / 3.0 / 4.x XML examples for testing video ad tags.

![github](image/alg_R.png) [videojs-ima](https://github.com/googleads/videojs-ima) - Google's IMA SDK plugin for Video.js, useful for building test players that exercise VAST/VPAID creatives.

![github](image/alg_R.png) [googleads-ima-html5](https://github.com/googleads/googleads-ima-html5) - Official samples for the HTML5 IMA SDK, handy as a QA harness for video ad tags.

### Supply-chain validation

![github](image/alg_R.png) [python-sellers-json-validator](https://github.com/adops-tool/python-sellers-json-validator) - Async Python engine that probes, validates and audits IAB Tech Lab sellers.json endpoints across enterprise domain inventories.

![web](image/alg_I.png) [IAB Tech Lab](https://iabtechlab.com/) - Standards and specifications from the IAB Tech Lab for VAST, OpenRTB and programmatic reporting.

![web](image/alg_I.png) [VAST 4.3 specification](https://iabtechlab.com/wp-content/uploads/2022/09/VAST_4.3.pdf) - IAB Tech Lab's Video Ad Serving Template (VAST) 4.3 specification.

---

## Data Pipelines & ETL for Ad Data

*Extraction, transformation and modeling of ad data into warehouses and BI tools.*

### Extractors

![github](image/alg_R.png) [airbyte](https://github.com/airbytehq/airbyte) - Open-source ELT platform with pre-built connectors for Google Ads, Meta Marketing, and Ad Manager report exports.

![github](image/alg_R.png) [dlt](https://github.com/dlt-hub/dlt) - Python ETL library whose verified sources include Google Ads and Facebook Ads extractors for loading into warehouses.

![github](image/alg_R.png) [tap-googleads (Matatika)](https://github.com/Matatika/tap-googleads) - Meltano/Singer tap that extracts Google Ads reporting data for ELT pipelines.

### Transformations & models

![github](image/alg_R.png) [dbt_google_ads](https://github.com/fivetran/dbt_google_ads) - dbt package that models and transforms Google Ads data loaded into a warehouse.

![github](image/alg_R.png) [dbt_facebook_ads](https://github.com/fivetran/dbt_facebook_ads) - dbt package that transforms raw Meta Ads data into reporting-ready tables.

![github](image/alg_R.png) [dbt_amazon_ads](https://github.com/fivetran/dbt_amazon_ads) - dbt package that models Amazon Ads data for unified ad spend reporting.

![github](image/alg_R.png) [dbt_ad_reporting](https://github.com/fivetran/dbt_ad_reporting) - dbt package that unions multiple ad platform packages into a single blended ad reporting mart.

![github](image/alg_R.png) [dbt-bigquery](https://github.com/dbt-labs/dbt-adapters/tree/main/dbt-bigquery) - dbt package that models ad spend data in BigQuery; the official adapter lives in the dbt-adapters monorepo.

---

## Reporting, SQL & BI Templates

*SQL, dashboards and connectors for reporting across ad platforms.*

### Report fetchers & SQL (GitHub)

![github](image/alg_R.png) [ads-api-report-fetcher](https://github.com/google/ads-api-report-fetcher) - Google's "gaarf" tool that runs GAQL queries against Google Ads/Ad Manager and writes results straight to BigQuery, Sheets, or CSV.

![github](image/alg_R.png) [bigquery-utils](https://github.com/GoogleCloudPlatform/bigquery-utils) - Google Cloud's collection of reusable SQL scripts, UDFs, and views for BigQuery data warehouse operations.

### Dashboards

![github](image/alg_R.png) [grafana](https://github.com/grafana/grafana) - Open-source dashboarding platform commonly used to build real-time pacing and spend dashboards on top of ad data warehouses.

### Web references

![web](image/alg_I.png) [Load Google Ad Manager data into BigQuery](https://cloud.google.com/bigquery/docs/doubleclick-publisher-transfer) - Google's official guide and sample SQL for analyzing Ad Manager log-level data transferred into BigQuery.

---

## Workflow Orchestration & No-Code/Low-Code

*Schedulers, runners and low-code tools that chain ad platform actions.*

### Orchestration

![github](image/alg_R.png) [airflow](https://github.com/apache/airflow) - Workflow orchestration platform used to schedule recurring ad data extraction, QA, and reporting DAGs.

![github](image/alg_R.png) [apache-airflow-client-python](https://github.com/apache/airflow-client-python) - Official Python client for the Airflow REST API, useful for triggering AdOps DAGs from external scripts.

![github](image/alg_R.png) [n8n](https://github.com/n8n-io/n8n) - Open-source, self-hostable workflow automation tool with HTTP/webhook nodes used to stitch together ad platform APIs without heavy code.

### No-code/Low-code

![github](image/alg_R.png) [apps-script-samples](https://github.com/googleworkspace/apps-script-samples) - Google's official Apps Script samples, a frequent base for Sheets-driven trafficking and QA automations.

---

## Learning Resources & Communities

*Blogs, communities, trade press and official developer references for adtech practitioners.*

![web](image/alg_I.png) [r/adops](https://www.reddit.com/r/adops/) - Reddit community where ad ops and programmatic practitioners discuss tooling, workflows, and automation.

![web](image/alg_I.png) [AdMonsters](https://www.admonsters.com/) - Long-running publisher ad ops trade press covering ad tech operations and automation trends.

![web](image/alg_I.png) [AdExchanger](https://www.adexchanger.com/) - Daily news and analysis on programmatic, ad tech, and the platforms AdOps teams automate against.

![web](image/alg_I.png) [Google Ads Developer Blog](https://ads-developers.googleblog.com/) - Google's official blog for Ads/Ad Manager API releases, deprecations, and automation guidance.

---

## Contributing

Contributions are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md), which has the full guide. Before opening a pull request:

1. Confirm the resource is a real, verifiable GitHub repository, official SDK, or documented tool — no invented links.
2. Use the required list format: `![github](image/alg_R.png) [Resource Name](url) - Concise 1-sentence description of what it automates.` (or the `web` icon for websites).
3. Add the entry to the most relevant section, keeping alphabetical or logical grouping within that section.
4. Keep descriptions factual and focused on the automation value, not marketing language.
5. Run the local checker: `python3 scripts/check_readme.py`.

## License

Released under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, the author(s) have waived all copyright and related rights to this work.

[![CC0](https://img.shields.io/badge/CC0-1.0-lightgrey?style=flat-square)](LICENSE)
