# 🎮 Tic-Tac-Toe AI Bot - Web Version

A beautiful, interactive Tic-Tac-Toe game with an unbeatable AI opponent powered by the Minimax algorithm.

## 📋 Features

✨ **Modern Web Interface**
- Beautiful gradient UI with smooth animations
- Interactive game board with hover effects
- Real-time game status updates
- Responsive design (works on desktop and mobile)

🧠 **Unbeatable AI**
- Minimax algorithm for optimal play
- Never loses (always wins or draws)
- Evaluates all possible game states
- Intelligent move prioritization

🎯 **Complete Gameplay**
- Player vs AI matches
- Game state management
- Win/Draw detection
- Move counter
- New Game button
- Instructions modal

## 📁 Project Structure

```
├── app.py                 # Flask backend (Minimax AI)
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Game UI
└── static/
    ├── style.css         # Game styling
    └── script.js         # Game interactions
```

## 🚀 How to Run

### Prerequisites
- Python 3.7+
- Flask (will be installed via requirements.txt)

### Installation & Launch

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   python app.py
   ```

3. **Open in browser:**
   ```
   http://localhost:5000
   ```

4. **Start Playing!**
   - Click any empty cell to place your X
   - AI automatically responds with its O
   - Win by getting 3 in a row (horizontal, vertical, or diagonal)

## 🎮 How to Play

- **You are X** (green badge)
- **AI is O** (red badge)
- Click on any empty cell to make your move
- The AI will instantly respond with its move
- Get three marks in a row to win
- The AI uses Minimax - it plays perfectly!

## 🤖 AI Algorithm

**Minimax with Depth Scoring:**
- Evaluates all possible game outcomes
- Finds the optimal move for AI
- Never makes a losing move
- Prefers quicker wins and slower losses
- Unbeatable in perfect play

### Scoring System:
- **Win**: +10 (minus depth for quick wins)
- **Loss**: -10 (plus depth for delayed losses)
- **Draw**: 0

## 📊 Game Statistics

The interface displays:
- **Moves**: Total moves played
- **Algorithm**: Minimax (optimal strategy)
- **Difficulty**: Unbeatable

## 🎨 UI Components

- **Game Board**: 3x3 interactive grid
- **Status Display**: Real-time game state
- **Control Buttons**: New Game, Instructions
- **Game Info**: Player vs AI indicators
- **Statistics**: Game metrics

## 🔧 API Endpoints

- `GET /` - Serve the game interface
- `GET /api/game/state` - Get current board state
- `POST /api/game/move` - Make a player move + AI response
- `POST /api/game/reset` - Reset the game

## 📱 Responsive Design

The game works perfectly on:
- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Tablets
- Mobile phones

## 🎓 Learning Resources

This project demonstrates:
- Flask web framework
- Minimax algorithm implementation
- Game theory
- RESTful API design
- Interactive JavaScript
- Responsive CSS design

## 💡 Tips for Playing

1. **Opening**: Try taking the center (position 5) for advantage
2. **Corners**: Corners are strategic positions
3. **Block**: Try to block AI's winning moves
4. **Study**: Watch the AI's strategy - it's playing optimally!

## 📝 Files Explanation

**app.py**
- Flask server setup
- TicTacToe game logic class
- Minimax algorithm
- API endpoints for game moves

**index.html**
- Game board grid
- Player/AI info sections
- Status display
- Control buttons
- Instructions modal

**style.css**
- Modern gradient design
- Smooth animations
- Responsive layout
- Hover effects
- Modal styling

**script.js**
- Game state management
- API communication
- DOM updates
- User interactions
- Event handlers

## ⚙️ Customization

To modify difficulty or behavior:

1. **Change port** in `app.py`:
   ```python
   app.run(debug=True, port=5001)  # Change 5000 to 5001
   ```

2. **Disable debug mode** for production:
   ```python
   app.run(debug=False, port=5000)
   ```

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Change the port number in app.py or kill the process using port 5000
```

**Flask not found:**
```bash
pip install Flask==2.3.0
```

**Page won't load:**
- Check if server is running (you should see "Running on http://localhost:5000")
- Clear browser cache
- Try a different browser

## 📄 License

Free to use and modify!

## 👨‍💻 Author

Built as a demonstration of game AI and web development concepts.

---

**Enjoy playing against the unbeatable AI! 🎮**
