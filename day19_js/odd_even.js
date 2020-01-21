function oddOrEven(array) {
  if (array.length === 0) {
    return 'even'
  }
  const sum = array.reduce((total, amount) => {
    return total + amount;
  })
  if ((sum % 2 == 1) || (sum % 2 == -1)) {
    return 'odd'
  } else {
    return 'even'
  }
}

function oddOrEven(arr) {
  return arr.reduce((a, b) => a + b, 0) % 2 ? 'odd' : 'even';
}
