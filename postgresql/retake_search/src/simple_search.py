from retakesearch import (
    Client,
    Index,
    Database,
    Table,
    Search
)


client = Client(api_key="retake-test-key", url="http://localhost:8000")

database = Database(
    host="***",
    user="ywsung",
    # password="***",
    port=5432,
    dbname="postgres"
)

columns = ["column1"]
table = Table(
    name="table_name",
    columns=columns
)

index = client.create_index("my_index")
# Note: The table must have a primary key
index.add_source(database, table)
index.vectorize(columns)

# Keyword (BM25) search
query = Search().query("match", column1="my query")
response = index.search(query)

# Semantic (vector-based) search
query = Search().with_semantic("my_query", columns)
response = index.search(query)

# Neural (keyword + semantic) search
query = Search().with_neural("my_query", columns)
response = index.search(query)

print(response)
