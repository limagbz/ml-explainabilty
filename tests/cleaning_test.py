"""Unit tests for `cleaning.py`."""

import re
from contextlib import nullcontext

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from src.cleaning import (
    camel_to_snake,
    missing_values_table,
    plot_boxplots_grid,
    reorder_cols,
    spaces_to_snake,
    uniques_by_col,
)


@pytest.mark.parametrize(
    ("case", "expected"),
    [
        ("camelCase", "camel_case"),
        ("PascalCase", "pascal_case"),
        ("already_snake", "already_snake"),
        ("simple", "simple"),
        ("HTTPResponse", "http_response"),
    ],
)
def test_camel_to_snake(case, expected):
    assert camel_to_snake(case) == expected


@pytest.mark.parametrize(
    ("case", "expected"),
    [
        ("some spaces here", "some_spaces_here"),
        ("Already_Underscored", "already_underscored"),
        ("mixed Case spaces", "mixed_case_spaces"),
    ],
)
def test_spaces_to_snake(case, expected):
    assert spaces_to_snake(case) == expected


@pytest.mark.parametrize(
    ("case", "expected", "exception"),
    [
        (
            ["col1", "target_col", "pk_col", "col2"],
            ["pk_col", "col1", "col2", "target_col"],
            nullcontext(),
        ),
        (
            ["col1", "target_col"],
            None,
            pytest.raises(ValueError, match=re.escape("list.remove(x): x not in list")),
        ),
        (
            ["col1", "pk_col"],
            None,
            pytest.raises(ValueError, match=re.escape("list.remove(x): x not in list")),
        ),
    ],
)
def test_reorder_cols(case, expected, exception):
    with exception:
        assert reorder_cols(case, "pk_col", "target_col") == expected


def test_missing_values_table():
    df = pd.DataFrame(
        {
            "A": [1, 2, np.nan, 4, np.nan],  # 2 missing (40%)
            "B": [1, 2, 3, 4, 5],  # 0 missing (0%)
            "C": [np.nan, np.nan, np.nan, np.nan, np.nan],  # 5 missing (100%)
        }
    )

    # Case 01: Without filter
    res_df = missing_values_table(df, filter_none=False)

    assert list(res_df.columns) == ["% missing", "# total", "# missing"]
    assert list(res_df.index) == ["C", "A", "B"]  # Index should be ordered by %missing\
    assert res_df.loc["A", "# total"] == 5
    assert res_df.loc["A", "# missing"] == 2
    assert res_df.loc["A", "% missing"] == 40.0
    assert res_df.loc["B", "# total"] == 5
    assert res_df.loc["B", "# missing"] == 0
    assert res_df.loc["B", "% missing"] == 0.0
    assert res_df.loc["C", "# total"] == 5
    assert res_df.loc["C", "# missing"] == 5
    assert res_df.loc["C", "% missing"] == 100.0

    # Case 02: With filter
    res_df_filtered = missing_values_table(df, filter_none=True)

    assert list(res_df_filtered.columns) == ["% missing", "# total", "# missing"]
    assert "B" not in res_df_filtered.index
    assert list(res_df_filtered.index) == ["C", "A"]


def test_uniques_by_col():

    df = pd.DataFrame(
        {
            "COL1": ["a", "b", "c", "d", "e"],  # No uniques
            "COL2": ["a", "b", "b", "c", "c"],  # 3  Uniques
            "COL3": ["c", "c", "c", "c", "c"],  # All unique
            "COL4": ["d", "d", "e", "f", "g"],  # Skipped
        }
    )

    uniques = uniques_by_col(df, ["COL1", "COL2", "COL3"])

    assert uniques["COL1"] == ["a", "b", "c", "d", "e"]
    assert uniques["COL2"] == ["a", "b", "c"]
    assert uniques["COL3"] == ["c"]
    assert "COL4" not in list(uniques)


def test_plot_boxplots_grid():

    df = pd.DataFrame(
        {
            "COL1": [1, 2, 3],
            "COL2": [4, 5, 6],
            "COL3": [7, 8, 9],
        }
    )

    # Case 01: Multiple Plots
    fig, axes = plot_boxplots_grid(df, ["COL1", "COL2", "COL3"], plots_per_row=2)

    assert len(axes) == 3
    assert axes[0].get_title() == "COL1"
    assert len(axes[0].lines) > 0
    assert axes[1].get_title() == "COL2"
    assert len(axes[1].lines) > 0
    assert axes[2].get_title() == "COL3"
    assert len(axes[2].lines) > 0

    plt.close(fig)

    # Case 02: Unique Plot
    fig, axes = plot_boxplots_grid(df, ["COL1"], plots_per_row=2)

    assert len(axes) == 1
    assert axes[0].get_title() == "COL1"
    assert len(axes[0].lines) > 0

    plt.close(fig)
