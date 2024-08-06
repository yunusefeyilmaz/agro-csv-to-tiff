import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import argparse

class CSVToTIFFConverter:
    def __init__(self, file, width, height, output='output', dpi=100, cmap='gray', header=None, delimiter=','):
        self.file = file
        self.output = output
        self.width = width
        self.height = height
        self.dpi = dpi
        self.cmap = cmap
        self.header = header
        self.delimiter = delimiter

    def convert(self):
        # Read the CSV file
        df = pd.read_csv(self.file, header=self.header, names=['idx', 'classId'], dtype={'idx': 'str', 'classId': 'str'}, delimiter=self.delimiter)

        # Convert data to numeric
        df['idx'] = pd.to_numeric(df['idx'], errors='coerce')
        df['classId'] = pd.to_numeric(df['classId'], errors='coerce')

        # Drop NaN values
        df.dropna(inplace=True)

        # Convert data to numpy arrays
        idx = df['idx'].values.astype(int)
        classId = df['classId'].values.astype(int)

        # Create an empty grid
        raster_data = np.zeros((self.height, self.width), dtype=np.uint8)

        # Populate the grid with data
        for i in range(len(idx)):
            x = idx[i] % self.width
            y = idx[i] // self.width
            if y < self.height and x < self.width:
                raster_data[y, x] = classId[i]

        # Create and save the image
        fig, ax = plt.subplots(figsize=(self.width / 100, self.height / 100), dpi=self.dpi)
        cmap = plt.get_cmap(self.cmap)
        norm = mcolors.Normalize(vmin=raster_data.min(), vmax=raster_data.max())
        img = ax.imshow(raster_data, cmap=cmap, norm=norm)
        plt.axis('off')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        plt.savefig(self.output + '.tiff', format='tiff', dpi=self.dpi)
        plt.close()

def main():
    # Read args from command line
    parser = argparse.ArgumentParser(description='Convert CSV to TIFF')
    parser.add_argument('--file', type=str, required=True, help='CSV file to convert')
    parser.add_argument('--output', type=str, default='output', help='Output file name')
    parser.add_argument('--width', type=int, required=True, help='Width of the grid')
    parser.add_argument('--height', type=int, required=True, help='Height of the grid')
    parser.add_argument('--dpi', type=int, default=100, help='DPI of the output image')
    parser.add_argument('--cmap', type=str, default='gray', help='Color map of the output image')
    parser.add_argument('--header', type=int, default=None, help='Header of the CSV file')
    parser.add_argument('--delimiter', type=str, default=',', help='Delimiter of the CSV file')

    args = parser.parse_args()

    converter = CSVToTIFFConverter(
        file=args.file,
        output=args.output,
        width=args.width,
        height=args.height,
        dpi=args.dpi,
        cmap=args.cmap,
        header=args.header,
        delimiter=args.delimiter
    )
    converter.convert()

if __name__ == '__main__':
    main()