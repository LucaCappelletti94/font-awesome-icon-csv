"""Test whether the CSV file is valid."""
import pandas as pd

def test_csv_validity():
    """Test whether the Font Awesome CSV file is valid."""

    # The CSV file has a two layered header.
    pd.read_csv("font_awesome.csv", header=[0, 1])