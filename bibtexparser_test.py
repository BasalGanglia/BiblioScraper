
# bibtex = """@ARTICLE{Cesar2013,
#   author = {Jean César},
#   title = {An amazing title},
#   year = {2013},
#   month = jan,
#   volume = {12},
#   pages = {12--23},
#   journal = {Nice Journal},
#   abstract = {This is an abstract. This line should be long enough to test
#      multilines...},
#   comments = {A comment},
#   keywords = {keyword1, keyword2}
# }
# """
#
# with open('bibtex.bib', 'w') as bibfile:
#     bibfile.write(bibtex)



import bibtexparser

with open('bibtex.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)
print(bib_database.entries)

with open('../resources/ch2_eda_bib.bib') as bibtex_file:
  #  edabibs = bibtex_file.read()
    bib_database = bibtexparser.load(bibtex_file)
len(edabibs)

bib_database.entries