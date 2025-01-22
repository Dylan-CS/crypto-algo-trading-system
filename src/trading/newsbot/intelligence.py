from typing import List, Dict
import google.generativeai as genai
from datetime import datetime

class NewsIntelligence:
    def __init__(self, config: Dict):
        self.llm_client = self._init_llm(config["llm_api_key"])
        self.sentiment_threshold = config["sentiment_threshold"]
        
    async def analyze_news(self, news: List[Dict]) -> Dict:
        sentiments = []
        for item in news:
            sentiment = await self._analyze_sentiment(item["content"])
            sentiments.append(sentiment)
            
        return {
            "average_sentiment": sum(sentiments) / len(sentiments),
            "signals": self._generate_signals(sentiments),
            "timestamp": datetime.now().isoformat()
        }
        
    async def _analyze_sentiment(self, text: str) -> float:
        response = await self.llm_client.generate_content_async(
            f"Analyze the sentiment of this text (return only a number between -1 and 1):\n{text}"
        )
        return float(response.text)
        
    def _generate_signals(self, sentiments: List[float]) -> List[Dict]:
        signals = []
        avg_sentiment = sum(sentiments) / len(sentiments)
        
        if abs(avg_sentiment) > self.sentiment_threshold:
            signals.append({
                "type": "STRONG_BUY" if avg_sentiment > 0 else "STRONG_SELL",
                "confidence": abs(avg_sentiment),
                "timestamp": datetime.now().isoformat()
            })
            
        return signals 