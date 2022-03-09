# Business Critical Services Operational Insights API SDK

SDK for the Business Critical Services (BCS) Operations Insights (OI) API

[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/CiscoDevNet/bcs-oi-api-sdk/blob/master/LICENSE.md)
[![](https://img.shields.io/pypi/v/bcs-oi-api.svg)](https://pypi.python.org/pypi/bcs-oi-api)

## Example

```python
from bcs_oi_api import BCSOIAPI
from bcs_oi_api.models import Device, SecurityAdvisory, SecurityAdvisoryBulletin, SecurityAdvisoryOutcome

bcs_oi_api = BCSOIAPI(
    client_id='client id',
    client_secret='client secret',
    region='us'
)

# Getting a generator for all discovered devices
devices = bcs_oi_api.get_output(model=Device)

# Building a dictionary with as key the device_id and the value the Device object for lookups
devices_dict = {device.device_id: device for device in devices}

# Getting a generator for all the Security Advisories
security_advisories = bcs_oi_api.get_output(model=SecurityAdvisory)

# Getting a generator for all the Security Advisory Bulletins
security_advisory_bulletins = bcs_oi_api.get_output(model=SecurityAdvisoryBulletin)

# Building a dictionary with as key the id of the bulletin and as value the bulletin itself for lookups
security_advisory_bulletins_dict = {bulletin.security_advisory_cold_id: bulletin for bulletin in
                                    security_advisory_bulletins}

# Listing devices which are vulnerable to security advisories with a critical impact rating
for advisory in security_advisories:
    if advisory.match_confidence == SecurityAdvisoryOutcome.VULNERABLE and \
            security_advisory_bulletins_dict[advisory.security_advisory_cold_id].security_impact_rating == 'Critical':
        print(
            f"Device \"{devices_dict[advisory.device_id].device_name}\" is vulnerable to "
            f"\"{security_advisory_bulletins_dict[advisory.security_advisory_cold_id].bulletin_title}\""
        )

```

## Installation

Installing and upgrading is easy:

### Install via PIP
```
$ pip install bcs-oi-api
```

### Upgrading to the latest Version

```
$ pip install bcs-oi-api --upgrade
```


## Questions, Support & Discussion

bcs-oi-api is a *community developed* and *community supported* project. Feedback, thoughts, questions, issues can be submitted using the issues page.

## Contribution

bcs-oi-api is a *community developed* project. Code contributions are welcome via PRs!

 - [Business Cricital Services Operations Insights API](https://developer.cisco.com/docs/bcs-operational-insights)
 - [Issues](https://github.com/CiscoDevNet/bcs-oi-api-sdk/issues)

*Copyright (c) 2018-2021 Cisco and/or its affiliates.*
