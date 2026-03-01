// Game state
let gameState = {
    board: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    winner: null,
    gameOver: false
};
let moveCount = 0;

// DOM Elements
const gameBoard = document.getElementById('gameBoard');
const cells = document.querySelectorAll('.cell');
const statusText = document.getElementById('statusText');
const resetBtn = document.getElementById('resetBtn');
const infoBtn = document.getElementById('infoBtn');
const moveCounter = document.getElementById('moveCount');
const infoModal = document.getElementById('infoModal');
const closeModal = document.getElementById('closeModal');

// Initialize game
document.addEventListener('DOMContentLoaded', () => {
    loadGameState();
    cells.forEach(cell => {
        cell.addEventListener('click', handleCellClick);
    });
    resetBtn.addEventListener('click', resetGame);
    infoBtn.addEventListener('click', openModal);
    closeModal.addEventListener('click', closeInfoModal);
    window.addEventListener('click', (event) => {
        if (event.target === infoModal) closeInfoModal();
    });
});

async function loadGameState() {
    try {
        const response = await fetch('/api/game/state');
        const data = await response.json();
        gameState = data;
        renderBoard();
        updateStatus();
    } catch (error) {
        console.error('Error loading game state:', error);
    }
}

function renderBoard() {
    cells.forEach((cell, index) => {
        const value = gameState.board[index];
        cell.textContent = '';
        cell.classList.remove('x', 'o', 'disabled');
        
        if (value === 1) {
            cell.textContent = 'X';
            cell.classList.add('x');
        } else if (value === 2) {
            cell.textContent = 'O';
            cell.classList.add('o');
        }

        if (gameState.gameOver || value !== 0) {
            cell.classList.add('disabled');
        }
    });
}

function updateStatus() {
    if (gameState.gameOver) {
        if (gameState.winner === 'player') {
            statusText.textContent = '🎉 You Won! Congratulations!';
            statusText.style.color = '#4CAF50';
            gameBoard.classList.add('winner-animation');
        } else if (gameState.winner === 'ai') {
            statusText.textContent = '🤖 AI Wins! Better luck next time!';
            statusText.style.color = '#FF6B6B';
        } else if (gameState.winner === 'draw') {
            statusText.textContent = "🤝 It's a Draw!";
            statusText.style.color = '#FFD700';
        }
    } else {
        statusText.textContent = '👤 Your turn - Click a cell';
        statusText.style.color = 'white';
    }
    moveCounter.textContent = moveCount;
}

async function handleCellClick(event) {
    if (gameState.gameOver) return;

    const cell = event.target;
    const index = parseInt(cell.dataset.index);

    if (gameState.board[index] !== 0) return;

    try {
        statusText.textContent = '⏳ AI is thinking...';
        cells.forEach(c => c.classList.add('disabled'));

        const response = await fetch('/api/game/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ position: index })
        });

        if (!response.ok) {
            statusText.textContent = '❌ Invalid move! Try another cell.';
            cells.forEach(c => {
                if (gameState.board[parseInt(c.dataset.index)] === 0) {
                    c.classList.remove('disabled');
                }
            });
            return;
        }

        const data = await response.json();
        gameState = data;
        moveCount += 2; // Player + AI move

        renderBoard();
        updateStatus();

        // Re-enable cells if game is not over
        if (!gameState.gameOver) {
            cells.forEach(c => {
                if (gameState.board[parseInt(c.dataset.index)] === 0) {
                    c.classList.remove('disabled');
                }
            });
            statusText.textContent = '👤 Your turn - Click a cell';
        }
    } catch (error) {
        console.error('Error making move:', error);
        statusText.textContent = '❌ Error! Please try again.';
        cells.forEach(c => {
            if (gameState.board[parseInt(c.dataset.index)] === 0) {
                c.classList.remove('disabled');
            }
        });
    }
}

async function resetGame() {
    try {
        const response = await fetch('/api/game/reset', {
            method: 'POST'
        });
        const data = await response.json();
        gameState = data;
        moveCount = 0;
        gameBoard.classList.remove('winner-animation');
        renderBoard();
        updateStatus();
    } catch (error) {
        console.error('Error resetting game:', error);
    }
}

function openModal() {
    infoModal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeInfoModal() {
    infoModal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

// Handle Escape key to close modal
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && infoModal.style.display === 'block') {
        closeInfoModal();
    }
});
