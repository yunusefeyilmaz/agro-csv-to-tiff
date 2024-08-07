import pandas as pd
import numpy as np
from PIL import Image
import argparse

class CSVToTIFFConverter:
    def __init__(self, file, width, height, output='output', header=None, delimiter=','):
        self.file = file
        self.output = output
        self.width = width
        self.height = height
        self.header = header
        self.delimiter = delimiter

    def convert(self):
        try:
            # Read the CSV file
            df = pd.read_csv(self.file, header=self.header, names=['idx', 'classId'], dtype={'idx': 'str', 'classId': 'str'}, delimiter=self.delimiter)

            # Convert data to numeric and drop NaN values
            df['idx'] = pd.to_numeric(df['idx'], errors='coerce')
            df['classId'] = pd.to_numeric(df['classId'], errors='coerce')
            df.dropna(inplace=True)

            # Convert data to numpy arrays
            idx = df['idx'].values.astype(int)
            classId = df['classId'].values.astype(int)

            # Create an empty RGBA grid (R=Gray, A=Alpha)
            raster_data = np.zeros((self.height, self.width, 2), dtype=np.uint8)

            # Populate the grid with data
            x_coords = idx % self.width
            y_coords = idx // self.width
            valid_indices = (y_coords < self.height) & (x_coords < self.width)
            raster_data[y_coords[valid_indices], x_coords[valid_indices], 0] = classId[valid_indices]  # Set gray value
            raster_data[y_coords[valid_indices], x_coords[valid_indices], 1] = 255  # Set alpha to 255 (opaque) where there's data

            # Convert to grayscale with alpha
            img = Image.fromarray(raster_data, mode='LA')  # 'LA' mode for grayscale with alpha
            img.save(self.output + '.tiff', format='TIFF')
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    # Read args from command line
    parser = argparse.ArgumentParser(description='Convert CSV to TIFF')
    parser.add_argument('--file', type=str, required=True, help='CSV file to convert')
    parser.add_argument('--output', type=str, default='output', help='Output file name')
    parser.add_argument('--width', type=int, required=True, help='Width of the grid')
    parser.add_argument('--height', type=int, required=True, help='Height of the grid')
    parser.add_argument('--header', type=int, default=None, help='Header of the CSV file')
    parser.add_argument('--delimiter', type=str, default=',', help='Delimiter of the CSV file')

    args = parser.parse_args()

    converter = CSVToTIFFConverter(
        file=args.file,
        output=args.output,
        width=args.width,
        height=args.height,
        header=args.header,
        delimiter=args.delimiter
    )
    converter.convert()

if __name__ == '__main__':
    main()
