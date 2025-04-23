import ReadLine from 'readline';


const rl = ReadLine.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question('cual es la longitud : ', (inp: string): any => { // ten en cuenta que inp es un string
  let l = parseFloat(inp)
  const area = 2 * (3 ** 0.5) * (l ** 2)
  const v = (2 / 3) * (l ** 3)
  console.log(`Area: ${area}`)
  console.log(`Volumen: ${v}`)
  rl.close()
})