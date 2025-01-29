import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

class Visualizer:

    @staticmethod
    def _is_plottable(data: pd.DataFrame, x_col: str, y_col: str) -> bool:
        """
        Returns True if:
        - data is not empty
        - both x_col and y_col exist in data
        - both x_col and y_col are numeric or at least convertible to numeric
        """
        # If there's nothing to plot
        if data.empty:
            return False

        # Check if columns exist
        if x_col not in data.columns or y_col not in data.columns:
            return False

        # Optional check: ensure columns can be interpreted as numeric
        # (for bar_chart, line_chart, scatter_plot).
        # If your X-axis is categorical, you might relax the numeric check for x_col.
        try:
            pd.to_numeric(data[x_col])
            pd.to_numeric(data[y_col])
        except ValueError:
            # If either column cannot be converted to numeric
            return False

        return True

    @staticmethod
    def bar_chart(data: pd.DataFrame, x_col: str, y_col: str):
        if not Visualizer._is_plottable(data, x_col, y_col):
            # Do nothing if not plottable
            return

        fig, ax = plt.subplots()
        ax.bar(data[x_col], data[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    @staticmethod
    def line_chart(data: pd.DataFrame, x_col: str, y_col: str):
        if not Visualizer._is_plottable(data, x_col, y_col):
            return

        fig, ax = plt.subplots()
        ax.plot(data[x_col], data[y_col], marker="o")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    @staticmethod
    def scatter_plot(data: pd.DataFrame, x_col: str, y_col: str):
        if not Visualizer._is_plottable(data, x_col, y_col):
            return

        fig, ax = plt.subplots()
        ax.scatter(data[x_col], data[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        plt.xticks(rotation=45)
        st.pyplot(fig)
