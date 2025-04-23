import Readline from "readline"

const rl = Readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const n = 2
let i = 5

const Game = () => {

  if (i === 0) {
    rl.close()
    return
  }

  rl.question('escribe un numero : ', (number: string) => {
    const num = parseInt(number)
    try {
      if (num == n) {
        console.log('Ganaste :)')
        rl.close()
      } else {
        console.log('Perdiste :(')
        console.log('te quedan ' + i + ' intentos')
      }
    } catch (e) {
      console.log()
    }
    i--
    Game()
  })
}

Game()

