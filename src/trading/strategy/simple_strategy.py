class NewsSentimentStrategy:
    def __init__(self, newsbot: NewsBot, pipeline: MarketDataPipeline):
        self.newsbot = newsbot
        self.pipeline = pipeline
        self.sentiment_threshold = 0.8
        
    async def execute(self):
        market_sentiment = await self.newsbot.get_market_sentiment('BTC')
        if abs(market_sentiment['average_sentiment']) > self.sentiment_threshold:
            signal = {
                'action': 'BUY' if market_sentiment['average_sentiment'] > 0 else 'SELL',
                'confidence': abs(market_sentiment['average_sentiment']),
                'timestamp': datetime.now().isoformat()
            }
            await self.pipeline.publish_event(EventType.TRADING_SIGNAL.value, signal)