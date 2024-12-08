import streamlit as st
import faiss
import numpy as np
import ollama
import requests

# Load FAISS index
index = faiss.read_index('hierarchical_vector_store.index')


# Load chunks from your dataset
def load_chunks(file_path):
    with open(file_path, 'r') as f:
        chunks = [line.strip() for line in f.readlines()]
    return chunks


chunks = load_chunks('chunks.txt')


# Function to get query embedding using Mistral
def get_query_embedding(query):
    result = ollama.embeddings(model='mistral', prompt=query)
    return result['embedding']


# Function to search the FAISS index (RAG system)
def search_rag(query_embedding, threshold=0.5):
    query_vector = np.array(query_embedding)#.reshape(1, -1)
    distances, indices = index.search(query_vector, k=3)  # Retrieve top 3 matches
    relevant_chunks = [chunks[i] for i in indices[0]]

    # Check if any result is within a relevance threshold (lower distance is better)
    if any(dist <= threshold for dist in distances[0]):
        return relevant_chunks, distances[0]
    return [], distances[0]  # If no relevant chunks found, return empty list


# Function to check relevance (based on distance or content)
def is_relevant(distances, threshold=0.5):
    return any(dist <= threshold for dist in distances)


# Function to answer directly using Mistral (for simple queries)
def direct_answer(query):
    response = ollama.generate(model='mistral', prompt=f"Answer this: {query}")
    return response['text']


# Function to fetch real-time data (internet search)
def fetch_from_internet(query):
    api_url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(api_url)
    data = response.json()
    return data.get('Abstract', "No relevant information found.")


# Function to combine and rephrase chunks using Mistral
def rephrase_answer(query, chunks):
    combined_text = ' '.join(chunks)
    prompt = f"Here is some information to help answer the query: {query}. Based on the information provided below, please summarize and provide the best possible answer.\n\n{combined_text}"
    rephrased_response = ollama.generate(model='mistral', prompt=prompt)
    return rephrased_response['text']


# Streamlit app for user interaction
st.title("Decision-Making Agent")

user_query = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_query:
        # Step 1: Get query embedding using Mistral
        query_embedding = get_query_embedding(user_query)

        # Step 2: Search the vector store (RAG system)
        relevant_chunks, distances = search_rag(query_embedding)

        # Step 3: Check if the vector store returns a relevant answer
        if is_relevant(distances):
            st.write("Relevant information found in the knowledge base.")
            st.write("Combining and rephrasing the best chunks...")
            answer = rephrase_answer(user_query, relevant_chunks)
            st.write("Best Answer:")
            st.write(answer)

        else:
            # Step 4: If not relevant, use Mistral to generate an answer
            st.write("No relevant information found in the vector store.")
            st.write("Attempting to answer using Mistral's knowledge...")
            mistral_answer = direct_answer(user_query)

            if mistral_answer.strip():  # If Mistral provides an answer
                st.write("Mistral Answer:")
                st.write(mistral_answer)
            else:
                # Step 5: If no relevant information from Mistral, search the internet
                st.write("No relevant information found in Mistral.")
                st.write("Fetching real-time information from the internet...")
                internet_answer = fetch_from_internet(user_query)
                st.write("Internet Search Answer:")
                st.write(internet_answer)

    else:
        st.warning("Please enter a question.")
