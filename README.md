# Data repository for the RAW to ACES Utility 

## Table of Contents
1. [Introduction](#introduction)
2. [Package Contents](#package-contents)
3. [JSON Schema for Spectral Datasets](#schema)
4. [License](#license)

## Introduction
This is the data repository for the RAW to ACES Utility or `rawtoaces` (https://github.com/AcademySoftwareFoundation/rawtoaces), a software package that converts digital camera RAW files to ACES container files containing image data encoded according to the Academy Color Encoding Specification (ACES) as specified in [SMPTE 2065-1](http://ieeexplore.ieee.org/document/7289895/). The output image complies with the ACES Container specification [(SMPTE S2065-4)](http://ieeexplore.ieee.org/document/7290441).

## Package Contents

The repository contains the following:

* [`camera/`](./camera) - camera spectral sensitivities
* [`illuminant/`](./illuminant) - light source spectral power distribution
* [`cmf/`](./cmf) - color matching functions (CIE-1931)
* [`training/`](./training) - 190 training patch dataset
	
## JSON Schema for Spectral Datasets

The schema takes its roots in [IES TM-27-14](http://www.techstreet.com/standards/ies-tm-27-14?product_id=1881073) but implements support for multiple spectral datasets while adopting [JSON](http://www.json.org/) over [XML](https://www.w3.org/TR/REC-xml/) for the simplicity of its grammar.

`rawtoaces` expects the spectral dataset to have the following shape: **(380, 780, 5)**, i.e. starting from 380nm and ending at 780nm with a 5nm interval/bin size.

The attributes are defined as follows:

- `header`
    - `schema_version`
        - **description**: *Required*, schema version of the current document.
        - **type**: `"string"`
    - `catalog_number`
        - **description**: *Optional*,
        - **type**: `["string", "null"]`
    - `comments`
        - **description**: *Optional*, additional information for the spectral dataset.
        - **type**: `["string", "null"]`
    - `description`
        - **description**: *Required*, description of the spectral dataset.
        - **type**: `"string"`
    - `document_creation_date`
        - **description**: *Required*, document creation date expressed as per RFC 3339 - Date and Time on the Internet: Timestamps, e.g. 2017-01-01T12:00:00Z.
        - **type**: `"string"`
        - **format**: `"date-time"`
    - `document_creator`
        - **description**: *Required*, creator of the document, e.g. company, individual, laboratory, etc.
        - **type**: `"string"`
    - `laboratory`
        - **description**: *Optional*, laboratory or company that performed the measurements.
        - **type**: `["string", "null"]`
    - `license`
        - **description**: *Required*, usage license of the document, e.g. "CC-BY-NC-ND".
        - **type**: `["string", "null"]`
    - `manufacturer`
        - **description**: *Optional*, manufacturer of the device being tested.
        - **type**: `["string", "null"]`
    - `measurement_equipment`
        - **description**: *Optional*, measurement equipment used to test the device.
        - **type**: `["string", "null"]`
    - `model`
        - **description**: *Optional*, model of the device being tested.
        - **type**: `["string", "null"]`
    - `unique_identifier`
        - **description**: *Optional*, generated unique identifier for the document, e.g. SHA256.
        - **type**: `["string", "null"]`
- `spectral_data`
    - `bandwidth_FWHM`
        - **description**: *Optional*, spectro-radiometer full-width at half-maximum bandwidth in nm.
        - **type**: `["number", "null"]`
    - `bandwidth_corrected`
        - **description**: *Optional*, whether bandwidth correction has been applied to the spectral data.
        - **type**: `["boolean", "null"]`
    - `data`
        - **description**: *Required*, defines the spectral dataset, requiring at least one *key* from `index` whose *value* is an *object* containing wavelength/value pairs.
        - **type**: `"object"`
    - `index`
        - **description**: *Required*, indexes the spectral dataset.
        - **type**: `"object"`
    - `reflection_geometry`
        - **description**: *Required* if `units` is *reflectance*, reflection geometry attributes as per CIE 15:2004.
        - **type**: `["string", "null"]`
        - **enum**: `["di:8", "de:8", "8:di", "8:de", "d:d", "d:0", "45a:0", "45c:0", "0:45a", "45x:0", "0:45x", "other", null]`
    - `transmission_geometry`
        - **description**: *Required* if `units` is *transmittance*, transmission geometry attributes as per CIE 15:2004.
        - **type**: `["string", "null"]`
        - **enum**: `["0:0", "di:0", "de:0", "0:di", "0:de", "d:d", "other", null]`
    - `units`
        - **description**: *Required*, unit or quantity of measurement for the spectral dataset.
        - **type**: `"string"`
        - **enum**: `["flux", "absorptance", "transmittance", "reflectance", "intensity", "irradiance", "radiance", "exitance", "R-Factor", "T-Factor", "relative", "other"]`

The full JSON schema for spectral datasets can be used to validate a new user file using a [validator](http://www.jsonschemavalidator.net/) and is defined in [schema_0.1.0.json](./schema_0.1.0.json)

## Licence

rawtoaces-data is licensed under the [Apache-2.0 license](./LICENSE).
