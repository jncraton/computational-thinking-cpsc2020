function countWords(text) {
  let count = 0
  let inWhitespace = true

  for (let char of text) {
    if (char == ' ' || char == '\n') {
      inWhitespace = true
    } else if (inWhitespace) {
      count += 1
      inWhitespace = false
    }
  }

  return count
}

console.assert(countWords('Hello world') == 2)
console.assert(countWords('   extra   spaces   ') == 2)
console.assert(countWords('') == 0)
