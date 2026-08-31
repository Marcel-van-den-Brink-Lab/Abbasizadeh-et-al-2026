import math
import numpy as np
from matplotlib.lines import Line2D


def format_umap_legend(
    axes,
    loc="center left",
    bbox_to_anchor=(1.01, 0.5),
    fontsize=8,
    markersize=8,
    markeredgecolor="black",
    markeredgewidth=0.25,
    max_rows=14,
    max_columns=4,
    handletextpad=0.6,
    columnspacing=1.0,
    labelspacing=0.4,
):
    """
    Reformat Scanpy/Matplotlib UMAP legends with circular markers and
    automatic multi-column layout.

    Parameters
    ----------
    axes : matplotlib.axes.Axes or iterable of Axes
        Axis or axes containing legends.
    """

    axes = np.atleast_1d(axes).ravel()

    for ax in axes:
        if ax is None:
            continue

        legend = ax.get_legend()

        if legend is None:
            continue

        old_handles = getattr(
            legend,
            "legend_handles",
            getattr(legend, "legendHandles", [])
        )

        labels = [text.get_text() for text in legend.get_texts()]

        circle_handles = []

        for handle in old_handles:
            if hasattr(handle, "get_markerfacecolor"):
                color = handle.get_markerfacecolor()

            elif hasattr(handle, "get_facecolor"):
                facecolors = handle.get_facecolor()
                color = facecolors[0] if len(facecolors) > 0 else "gray"

            else:
                color = "gray"

            circle_handles.append(
                Line2D(
                    [0],
                    [0],
                    marker="o",
                    linestyle="none",
                    markerfacecolor=color,
                    markeredgecolor=markeredgecolor,
                    markersize=markersize,
                    markeredgewidth=markeredgewidth,
                )
            )

        legend.remove()

        legend_ncol = min(
            max_columns,
            max(1, math.ceil(len(labels) / max_rows))
        )

        ax.legend(
            circle_handles,
            labels,
            loc=loc,
            bbox_to_anchor=bbox_to_anchor,
            prop={"size": fontsize},
            frameon=False,
            ncol=legend_ncol,
            handletextpad=handletextpad,
            columnspacing=columnspacing,
            labelspacing=labelspacing,
            borderaxespad=0,
        )
