"""
DataLens — Load, clean, and visualize data in just a few lines.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

from datalens.loaders.core import load
from datalens.cleaners.core import clean, profile
from datalens.visualizers.core import plot, suggest_charts
from datalens.dashboard.core import create_dashboard

__all__ = ["load", "clean", "profile", "plot", "suggest_charts", "create_dashboard"]
