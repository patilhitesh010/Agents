"""
Tic-Tac-Toe Game with AI Strategy Bot
Uses Minimax algorithm for optimal AI play
"""

class TicTacToe:
    def __init__(self):
        self.board = [0] * 9  # 0: empty, 1: player (X), 2: AI (O)
        self.human = 1
        self.ai = 2
    
    def print_board(self):
        """Display the current board state"""
        print("\n")
        for i in range(3):
            row = "  "
            for j in range(3):
                spot = self.board[i*3+j]
                if spot == 0:
                    row += str(i*3+j+1)  # Show position number
                elif spot == 1:
                    row += "X"
                else:
                    row += "O"
                if j < 2:
                    row += " | "
            print(row)
            if i < 2:
                print("  ---------")
        print("\n")
    
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
        """
        Minimax algorithm for optimal AI play
        Returns the best score for the current board state
        """
        # Terminal states
        if self.is_winner(self.ai):
            return 10 - depth
        if self.is_winner(self.human):
            return depth - 10
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            # AI's turn - maximize score
            best_score = float('-inf')
            for cell in self.get_empty_cells():
                self.board[cell] = self.ai
                score = self.minimax(depth + 1, False)
                self.board[cell] = 0
                best_score = max(score, best_score)
            return best_score
        else:
            # Player's turn - minimize score
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
    
    def play_game(self):
        """Main game loop"""
        print("=" * 30)
        print("  WELCOME TO TIC-TAC-TOE BOT")
        print("=" * 30)
        print("\nYou are X, AI is O")
        print("Enter position (1-9) to place your mark:\n")
        
        self.print_board()
        
        while True:
            # Player's turn
            while True:
                try:
                    position = int(input("Your move (1-9): ")) - 1
                    if position < 0 or position > 8:
                        print("Invalid! Enter number 1-9")
                        continue
                    if self.board[position] != 0:
                        print("Position occupied! Choose another")
                        continue
                    self.board[position] = self.human
                    break
                except ValueError:
                    print("Invalid input! Enter a number 1-9")
            
            self.print_board()
            
            if self.is_winner(self.human):
                print("🎉 You won! Congratulations!")
                break
            
            if self.is_board_full():
                print("🤝 It's a draw!")
                break
            
            # AI's turn
            print("AI is thinking...")
            ai_position = self.ai_move()
            self.board[ai_position] = self.ai
            print(f"AI played at position {ai_position + 1}")
            
            self.print_board()
            
            if self.is_winner(self.ai):
                print("🤖 AI wins! Better luck next time!")
                break
            
            if self.is_board_full():
                print("🤝 It's a draw!")
                break


def main():
    """Run the game"""
    while True:
        game = TicTacToe()
        game.play_game()
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()