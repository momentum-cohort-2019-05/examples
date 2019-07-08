function pickRandomNumber (min, max) {
  const range = max - min + 1
  return Math.floor(Math.random() * range) + min
}

function getGuess (randomNumber) {
  let guess = window.prompt("What's your guess?")
  if (!guess) {
    return 'exit'
  }
  guess = parseInt(guess)
  if (guess === randomNumber) {
    window.alert('You got it!')
    return true
  } else if (guess < randomNumber) {
    window.alert('Too low!')
    return false
  } else {
    window.alert('Too high!')
    return false
  }
}

function startGame () {
  window.alert("Let's play a game! I've picked a random number between 1 and 100. Try to guess it.")
  const actualNumber = pickRandomNumber(1, 100)
  let guessed = false
  while (!guessed) {
    guessed = getGuess(actualNumber)
    if (guessed === 'exit') {
      break
    }
  }
}

startGame()
