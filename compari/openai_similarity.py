# Obtinem distanta dintre 2 stringuri folosind API-ul OpenAI
# https://platform.openai.com/
# https://platform.openai.com/docs/guides/embeddings
import openai
import os
from dotenv import load_dotenv
import json 
from openai.embeddings_utils import (
    get_embedding,
    distances_from_embeddings,
    tsne_components_from_embeddings,
    chart_from_components,
    indices_of_nearest_neighbors_from_distances,
)

# constants
EMBEDDING_MODEL = "text-embedding-ada-002"

# Load the .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Textele pe care doriți să le comparați
text1 = "Primul text pe care doriți să-l comparați."
text2 = "Al doilea text pe care doriți să-l comparați."
text3 = "Masina de cusut Singer 2250 Tradition, 10 programe, 85W, Alb"
text4 = "Alt text pe care doriți să-l comparați."
text5 = "Baterie externa"
text6 = "Baterie externa"

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

embeddings = []
embeddings.append(get_embedding(text1))
embeddings.append(get_embedding(text2))
embeddings.append(get_embedding(text3))
embeddings.append(get_embedding(text4))
embeddings.append(get_embedding(text5))
embeddings.append(get_embedding(text6))


# get embeddings for the texts (function from embeddings_utils.py)
query_embedding = get_embedding(text1)

# get distances between the source embedding and other embeddings (function from embeddings_utils.py)
distances = distances_from_embeddings(query_embedding, embeddings, distance_metric="cosine")

print(distances)




def recommendations_from_strings(
   strings: list[str],
   index_of_source_string: int,
   model="text-embedding-ada-002",
) -> list[int]:
   """Return nearest neighbors of a given string."""

   # get embeddings for all strings
   embeddings = [get_embedding(string, model=model) for string in strings]

   # get the embedding of the source string
   query_embedding = embeddings[index_of_source_string]

   # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
   distances = distances_from_embeddings(query_embedding, embeddings, distance_metric="cosine")

   # get indices of nearest neighbors (function from embeddings_utils.py)
   indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)
   return indices_of_nearest_neighbors

# get recommendations for the first string
indices = recommendations_from_strings(
   strings=[text1, text2, text3, text4, text5, text6],
   index_of_source_string=0,
   model=EMBEDDING_MODEL,
)

print(indices)