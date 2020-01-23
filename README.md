# [WIP] Citrix Analysis Notebook

A jupyter notebook to aid in automating some of the analysis related to compromised Citrix hosts.

# Features

- Automatic decompression of logs
- Parsing of logs into pandas dataframes for further analysis if desired
- Searching of common IOCs associated with compromise
- Automatic parsing and decoding of XML payload files if available
- Output of analysis to excel results sheet for review

# Changelog

## v 0.4
* added bash log parsing
* added 'haveTemplateDir' bool to config to allow running of the notebook even if not in possession of the /Templates dir from the netscaler host

## v 0.5
* added parsing for the majority of notice logs (see errors for exceptions)
    * exceptions are currently: sslvpn_aaad_login_handler and Session setup data send logs although they print via errors so you can still inspect them

## v 0.6
* added sh log parsing
* added common 'searchFor' var to config to hold search terms for suspicious activity that will be searched for in every log

## v 0.7
* added payload decoding (chr() and base64) + aggregation of all payloads into 'decodedpayloads' column

## v 0.8
* added 'latin1' encoding to all log parsing to account for instances where logs where not in utf-8 and caused parsing errors
* split searchFor into searchFor and shSearchFor as sh logs have different criteria to search that doesn't show up in other logs (helps efficiency)
