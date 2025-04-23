import readLine from 'readline';

const rl = readLine.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('EL valor de a : ', (a) => {
  rl.question('El valor de b : ', (b) => {
    if (a != null && b != null) {
      let A = parseInt(a);
      let B = parseInt(b);
      let x = (A * B) + 2
      let z = B + 2
      console.log(`valor de x : ${x}`)
      console.log(`valor de z : ${z}`)
    } else {
      console.log('No se puede realizar la operacion')
    }
    rl.close()
  })
})


