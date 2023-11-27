//Problem 2
// You have 6 x 6 game board where each cell is shown as a *
// This is a two player dice game. The die has numbers 1 to 6.
// Each player rolls the dice twice. First roll is row number, second roll is col number.
// After the player rolls the dice, in the (row,col) enter the player's initial. 
// If the player  A rolls the dice and  if  player B already has their initial in the same row,col
// add a point to A and change the initial to A. 


function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
  }
  
  function playGame() {
    // 6*6 game board - all elements set to "*"
    const board = Array.from({ length: 6 }, () => Array(6).fill('*'));
    let currentPlayer = 'A'; // Starting with A
    let playerA = 0; //points
    let playerB = 0; 
    
    while (playerA < 5 && playerB < 5) {
      // to get array matching value , subtracting 1
      const row = rollDice() - 1;
      const col = rollDice() - 1;
  
      // checing if empty (ie) - "*"
      if (board[row][col] === '*') {
        // If empty, place current player's initial there
        board[row][col] = currentPlayer;
      } else if (board[row][col] === 'B' && currentPlayer === 'A') {
        // If B is already present , A earns a point
        playerA++;
        board[row][col] = 'A';
      } else if (board[row][col] === 'A' && currentPlayer === 'B') {
        // If A is already present , B earns a point
        playerB++;
        board[row][col] = 'B';
      }
  
      // Switch players
      currentPlayer = currentPlayer === 'A' ? 'B' : 'A';
    }
  
    // results
    const winner = playerA === 5 ? 'Player A' : 'Player B';
    console.log(`${winner} wins the game!`);
  }
  
  playGame();
  