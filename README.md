# Business Critical Services Operational Insights API

Example consumer script of the Business Critical Services (BCS) Operations Insights (OI) API

[![](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/bcs-apis)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/CiscoDevNet/bcs-apis/blob/master/LICENSE)
[![](https://img.shields.io/pypi/v/bcs-apis.svg)](https://pypi.python.org/pypi/bcs-apis)


## Example

```python
from bcs_oi_api import BCSOIAPI
from models import Device, SecurityAdvisory, SecurityAdvisoryBulletin, SecurityAdvisoryOutcome

bcs_oi_api = BCSOIAPI(
    client_id='client id',
    client_secret='client secret',
    region='us'
)

# Getting all discovered devices
devices = bcs_oi_api.get_output(model=Device)

# Building a dictionary with as key the device_id and the value the Device object for lookups
devices_dict = {device.device_id: device for device in devices}

# Getting all the Security Advisories
security_advisories = bcs_oi_api.get_output(model=SecurityAdvisory)

# Getting all the Security Advisory Bulletins
security_advisory_bulletins = bcs_oi_api.get_output(model=SecurityAdvisoryBulletin)

# Building a dictionary with as key the id of the bulletin and as value the bulletin itself for lookups
security_advisory_bulletins_dict = {bulletin.security_advisory_cold_id: bulletin for bulletin in
                                    security_advisory_bulletins}

# Listing devices which are vulnerable
for advisory in security_advisories:
    if advisory.match_confidence == SecurityAdvisoryOutcome.VULNERABLE:
        print(
            f"Device \"{devices_dict[advisory.device_id].device_name}\" is vulnerable to "
            f"\"{security_advisory_bulletins_dict[advisory.security_advisory_cold_id].bulletin_title}\""
        )

```

## Installation

Installing and upgrading is easy:

### Install via PIP
```
$ pip install bcsoiapi
```

### Upgrading to the latest Version

```
$ pip install bcsoiapi --upgrade
```


## Questions, Support & Discussion

bcsoiapi is a *community developed* and *community supported* project. Feedback, thoughts, questions, issues can be submitted using the issues page.

## Contribution

bcsoiapi is a *community developed* project. Code contributions are welcome via PRs!

 - [Business Cricital Services Operations Insights API](https://github.com/CiscoDevNet/bcs-apis)
 - [Issues](https://github.com/CiscoDevNet/bcs-apis/issues)

*Copyright (c) 2018-2021 Cisco and/or its affiliates.*
