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

## Development Setup

### Prerequisites
- Python 3.7+
- Docker & Docker Compose
- MongoDB
- Redis (for caching)
- CUDA-compatible GPU (recommended for model training)

### Quick Start

1. **Clone & Setup**
```bash
git clone https://github.com/yourusername/crypto-quant-trading-system.git
cd crypto-quant-trading-system
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

2. **Configuration**
- Copy `.env.example` to `.env` and configure environment variables
- Update service configurations in `src/core/config.py`
- Configure exchange API keys in `config/exchanges.yaml`

3. **Launch Services**
```bash
docker-compose up -d  # Start infrastructure services
python src/main.py    # Launch main application
```

## System Configuration

### Service Discovery
- **Nacos Configuration**
  - Server: `localhost:8848` (default)
  - Namespace: `crypto-trading`
  - Authentication: JWT-based

### Model Parameters
- **LSTM Configuration** (`src/models/lstm/config.py`)
  ```python
  SEQUENCE_LENGTH = 60
  LSTM_UNITS = [50, 50, 50, 50]
  DROPOUT_RATE = 0.2
  OPTIMIZER = 'adam'
  LOSS = 'mse'
  ```

### LLM & Search API Configuration
- **Deepseek Configuration** (`src/services/newsbot/llm/config.py`)
  ```python
  DEEPSEEK_API_KEY = "your_api_key"
  DEEPSEEK_MODEL = "deepseek-chat-v3"
  MAX_TOKENS = 2048
  TEMPERATURE = 0.7
  TOP_P = 0.95
  CONTEXT_WINDOW = 16384  # Maximum context length
  ```

- **Google Search API** (`src/services/newsbot/config.py`)
  ```python
  GOOGLE_API_KEY = "your_api_key"
  GOOGLE_CSE_ID = "your_custom_search_engine_id"
  SEARCH_QUOTA_PER_DAY = 10000
  MAX_RESULTS_PER_QUERY = 10
  REGION = "US"  # Search region
  ```

### Development Workflow
1. Fork the repository
2. Create feature branch (`git checkout -b feature/xyz`)
3. Commit changes (`git commit -m 'Add feature xyz'`)
4. Push to branch (`git push origin feature/xyz`)
5. Submit Pull Request

### Code Standards
- Follow PEP 8 style guide
- Maintain test coverage >80%
- Document all public APIs
- Add type hints to new code

### Contact
- https://www.linkedin.com/in/dylan-chen-684a52249/

## License
MIT License - See LICENSE file for details


