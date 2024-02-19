from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "elastic"
ELASTIC_USERNAME = "elastic"
ELASTIC_PATH = "http://localhost:9200"
INDEX_NAME = "nba_players"
# ASYNC_SEARCH_INDEX_NAME = ".async-search"  


def connect_to_elastic() -> Elasticsearch:
    client = Elasticsearch(
        ELASTIC_PATH,
        verify_certs=False,
        basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
    )
    return client


# def remove_read_only_allow_delete_block(client: Elasticsearch, index_name: str):
#     client.indices.put_settings(index=index_name, body={"settings": {"index.blocks.read_only_allow_delete": None}})

def main():
    document_to_update = {
        "doc": {'first_name': 'LeBron', 'last_name': 'James', 'date_of_birth': '1984-12-30', 'position': 'PF',
                'team': 'Chennai Super Kings',
                'avg_scoring': 25.4, 'avg_rebound': 7.9, 'avg_assist': 7.9, 'country': 'USA'}}

    client = connect_to_elastic()

    # remove_read_only_allow_delete_block(client, INDEX_NAME)

    # Remove read-only-allow-delete block for .async-search index
    # remove_read_only_allow_delete_block(client, ASYNC_SEARCH_INDEX_NAME)

    result = client.update(index=INDEX_NAME, id=0, body=document_to_update)

    print(result)


if __name__ == '__main__':
    main()
