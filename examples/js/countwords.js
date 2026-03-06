function count_word(text) {
  let count = 0
  let in_whitespace = true

  for (let char of text) {
    if (char == " " || char == "\n") {
      in_whitespace = true
    } else if (in_whitespace) {
      count += 1
      in_whitespace = false
    }
  }

  return count
}

console.assert(count_word("Hello world") == 2)
console.assert(count_word("   extra   spaces   ") == 2)
console.assert(count_word("") == 0)
