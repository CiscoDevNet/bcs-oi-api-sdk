# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased] - yyyy-mm-dd

### Added

### Changed

### Fixed

## [1.0.3] - 2022-05-25

### Fixed
 - Exception was raised when lastProfileTime of the collector was not available
 - Fixed scenario generating exception when JWT expired while fetching all pages of a given API endpoint

## [1.0.2] - 2022-03-16

### Fixed
 - Library does not retry after specified time when receiving 429 return code

## [1.0.1] - 2022-03-09

### Added
 - Change Log
 - GitHub Actions for type checking, code formatting and unit tests

### Changed
 - Example changed to list on `critical` security advisories
 
## [1.0.0] - 2022-03-03

### Added
First release of the Business Critical Services Operational Insights API SDK.
