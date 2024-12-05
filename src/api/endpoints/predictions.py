from fastapi import APIRouter, HTTPException
from typing import Dict, List
import numpy as np
from src.trading.bitcoin_lstm import BitcoinLSTM

router = APIRouter()
model = BitcoinLSTM("data/bitcoin_prices.csv")

@router.get("/predictions", response_model=Dict)
async def get_predictions():
    try:
        # Load and preprocess data
        model.load_data()
        X, y = model.preprocess_data()
        
        # Build and train model if not already trained
        if model.model is None:
            model.build_model()
            model.train_model(X, y)
        
        # Make predictions
        predictions = model.predict(X[-60:])
        
        return {
            "status": "success",
            "predictions": predictions.tolist(),
            "timestamp": "latest"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
