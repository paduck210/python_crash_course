function order(words) {
  const dict = {}
  words.split(" ").forEach((word)=> {
    word.split("").forEach((letter)=> {
      if ("123456789".includes(letter)) { dict[letter] = word; }
    })
  })
  return(Object.values(dict).join(" "));
}

// function order(words) {
//   return words.split(' ').sort(function (a, b) {
//     return a.match(/\d/) - b.match(/\d/);
//   }).join(' ');
// }

console.log(order("is2 Thi1s T4est 3a")) //, "Thi1s is2 3a T4est")
console.log(order("4of Fo1r pe6ople g3ood th5e the2")) // "Fo1r the2 g3ood 4of th5e pe6ople")
console.log(order(""))
