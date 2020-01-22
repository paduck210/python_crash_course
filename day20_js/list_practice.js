function findSum(n) {
  const three = [...Array(n).keys()].map(x => ++x*3);
  const five = [...Array(n).keys()].map(x => ++x*5);
  const eight = three.concat(five).sort((a,b)=> {return a-b})
  console.log(eight)
}

findSum(10)


