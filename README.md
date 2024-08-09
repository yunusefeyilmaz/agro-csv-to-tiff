# CSV to GeoTIFF Converter

## Overview

This script converts CSV files to GeoTIFF format. Each row in the CSV file should represent a pixel value in the image, and the script reconstructs the image with the specified dimensions and geospatial properties.

For converting GeoTIFF files to CSV format, refer to the ***[TIFF to CSV Converter repository](https://github.com/yunusefeyilmaz/agro-tiff-to-csv)***.

## Features

- **CSV to GeoTIFF Conversion**: Converts pixel values from CSV to GeoTIFF format.
- **Geospatial Metadata**: Allows setting pixel size, coordinate bounds, and projection (EPSG code).
- **Error Handling**: Manages exceptions and handles missing values (NaN).

## Installation

Ensure you have the required libraries installed:

```bash
pip install numpy gdal
```
## Usage

#### Command-Line Arguments
- --file (required): Path to the input CSV file.
- --output (optional): Path to the output TIFF file. Defaults to output.tiff.
- --width (required): Width of the output image.
- --height (required): Height of the output image.
- --pixel_size (optional): Size of each pixel in the output image. Defaults to 1000.
- --x (optional): Minimum x coordinate. Defaults to 0.0.
- --y (optional): Maximum y coordinate. Defaults to 0.0.
- --epsg (optional): EPSG code of the projection. Defaults to 4326.

#### Example Command
```bash
python csv_to_geotiff.py --file input_data.csv --output output_image.tiff --width 1024 --height 768 --pixel_size 1000 --x 0 --y 0 --epsg 4326
```
