import readline from 'node:readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})


console.log('================================================================')
rl.question('Entrada de a : ', (a) => {
  rl.question('Entrada de b : ', (b) => {
    rl.question('Entrada de h : ', (h) => {
      let A = parseFloat(a);
      let B = parseFloat(b);
      let H = parseFloat(h);
      let x = (((A * A) * B) / 2) * H
      console.log(`El resultado es ${x}`)
      console.log('================================================================')
      rl.question('pedro nota 1 : ', (pedroNota1) => {
        rl.question('predro nota 2 : ', (pedroNota2) => {
          let notaPedro = (parseFloat(pedroNota1) * 0.30) + (parseFloat(pedroNota2) * 0.70)
          console.log(`la nota de pedro es : ${notaPedro}`)
          rl.question('paublo nota 1 : ', (paubloNota1) => {
            rl.question('paublo nota 2 : ', (paubloNota2) => {
              let notaPaublo = (parseFloat(paubloNota1) * 0.30) + (parseFloat(paubloNota2) * 0.70)
              console.log(`la nota de paublo es : ${notaPaublo}`)
              rl.question('beti nota 1 :', (betiNota1) => {
                rl.question('beti nota 2 : ', (betiNota2) => {
                  let notaBeti = (parseFloat(betiNota1) * 0.30) + (parseFloat(betiNota2) * 0.70)
                  console.log(`la nota de beti es : ${notaBeti}`)
                  rl.question('banban nota 1 : ', (banbanNota1) => {
                    rl.question('banban nota 2 : ', (banbanNota2) => {
                      let notaBanban = (parseFloat(banbanNota1) * 0.30) + (parseFloat(banbanNota2) * 0.70)
                      console.log(`la nota de banban es : ${notaBanban}`)
                      rl.close()
                    })
                  })
                })
              })
            })
          })
        })
      })
    })
  })
})

