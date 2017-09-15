import sys
import os.path
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.ZigModel import ZigModel
from src.ZoneModel import ZoneModel
from src.ModelRunner import ModelRunner

def main():
    parser = argparse.ArgumentParser(description="Simulate Plane Boarding")

    parser.add_argument("--rows", "-r", help="Number of rows on the plane", default=3, nargs=1, type=int)
    parser.add_argument("--seats", "-s", help="Number of seats on each side of the aisle of the plane", default=3, nargs=1, type=int)
    parser.add_argument("--visualize", "-v", help="Display Visualizer", default=False, action="store_true")
    parser.add_argument("--model", "-m", help="Model to use", default="zig", choices=["zig", "zone"], type=str)

    args = parser.parse_args()

    if (args.model == "zip"):
        model = ZigModel()
    else:
        model = ZoneModel()

    runner = ModelRunner()
    runner.run(model, args.rows, args.seats, args.visualize)

if __name__ == '__main__':
    main()
