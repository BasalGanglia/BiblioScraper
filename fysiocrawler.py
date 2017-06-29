# Fysio Crawler

"""

Crawls Google Scholar

"""
from scholar import ScholarQuerier
from scholar import ScholarSettings
from scholar import SearchScholarQuery
from scholar import ClusterScholarQuery
import jsonpickle
import time

def superquery(wordone, wordtwo, cluster_id=None):
    """
    Fetches stuff from Google Scholar
    """
    time.sleep(1)
    print "querying"
    querier = ScholarQuerier()
    settings = ScholarSettings()

    settings.set_citation_format(ScholarSettings.CITFORM_BIBTEX)

    querier.apply_settings(settings)

    query = SearchScholarQuery()


    query.set_num_page_results(5)
    query.set_include_citations(True)
    # if cluster_id:
    #     query = ClusterScholarQuery(cluster=cluster_id)
    # else:
    query.set_words([wordone, wordtwo])
        # query.set_author(['ilkka kosunen'])
    querier.send_query(query)
    querier.save_cookies()

    articles = []

    for art in querier.articles:
        articles.append(art)


    return articles

def recursivesearch(lista, fetcheditems):
    """
    Crawls Google Scholar recursively
    """
    # print "Recursive\n"
    for art in lista:
        # print "Title:\t" + art['title']
        # print "URL:\t" + art['url']
        # print "Year:\t" + art['year']
        # print "Excerpt:" + art['excerpt']
        # print "Cluster ID:" + art['cluster_id']
        # print "\n"
        if not fetcheditems.has_key(art['cluster_id']):
            if len(fetcheditems) < 10:
                fetcheditems[art['cluster_id']] = art

    print str(len(fetcheditems))
    return fetcheditems

def readtags(inputfile, fetcheditems):
    """
    Reads tags and queries files
    """
    for index, line in enumerate(inputfile):
        if index is not 0:
            array = line.split(",")
            fetcheditems = recursivesearch(superquery(array[0], array[1]), fetcheditems)
        if len(fetcheditems) >= 10:
            return fetcheditems
    return fetcheditems


def main():
    """
    Main method
    """
    # lista = superquery()
    fetcheditems = {}
    inputfile = open('input.csv', 'r')
    fetcheditems = readtags(inputfile, fetcheditems)
    pickled = jsonpickle.encode(fetcheditems)
    output = open('output.json', 'w')
    output.write(pickled)
    output.close()
    inputfile.close()

if __name__ == "__main__":
    main()





