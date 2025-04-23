import readLine from 'readline';

const rl = readLine.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('nota 1 ', (n1) => {
  rl.question('nota 2 ', (n2) => {
    rl.question('nota 3', (n3) => {
      let nota1 = parseFloat(n1)
      let nota2 = parseFloat(n2)
      let nota3 = parseFloat(n3)
      let media = (nota1 + nota2 + nota3) / 3
      if (media >= 3.5) {
        console.log('Aprobado')
      }
      else {
        console.log('Reprobado')
      }
      rl.close()
    })
  })
})