"""
Web-based Tic-Tac-Toe Game with AI Strategy Bot
Flask backend with Minimax algorithm
"""

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [0] * 9  # 0: empty, 1: player (X), 2: AI (O)
        self.human = 1
        self.ai = 2
    
    def is_winner(self, player):
        """Check if the specified player has won"""
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]               # diagonals
        ]
        for combo in winning_combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def is_board_full(self):
        """Check if board is full"""
        return all(spot != 0 for spot in self.board)
    
    def get_empty_cells(self):
        """Return list of empty cell positions"""
        return [i for i in range(9) if self.board[i] == 0]
    
    def minimax(self, depth, is_maximizing):
        """Minimax algorithm for optimal AI play"""
        if self.is_winner(self.ai):
            return 10 - depth
        if self.is_winner(self.human):
            return depth - 10
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for cell in self.get_empty_cells():
                self.board[cell] = self.ai
                score = self.minimax(depth + 1, False)
                self.board[cell] = 0
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for cell in self.get_empty_cells():
                self.board[cell] = self.human
                score = self.minimax(depth + 1, True)
                self.board[cell] = 0
                best_score = min(score, best_score)
            return best_score
    
    def ai_move(self):
        """Find the best move for AI using minimax"""
        best_score = float('-inf')
        best_move = None
        
        for cell in self.get_empty_cells():
            self.board[cell] = self.ai
            score = self.minimax(0, False)
            self.board[cell] = 0
            
            if score > best_score:
                best_score = score
                best_move = cell
        
        return best_move
    
    def player_move(self, position):
        """Place player move"""
        if position < 0 or position > 8:
            return False
        if self.board[position] != 0:
            return False
        self.board[position] = self.human
        return True
    
    def get_game_state(self):
        """Return current game state"""
        winner = None
        game_over = False
        
        if self.is_winner(self.human):
            winner = "player"
            game_over = True
        elif self.is_winner(self.ai):
            winner = "ai"
            game_over = True
        elif self.is_board_full():
            winner = "draw"
            game_over = True
        
        return {
            "board": self.board,
            "winner": winner,
            "gameOver": game_over
        }

# Store game instance
game = TicTacToe()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/game/state', methods=['GET'])
def get_game_state():
    """Get current game state"""
    return jsonify(game.get_game_state())

@app.route('/api/game/move', methods=['POST'])
def make_move():
    """Handle player move and AI response"""
    data = request.json
    position = data.get('position')
    
    # Validate and make player move
    if not game.player_move(position):
        return jsonify({"error": "Invalid move"}), 400
    
    state = game.get_game_state()
    
    # If game is over, return state
    if state['gameOver']:
        return jsonify(state)
    
    # AI makes its move
    ai_position = game.ai_move()
    if ai_position is not None:
        game.board[ai_position] = game.ai
    
    state = game.get_game_state()
    return jsonify(state)

@app.route('/api/game/reset', methods=['POST'])
def reset_game():
    """Reset the game"""
    global game
    game = TicTacToe()
    return jsonify(game.get_game_state())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
