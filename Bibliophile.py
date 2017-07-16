import os
import bibtexparser
import jsonpickle
import collections
import json

def parse_bibfiles(dirname):

    filenames = os.listdir(dirname)
    db_list = []
    for line in filenames:
        if '.bib' not in line:
            continue

        bib_file_name = dirname + line
        print("the bibfilename = {}".format(bib_file_name))
        with open(bib_file_name, encoding="utf8") as bibtex_file:
            bibtex_str = bibtex_file.read()
            bib_tex_db = bibtexparser.loads(bibtex_str)
            db_list.append(bib_tex_db)
    #    break

    return db_list

def parse_tags(inputfile):
    """
    parse tags from a .csv file
    """
    tag_list = []
    ifile = open(inputfile, 'r')
    for index, line in enumerate(ifile):
        if index is not 0:
            array = line.split(",")
            tag_list.append(array[0])

    return tag_list

def parse_articles(s_tags, m_tags, bib_db):
    die_list = []
    Article = collections.namedtuple('Article', ['title', 'authors', 'year', 'signals'])

    for bibsu in bib_db:
        die_list.append ([Article(tag['title'], tag['author'], tag['year'], tagie) for tag in bibsu.entries for tagie in s_tags if tagie in tag['title']])

    return die_list

def main():

    signal_tags = parse_tags('resources/signalTable.csv')
    metric_tags = parse_tags('resources/metricTable.csv')
    bibsit = parse_bibfiles('resources/')
    Article = collections.namedtuple('Article', ['title', 'authors', 'signals'])
    signal_tags.append('Electrodermal')
    signal_tags.append('electrodermal')
    json_articles = parse_articles(signal_tags, metric_tags, bibsit)

    fhandle = open('articles_output.json', 'w')
    for itemlist in json_articles:
        for item in itemlist:
            fhandle.write(json.dumps(item._asdict()))
            fhandle.write('\n')
            ##print("json_ouput:{}\n".format(json.dumps(item._asdict())))
            #print("json_output: title: {}, authors: {}, signals: {}\n".format(item[0],item[1],item[2]))
    fhandle.close()



# file = open("output.json",'r')
# stuff = file.read()
# unpickled_stuff = jsonpickle.decode(stuff)




if __name__ == "__main__":
    main()
