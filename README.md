# [WIP] Citrix Analysis Notebook

A jupyter notebook to aid in automating some of the forensic analysis related to Citrix Netscaler hosts compromised via CVE-2019-19781. Not a be-all end-all solution, just there to help you get started.

All notes/suggestions are welcome. Feel free to submit pull requests or issues.

# Features

- Currently handles the following logs and payload XMLs if available:
  - HTTPAccess
  - Cron
  - Bash
  - Notice
  - Sh
- Decompression of logs
- Parsing of logs into pandas dataframes for further analysis if desired
- Searching of logs for common IOCs associated with compromise
- Parsing and decoding of XML payload files if available
- Output of analysis to excel results sheet for review

# Changelog

## v 0.8
* added 'latin1' encoding to all log parsing to account for instances where logs were not in utf-8 and caused parsing errors
* split searchFor into searchFor and shSearchFor as sh logs have different criteria to search that doesn't show up in other logs

## v 0.7
* added payload decoding (chr() and base64) + aggregation of all payloads into 'decodedpayloads' column

## v 0.6
* added sh log parsing
* added common 'searchFor' var to config to hold search terms for suspicious activity that will be searched for in every log

## v 0.5
* added parsing for the majority of notice logs (see errors for exceptions)
    * exceptions are currently: sslvpn_aaad_login_handler and Session setup data send logs although they print via errors so you can still inspect them

## v 0.4
* added bash log parsing
