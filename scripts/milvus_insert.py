from pymilvus import (

    connections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
    utility

)

import json


# ===================================
# CONNECT MILVUS
# ===================================

connections.connect(

    host="localhost",
    port="19530"

)

print("Connected to Milvus")


# ===================================
# LOAD JSON
# ===================================

with open(

    "embedded_documents.json",
    "r",
    encoding="utf-8"

) as f:

    data = json.load(f)


print("Documents Loaded:",len(data))


# ===================================
# COLLECTION NAME
# ===================================

collection_name = "subscription_policies"


# ===================================
# DELETE OLD COLLECTION (OPTIONAL)
# ===================================

if utility.has_collection(collection_name):

    utility.drop_collection(collection_name)

    print("Old Collection Deleted")


# ===================================
# CREATE SCHEMA
# ===================================

embedding_dim = len(data[0]["embedding"])


id_field = FieldSchema(

    name="id",

    dtype=DataType.INT64,

    is_primary=True,

    auto_id=True

)


embedding_field = FieldSchema(

    name="embedding",

    dtype=DataType.FLOAT_VECTOR,

    dim=embedding_dim

)


text_field = FieldSchema(

    name="text",

    dtype=DataType.VARCHAR,

    max_length=6000

)


provider_field = FieldSchema(

    name="provider",

    dtype=DataType.VARCHAR,

    max_length=200

)


policy_field = FieldSchema(

    name="policy_type",

    dtype=DataType.VARCHAR,

    max_length=100

)


source_field = FieldSchema(

    name="source_file",

    dtype=DataType.VARCHAR,

    max_length=300

)


chunk_field = FieldSchema(

    name="chunk_id",

    dtype=DataType.INT64

)


schema = CollectionSchema(

    fields=[

        id_field,
        embedding_field,
        text_field,
        provider_field,
        policy_field,
        source_field,
        chunk_field

    ],

    description="Subscription Policies"

)


collection = Collection(

    collection_name,
    schema

)

print("Collection Created")


# ===================================
# PREPARE DATA
# ===================================

embeddings = []
texts = []
providers = []
policies = []
sources = []
chunks = []


for doc in data:

    embeddings.append(doc["embedding"])

    texts.append(doc["text"])

    providers.append(doc["provider"])

    policies.append(doc["policy_type"])

    sources.append(doc["source_file"])

    chunks.append(doc["chunk_id"])


# ===================================
# INSERT DATA
# ===================================

collection.insert([

    embeddings,
    texts,
    providers,
    policies,
    sources,
    chunks

])

collection.flush()

print("Data Inserted")


# ===================================
# CREATE INDEX
# ===================================

index_params = {

    "index_type":"IVF_FLAT",

    "metric_type":"COSINE",

    "params":{"nlist":32}

}


collection.create_index(

    field_name="embedding",

    index_params=index_params

)

print("Index Created")


# ===================================
# LOAD COLLECTION
# ===================================

collection.load()

print("Collection Loaded — SEARCH READY")