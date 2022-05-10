# Bibliometry utils

A collection of tools and utils to help with bibliometric research.

## Google Scholar (GS) utils

### Author info collecting
This tool collects information about an authors publications (titles, number of citations, years of publication) from the author's Google Scholar page and saves it to a CSV file.

#### Usage
The usage is simple you have to give the program only one parameter '--author_gs_page'. Try following examples to collect info about Albert Einstein and Stephen Hawking publications:

python coll_auth_info_GS.py --author_gs_page=https://scholar.google.com/citations?user=qc6CJjYAAAAJ

python coll_auth_info_GS.py --author_gs_page=https://scholar.google.com/citations?user=-AEEg5AAAAAJ

#### TODO:
1. Add calculation of statistics for an author:
- Hirch index.
- h10-index.
- Publications/citations by year.
- Co-author stats.
- Journal stats.
2. Citation graph.
3. Publication topic stats.
4. Keyword stats.

### Article citation stats by year
To be published soon.

## Referencing
If you find the Bibliometry utils useful, please cite it as:
@misc{bib_utils2022,
  author = {Iskander, Akhmetov},
  title = {Bibliometry utils},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/iskander-akhmetov/Bibliometry_utils/}}
}


