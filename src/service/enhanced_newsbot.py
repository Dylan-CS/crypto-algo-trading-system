from openai import OpenAI
from googleapiclient.discovery import build
from FlagEmbedding import FlagModel
import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict
from datetime import datetime
from core.config import settings

class EnhancedNewsBot:
    def __init__(self):
        self.deepseek_client = OpenAI(
            api_key=settings.DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com"
        )
        
        self.google_service = build(
            "customsearch", 
            "v1", 
            developerKey=settings.GOOGLE_API_KEY
        )
        
        self.embedding_model = FlagModel(
            settings.BGE_MODEL_NAME, 
            use_fp16=True
        )
        
        self.chroma_client = chromadb.Client(
            settings.CHROMA_DB_PATH
        )
        self.collection = self._init_collection()
        
    def _init_collection(self):
        return self.chroma_client.create_collection(
            name="search_results",
            embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name=settings.BGE_MODEL_NAME
            )
        )
        
    async def search_news(self, query: str, num_results: int = 5) -> List[Dict]:
        try:
            res = self.google_service.cse().list(
                q=query,
                cx=settings.GOOGLE_CSE_ID,
                num=num_results,
                dateRestrict="d3"
            ).execute()
            
            search_results = res.get("items", [])
            await self._embed_and_index(search_results)
            return search_results
            
        except Exception as e:
            print(f"Error during Google search: {e}")
            return []
            
    async def _embed_and_index(self, search_results: List[Dict]):
        for idx, item in enumerate(search_results):
            text = f"{item['title']}: {item['snippet']}"
            embedding = self.embedding_model.encode(text)
            self.collection.add(
                documents=[text],
                embeddings=[embedding.tolist()],
                ids=[f"{datetime.now().timestamp()}_{idx}"]
            )
            
    async def analyze_sentiment(self, text: str) -> float:
        relevant_docs = await self._retrieve_relevant_documents(text)
        context = "\n\n".join(relevant_docs)
        
        response = await self.deepseek_client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Analyze the sentiment and return a score between -1 (negative) and 1 (positive)."},
                {"role": "user", "content": f"Text: {text}\n\nContext:\n{context}"},
            ]
        )
        
        return float(response.choices[0].message.content)
        
    async def _retrieve_relevant_documents(self, query: str, top_k: int = 3) -> List[str]:
        query_embedding = self.embedding_model.encode(query).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results["documents"][0] 