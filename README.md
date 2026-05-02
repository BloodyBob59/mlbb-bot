# Mobile Legends Autonomous Bot Documentation

## Features
- Automated gameplay for Mobile Legends
- In-game strategy suggestions based on current match state
- Enhanced performance through machine learning model training
- Customizable settings for user preferences
- Support for various game modes

## Setup Instructions
1. **Prerequisites**
   - Python 3.7 or higher
   - Required libraries: `tensorflow`, `numpy`, `opencv`, etc.
2. **Installation**
   - Clone the repository:
     ```bash
     git clone https://github.com/BloodyBob59/mlbb-bot.git
     ```
   - Navigate to the project folder:
     ```bash
     cd mlbb-bot
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Usage
- To run the bot, use the following command:
  ```bash
  python main.py
  ```
- Configure the settings in the `config.ini` file to suit your preferences.

## Architecture
- The bot uses a modular architecture:
  - **Input Module**: Captures game state via screen recognition.
  - **Processing Module**: Processes input and makes decisions using ML models.
  - **Output Module**: Sends commands to the game.

## How to Train Detection Models
1. **Collect Data**: Capture gameplay footage and extract frames using `data_collection.py`.
2. **Prepare Data**: Use the `data_preparation.py` script to format your data.
3. **Train**: Run the `train_model.py` script to train your model. Make sure to specify parameters such as learning rate and epochs in the config.
4. **Evaluate**: Test your model on new data to assess performance.
5. **Deploy**: Integrate the trained model back into the bot through the `model_integration.py` script.

## Contributing
- Pull requests are welcome! Please ensure to update tests as appropriate.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Special thanks to the Mobile Legends community for their support and resources!