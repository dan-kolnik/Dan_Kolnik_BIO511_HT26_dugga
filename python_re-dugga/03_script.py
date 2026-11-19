# Q3


import argparse
import pandas as pd
import matplotlib.pyplot as plt

# Task C

parser = argparse.ArgumentParser(
    description="Scatter plot of copy_number against log2_ratio")
parser.add_argument("input_file", nargs="?", default="cnv_data.csv",
                    help="CSV file to read (default: cnv_data.csv)")
parser.add_argument("output_file", nargs="?", default="cnv_plot.png",
                    help="image file to save (default: cnv_plot.png)")
args = parser.parse_args()


# Task A

df = pd.read_csv(args.input_file)

plt.figure(figsize=(10,5))
plt.scatter(df["log2_ratio"], df["copy_number"], s=10, alpha=0.6)
plt.xlabel("log2_ratio")
plt.ylabel("copy_number")
plt.title("Copy number variation")


# Task B

plt.savefig(args.output_file, dpi=150, bbox_inches="tight")
print(f"Plot saved to '{args.output_file}'")