# [WIP] Citrix Analysis Notebook

A jupyter notebook to aid in automating some of the forensic analysis related to Citrix Netscaler hosts compromised via CVE-2019-19781. Not a be-all end-all solution, just there to help you get started.

All notes/suggestions are welcome. Feel free to submit pull requests or issues.

# Features

- Currently handles the following logs and payload XMLs if available:
  - HTTPAccess
  - HTTPError
  - Cron
  - Bash
  - Notice
  - Sh
- Decompression of logs
- Parsing of logs into pandas dataframes for further analysis if desired
- Searching of logs for common IOCs associated with compromise
- Parsing and decoding of XML payload files if available
- Output of analysis to excel results sheet for review

# Useful Resources

- [Citrix Final Patches](https://www.citrix.com/blogs/2020/01/24/citrix-releases-final-fixes-for-cve-2019-19781/)
- [FireEye IOC Script](https://www.citrix.com/news/announcements/jan-2020/citrix-and-fireeye-mandiant-launch-indicator-of-compromise-scann.html)
- [x1sec Great CVE-2019-19781 Notes](https://github.com/x1sec/CVE-2019-19781/blob/master/CVE-2019-19781-DFIR.md)
- [Overview of Observed Payloads](https://isc.sans.edu/diary/Citrix+ADC+Exploits%3A+Overview+of+Observed+Payloads/25704)
- [FireEye NOTROBIN Writeup](https://www.fireeye.com/blog/threat-research/2020/01/vigilante-deploying-mitigation-for-citrix-netscaler-vulnerability-while-maintaining-backdoor.html)
- [TrustedSec Forensics Guide](https://www.trustedsec.com/blog/netscaler-remote-code-execution-forensics/)
- [TrustedSec Honeypot Writeup](https://www.trustedsec.com/blog/netscaler-honeypot/)
- [US-Cert Writeup](https://www.us-cert.gov/ncas/alerts/aa20-031a)

# Changelog

## v 1.0
* Added httperror log parsing
* Notice analysis now searches for same terms as sh analysis (sh are included in notice and thus we must search the same terms in both for the same results)
* Dataframes will now no longer be exported to the results sheet if they are empty. Instead a log message will display which dataframes are empty in the excel writing cell of the notebook.

## v 0.9
* Added retrieval of start and end date covered by each log listed above
* Refactored xml parsing code slightly to incorporate 'username' key allowing parsing of xmls retrieved from /xml/bookmarks

## v 0.8
* Added 'latin1' encoding to all log parsing to account for instances where logs were not in utf-8 and caused parsing errors
* Split searchFor into searchFor and shSearchFor as sh logs have different criteria to search that doesn't show up in other logs

## v 0.7
* Added payload decoding (chr() and base64) + aggregation of all payloads into 'decodedpayloads' column

## v 0.6
* Added sh log parsing
* Added common 'searchFor' var to config to hold search terms for suspicious activity that will be searched for in every log

## v 0.5
* Added parsing for the majority of notice logs (see errors for exceptions)
    * Exceptions are currently: sslvpn_aaad_login_handler and Session setup data send logs although they print via errors so you can still inspect them

## v 0.4
* Added bash log parsing
