import numpy as np
import csv
import argparse
import tifffile as tiff

class CSVToTIFFConverter:
    def __init__(self, file, output, width, height):
        """
        Initialize the converter with the input CSV file and output TIFF file name.
        
        :param file: Path to the input CSV file.
        :param output: Path to the output TIFF file.
        :param width: Width of the output image.
        :param height: Height of the output image.
        """
        self.file = file
        self.output = output
        self.width = width
        self.height = height

    def convert(self):
        """
        Convert the CSV file to a TIFF file.
        """
        try:
            # Initialize an empty image array with NaN values
            img = np.full((self.height, self.width), np.nan, dtype=np.float32)

            # Read the CSV file
            with open(self.file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header

                # Populate the image array
                for row in reader:
                    idx, classId = int(row[0]), float(row[1])
                    y, x = divmod(idx, self.width)
                    img[y, x] = classId
                        

            # Save the image as a TIFF file using tifffile
            tiff.imwrite(self.output, img)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """
    Main function to parse command line arguments and initiate the conversion.
    """
    # Read args from command line
    parser = argparse.ArgumentParser(description='Convert CSV to TIFF')
    parser.add_argument('--file', type=str, required=True, help='CSV file to convert')
    parser.add_argument('--output', type=str, default='output.tiff', help='Output TIFF file name')
    parser.add_argument('--width', type=int, required=True, help='Width of the output image')
    parser.add_argument('--height', type=int, required=True, help='Height of the output image')

    args = parser.parse_args()

    converter = CSVToTIFFConverter(file=args.file, output=args.output, width=args.width, height=args.height)
    converter.convert()

if __name__ == '__main__':
    main()
