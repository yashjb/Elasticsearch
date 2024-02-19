from elasticsearch import Elasticsearch
from pprint import pprint

ELASTIC_PASSWORD = "elastic"
ELASTIC_USERNAME = "elastic"
ELASTIC_PATH = "http://localhost:9200"
INDEX_NAME = "nba_players"


def connect_to_elastic() -> Elasticsearch:
    client = Elasticsearch(
        ELASTIC_PATH,
        verify_certs=False,
        basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
    )
    return client


def main():
    es = connect_to_elastic()
    # create a query dict that matches documents where the 'avg_assist' field is less than 7 and the 'avg_scoring'
    # field is greater than 10
    # kibana search syntax -> avg_scoring > 10 and avg_assist < 5
    query = {
        "query": {
            "bool": {
                "must": [
                    {"range": {"avg_scoring": {"gt": 10}}},
                    {"range": {"avg_assist": {"lt": 7}}}
                ]
            }
        }
    }
    # execute the search and print the results
    response = es.search(index=INDEX_NAME, body=query)

    # get only the documents
    for hit in response['hits']['hits']:
        print(hit['_source'])


if __name__ == '__main__':
    main()
