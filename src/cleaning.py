"""Functions used for the cleaning phase of the dataset."""

import math
import re
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import pandas as pd

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure


def camel_to_snake(name: str) -> str:
    """Convert camelCase/PascalCase to snake_case.

    Args:
        name (str): string to be formatted
    Returns:
        str: formatted string
    """
    pattern = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
    return pattern.sub("_", name).lower()


def spaces_to_snake(name: str) -> str:
    """Convert strings separated by spaces (e.g. Lorem Ipsum) to snake_case (e.g. lorem_ipsum).

    Args:
        name (str): string to be formatted
    Returns:
        str: formatted string
    """
    return name.replace(" ", "_").lower()


def reorder_cols(cols: list[str], pk: str, target: str) -> list[str]:
    """Reorder columns for better readability of the data.

    This function sets the PK as the first column, the target as the last and the
    other columns alphabetically.

    Args:
        cols (list[str]): List of columns
        pk (str): Primary key
        target (str): Target Variable
    Returns:
        list[str]: Ordered list of columns
    """
    cols.remove(pk)
    cols.remove(target)
    cols.sort()
    return [pk, *cols, target]


def missing_values_table(df: pd.DataFrame, filter_none: bool = False) -> pd.DataFrame:  # noqa: FBT001, FBT002
    """Creates a dataframe that summarize information about missing values in the dataset.

    Args:
        df (pd.DataFrame): DataFrame to be analyzed
        filter_none (bool, optional): If True, exclude columns that have no missing values. Defaults to False
    Returns:
        pd.DataFrame: Summary table of missing values
    """
    total_lines = len(df)
    missing_count = df.isna().sum()
    missing_percent = (missing_count / total_lines) * 100

    # 4. Combine everything into a new DataFrame
    summary_df = pd.DataFrame(
        {
            "% missing": missing_percent,
            "# total": total_lines,
            "# missing": missing_count,
        }
    )

    summary_df = summary_df.sort_values(by="% missing", ascending=False)
    summary_df["% missing"] = summary_df["% missing"].round(3)

    if filter_none:
        summary_df = summary_df[summary_df["# missing"] > 0]

    return summary_df


def uniques_by_col(df: pd.DataFrame, columns: list[str]) -> dict:
    """Get the unique values on a dataframe for the specified columns.

    Args:
        df (pd.DataFrame): DataFrame to analyze
        columns (list[str]): Columns to find uniques

    Returns:
        dict: Unique values for each column
    """
    uniques = {}
    for c in columns:
        uniques[c] = list(df[c].unique())

    return uniques


def plot_boxplots_grid(
    df: pd.DataFrame, columns: list[str], plots_per_row: int = 3
) -> tuple[Figure, list[Axes]]:
    """Plot a grid of boxplots for a list of columns with a specified number of plots per row.

    Args:
        df (pd.DataFrame): Dataframe containing the data
        columns (list[str]): List of columns to plot
        plots_per_row (int, optional): Number of plots per row. Defaults to 3.
    """
    num_rows = math.ceil(len(columns) / plots_per_row)
    fig, axes = plt.subplots(
        num_rows, plots_per_row, figsize=(5 * plots_per_row, 4 * num_rows)
    )
    axes = [axes] if isinstance(axes, plt.Axes) else axes.flatten()

    for i, col in enumerate(columns):
        df.boxplot(column=col, ax=axes[i], grid=False)
        axes[i].set_title(f"{col}", fontsize=12, fontweight="bold")
        axes[i].set_ylabel("Values")

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    return fig, fig.axes
