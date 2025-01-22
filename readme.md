# Crypto Algo Trading System

## Overview

A high-performance cryptocurrency trading system that combines AI-driven analysis with automated execution. Built on a microservice architecture, it features LSTM neural networks for price prediction, real-time market data processing, and advanced risk management capabilities. The platform supports multiple exchanges and includes LLM-powered news sentiment analysis for comprehensive market insights.

## Project Structure
```
crypto-quant-trading-system/
   ├── src/
   │   ├── api/                      # API Layer
   │   │   ├── endpoints/            # API Endpoints
   │   │   ├── routes/               # Route Definitions
   │   │   └── websocket/            # WebSocket Handlers
   │   │
   │   ├── core/                     # Core Functionality
   │   │   ├── config/               # Configuration Management
   │   │   ├── events/               # Event Handling
   │   │   └── utils/                # Utility Functions
   │   │
   │   ├── data/                     # Data Layer
   │   │   ├── collectors/           # Data Collectors
   │   │   │   ├── market_data/      # Exchange Market Data
   │   │   │   └── news_data/        # News & Social Data
   │   │   ├── processors/           # Data Processors
   │   │   └── storage/              # Data Storage
   │   │
   │   ├── models/                   # Model Layer
   │   │   ├── evaluation/           # Model Evaluation
   │   │   ├── lstm/                 # LSTM Price Models
   │   │   └── sentiment/            # Sentiment Models
   │   │
   │   ├── services/                 # Services Layer
   │   │   ├── monitoring/           # Monitoring Services
   │   │   ├── nacos/                # Service Registration
   │   │   └── newsbot/              # News Analysis Service
   │   │       ├── llm/              # LLM Integration
   │   │       ├── sentiment/        # Sentiment Analysis
   │   │       └── signals/          # Trading Signal Generation
   │   │
   │   └── trading/                  # Trading Layer
   │       ├── execution/            # Trade Execution
   │       │   ├── order_router/     # Smart Order Routing
   │       │   └── position/         # Position Management
   │       ├── risk/                 # Risk Management
   │       │   ├── limits/           # Trading Limits
   │       │   └── metrics/          # Risk Metrics
   │       └── strategy/             # Trading Strategies
   │           ├── arbitrage/        # Arbitrage Strategies
   │           ├── mean_reversion/   # Mean Reversion
   │           └── trend/            # Trend Following
   │
   ├── tests/                        # Tests Directory
   │   ├── unit/                     # Unit Tests
   │   └── integration/              # Integration Tests
   ├── docs/                         # Documentation
   └── scripts/                      # Deployment Scripts
```

## Key Features

### 1. Event-Driven Data Pipeline
- **Data Integration Layer**:
  - Real-time market data websocket streams
  - Custom data normalization and preprocessing
  - Multi-exchange data aggregation
- **Event Processing**:
  - Event-driven architecture for real-time data handling
  - Message queue integration for event distribution
  - Scalable event processing framework

### 2. Trading System
- **Mid-Low Frequency Trading**:
  - Statistical arbitrage strategies
  - Mean reversion models
  - Trend following implementations
- **Risk Management**: 
  - Position sizing algorithms
  - Stop-loss automation
  - Volatility-based risk adjustment
  - Maximum drawdown controls
- **Order Management**:
  - Smart order routing
  - Order splitting algorithms
  - Multi-exchange execution

### 3. Price Engine
- **LSTM Price Prediction**: 
  - Multi-layer LSTM implementation (4 layers with 50 units each)
  - Dropout layers (0.2) for preventing overfitting
  - Time-series prediction optimization
- **Traditional Pricing Models**:
  - Black-Scholes model implementation
  - Volatility surface calibration
  - Greeks calculation and risk metrics

### 4. Newsbot Intelligence
- **LLM Integration**:
  - Deepseek API implementation for market analysis
  - Custom prompt engineering for financial context
- **Information Gathering**:
  - Google Search API integration
  - Real-time news aggregation
  - Sentiment analysis pipeline
- **Trading Signal Generation**:
  - News-based event detection
  - Sentiment-driven trading signals
  - Market impact analysis

## Getting Started

### Prerequisites
- Python 3.7+
- Docker & Docker Compose
- MongoDB
- Redis (for caching)
- GPU support (optional, for faster model training)

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/crypto-quant-trading-system.git
cd crypto-quant-trading-system
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

## Configuration

1. **Nacos Setup**
   - Configure Nacos server settings in `src/data/nacos_client.py`
   - Default Nacos server port: 8848
   - Set up namespace and authentication if required

2. **LSTM Model Configuration**
   - Model parameters can be adjusted in `src/trading/bitcoin_lstm.py`
   - Default configuration:
     - Sequence length: 60 time steps
     - 4 LSTM layers with dropout
     - Adam optimizer with MSE loss

3. **API Settings**
   - Update FastAPI configurations in `src/core/config.py`
   - Default API port: 8000

## Usage

1. **Start the Service**
```bash
python src/main.py
```

2. **Access API Documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

3. **Monitor Trading Performance**
   - Access monitoring endpoints through the API
   - Check service health at `/health`
   - View predictions at `/predictions`

## Architecture

The system follows a microservice architecture with the following components:

```
src/
├── api/           # API endpoints and dependencies
├── core/          # Core configurations and events
├── data/          # Data handling and Nacos client
└── trading/       # LSTM model and trading logic
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions and support, please contact:
- Project Maintainer: your-email@example.com
- Issue Tracker: GitHub Issues

## Acknowledgments

- TensorFlow team for LSTM implementation
- FastAPI framework developers
- Nacos team for service discovery

## Support & Community
- Discord Channel: [Link]
- Documentation Wiki: [Link]
- Community Forums: [Link]
- Regular Webinars: [Schedule]

