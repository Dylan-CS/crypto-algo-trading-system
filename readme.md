# Crypto Quant Trading System

## Overview

A sophisticated cryptocurrency trading platform that combines LSTM-based deep learning with automated trading execution. The system leverages FastAPI for its microservice architecture and Nacos for service discovery, making it both scalable and maintainable.

## project structure
```
crypto-quant-trading-system/
   ├── src/
   │   ├── api/                 # API Layer
   │   │   ├── endpoints/       # API Endpoints
   │   │   └── routes/          # Route Definitions
   │   │
   │   ├── core/                # Core Functionality
   │   │   ├── config/          # Configuration Management
   │   │   ├── events/          # Event Handling
   │   │   └── utils/           # Utility Functions
   │   │
   │   ├── data/                # Data Layer
   │   │   ├── collectors/      # Data Collectors
   │   │   ├── processors/      # Data Processors  
   │   │   └── storage/         # Data Storage
   │   │
   │   ├── models/              # Model Layer
   │   │   ├── evaluation/      # Model Evaluation
   │   │   └── lstm/            # LSTM Models
   │   │
   │   ├── services/            # Services Layer
   │   │   ├── monitoring/      # Monitoring Services
   │   │   └── nacos/           # Service Registration
   │   │
   │   └── trading/             # Trading Layer
   │       ├── execution/       # Trade Execution
   │       ├── risk/            # Risk Management
   │       └── strategy/        # Trading Strategies
   │       └── newsbot.py       # New addition
   │
   ├── tests/                   # Tests Directory
   ├── docs/                    # Documentation
   └── scripts/                 # Deployment Scripts
```

## Key Features

### Machine Learning Components
- **LSTM Price Prediction**: Advanced neural network architecture with:
  - Multi-layer LSTM implementation (4 layers with 50 units each)
  - Dropout layers (0.2) for preventing overfitting
  - Optimized for time-series prediction of cryptocurrency prices

### System Architecture
- **FastAPI Backend**: High-performance asynchronous API
- **Nacos Integration**: Service discovery and dynamic configuration management
- **Scheduled Tasks**: Automated health checks and service registration
- **Modular Design**: Separated concerns for trading, prediction, and system management

### Trading Features
- **Real-time Data Processing**: 
  - Websocket integration for real-time market data
  - Custom data normalization pipeline
  - Multi-exchange data aggregation
- **Risk Management**: 
  - Position sizing algorithms
  - Stop-loss automation
  - Volatility-based risk adjustment
  - Maximum drawdown controls
- **Automated Trading**: 
  - Multi-exchange API support
  - Custom order types
  - Smart order routing
  - Order splitting algorithms
- **Performance Monitoring**: 
  - Real-time P&L tracking
  - Risk metrics dashboard
  - Performance attribution analysis
  - Trading journal automation

### Newsbot Integration
- **Deepseek API**: Integration of Deepseek API for enhanced data collection.
- **Google Search API**: A new package will be developed to integrate Google Search API, aimed at creating a newsbot.
- **Event-Driven Data Pipeline**: The system will utilize an event-driven data pipeline for mid to low-frequency algorithmic trading, incorporating data pipeline, simple strategy code, newsbot, and pricing model.

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

