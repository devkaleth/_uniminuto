import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let x = 0;

function preguntarEdad() {
  if (x > 10) {
    rl.close();
    return;
  }

  rl.question('¿Cuál es tu edad?: ', (edad: string) => {
    const edadNum = parseInt(edad);
    if (edadNum >= 18) {
      console.log('Eres mayor de edad');
    } else {
      console.log('Eres menor de edad');
    }

    x++;
    preguntarEdad(); // llamada recursiva
  });
}

preguntarEdad();
