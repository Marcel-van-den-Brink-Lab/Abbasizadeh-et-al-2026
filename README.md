# Activated dendritic cells sustain regulatory T cell-mediated thymic repair after injury

### AT A GLANCE


This repository contains analysis workflows associated with the manuscript: **"Activated dendritic cells sustain regulatory T cell-mediated thymic repair after injury"** *Abbasizadeh et al., 2026*

The repository includes:

- Analysis of newly generated mouse thymic single-cell RNA-sequencing datasets produced in this study. GEO accession: [GSE331141](https://www.ncbi.nlm.nihry/acc.cgi?acc=GSE331141) (parabiosis) and [GSE345985](https://www.ncbi.nlm.nihry/acc.cgi?acc=GSE345985) (CD4 PBS/DT)
- Re-analysis of a published murine thymic regeneration single-cell RNA-sequencing dataset. GEO accession: [GSE244673](https://www.ncbi.nlm.nihry/acc.cgi?acc=GSE244673)
- Re-analysis and de novo annotation of a published human thymic single-cell RNA-sequencing atlas. GEO accession: [GSE207204](https://www.ncbi.nlm.nih.gov/c.cgi?acc=GSE207204).


## Notebook summary

Notebooks are organized into subdirectories corresponding to independent scRNA-seq experiments. Each notebook builds on the output of the preceding notebook within its directory and should be run sequentially.

### `0 PARABIOSIS/` — Parabiosis scRNA-seq (GSE331141)

Analysis of thymic scRNA-seq data from parabiotic mice at steady state and day 1 post-injury. Samples include host and donor thymi under steady-state (SS_HOST, SS_DONOR) and day 1 post-injury (DAY1_HOST, DAY1_DONOR) conditions.

| Notebook | Description |
|----------|-------------|
| 0 QC.ipynb | Read 10x Genomics filtered feature–barcode matrices, concatenate samples, assign condition labels, and perform quality control filtering |
| 1 BROAD ANNOTATIONS.ipynb | Leiden clustering and marker-based annotation of broad cell types (DN_DP, SP, B, Myeloid, ILC) on the QC-filtered object |
| 2 DN DP.ipynb | Sub-clustering and iterative annotation of the DN/DP compartment into DN1, DN2, DN3, DN4, DP(P), DP(Q), DP(Sel), agonist-selected T cells, Tregs, gamma-delta T cells, CD4 SP, and CD8 SP subsets |
| 3 SP.ipynb | Sub-clustering and annotation of the SP compartment into CD4, CD8, CD4 Immature, CD8 Immature, DP(Sel), pTreg, and Treg subsets |
| 4 BCELLS.ipynb | Sub-clustering and annotation of B cells into Naive, Memory, and Plasma subsets |
| 5 ILC.ipynb | Sub-clustering and annotation of the ILC/NK compartment into ILCP, ILC1, ILC2, ILC3, NK, CD4 T, and CD8(GZMK+) subsets |
| 6 MYELOID.ipynb | Sub-clustering and annotation of the myeloid compartment into cDC1, cDC2, pDC, and aDC (activated dendritic cell) subsets |
| 7 MAP SUBSETS.ipynb | Map all cell-type subset annotations from notebooks 2–6 back onto the full dataset and generate the final annotated object |
| 8 DEG.ipynb | Differential expression analysis (Wilcoxon rank-sum) across multiple condition comparisons: recirculating vs. resident cells at steady state and day 1, and combined timepoint analyses; results exported to Excel |

### `1 CD4 PBS DTR/` — CD4 PBS vs. DT scRNA-seq ()

Analysis of thymic CD4 T cell scRNA-seq data comparing PBS-treated controls to diphtheria toxin (DT)-treated mice.

| Notebook | Description |
|----------|-------------|
| 0 QC.ipynb | Read 10x Genomics filtered feature–barcode matrices for PBS and DT samples, concatenate, and perform quality control filtering |
| 1 ANNOTATIONS.ipynb | Leiden clustering and marker-based annotation of CD4 T cell subsets: Activated, Naive, Proliferating, STAT1hi, and Treg |
| 2 DEG.ipynb | Differential expression analysis (Wilcoxon rank-sum) comparing DT vs. PBS conditions; results exported to Excel |

### `2 PUBlIC/` — MOUSE DCs (GSE244673)


| Notebook | Description |
|-----------|-----------|
| MOUSE DC REANALYSIS.ipynb | Re-analysis of activated dendritic cells (aDCs), cDC1s and cDC2s from GSE244673 |

### `2 PUBlIC/` — HUMAN DCs (GSE207204)

| Notebook | Description |
|-----------|-----------|
| HUMAN DC REANALYSIS.ipynb | Re-analysis and de novo annotation of the human thymic atlas from GSE207204 |


### GETTING STARTED

### Prerequisites

- Conda (Miniconda or Anaconda)
- Jupyter Notebook or JupyterLab
- Python packages specified within the environment file


### Setup

Analyses were performed using notebook-specific conda environments to maximize reproducibility and maintain compatibility across independent workflows.
Separate conda environments were used for individual analyses. The environment definition file is provided in the `envs/` directory and contains pinned package versions for the full dependency tree.

Create and activate the environment required for a given notebook:

```bash
conda env create -f envs/<environment>.yml
conda activate <environment>
```


### Reproducing the analysis

#### Analysis of datasets

1. Download processed data from the appropriate GEO accession (`GSE331141` for parabiosis, `TOADD` for CD4 PBS/DT, `GSE244673` for public mouse DCs, `GSE207204` for public human DCs).
2. Place downloaded files in the expected location within the `data/` directory.
3. Create and activate the conda environment as described above.
4. For public dataset analyses, ensure that `src/format_umap.py` is available locally and importable by the notebooks.
5. Run the notebooks within each subdirectory sequentially (0, 1, 2, ...) from beginning to end.


## Citation

If you use this repository, please cite:

> Abbasizadeh et al. (2026). *Activated dendritic cells sustain regulatory T cell-mediated thymic repair after injury*. Journal. DOI: to be added upon publication.

Machine-readable citation metadata are provided in:

```text
CITATION.cff
```

# License

Released under the MIT License. See [LICENSE](LICENSE) for details.
