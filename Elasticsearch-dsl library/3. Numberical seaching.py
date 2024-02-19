from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

# Elasticsearch credentials and configuration
ELASTIC_PASSWORD = "elastic"
ELASTIC_USERNAME = "elastic"
ELASTIC_PATH = "http://localhost:9200"
INDEX_NAME = "nba_players"


# Function to connect to Elasticsearch
def connect_to_elastic() -> Elasticsearch:
    client = Elasticsearch(
        ELASTIC_PATH,
        verify_certs=False,
        basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
    )
    return client


# Main function to execute the search query
def main():
    # Connect to Elasticsearch
    es = connect_to_elastic()

    # Create a Search object and specify the index to search in
    s = Search(using=es, index=INDEX_NAME)

    # Create a query object to find players with an average scoring of 20 or greater, and an average assist of 5 or greater
    # kibana search syntax -> avg_scoring >= 20 and avg_assist >=5
    s = s.query(Q("bool",
                  must=[Q("range", avg_scoring={"gte": 20}),
                        Q("range", avg_assist={"gte": 5})]))

    # Execute the search
    response = s.execute()

    # Print the search response
    print(f"response: \n {response}")

    # Loop over the search results and print the player's first name, last name, average scoring, and average assist
    for hit in response:
        print(hit.first_name, hit.last_name, hit.avg_scoring, hit.avg_assist)


if __name__ == '__main__':
    main()
