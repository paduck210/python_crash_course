// function solution(string) {
//     const letterList = [];
//     string.split("").forEach(letter => {
//         if (letter == letter.toUpperCase()) {
//             letterList.push(` ${letter}`);
//         } else {
//             letterList.push(letter)
//         }
//     })
//     return letterList.join("")
// }
//
//
// function solution(string) {
//     return(string.replace(/([A-Z])/g, ' $1'));
//
// }

const targetStr = "$ivagrs1]@{naywj+1ds\\o9rw";
const regexr = /[A-Za-z]+/g;
console.log(targetStr.match(regexr)); // [ 'AA', 'BB', 'Aa', 'Bb' ]
