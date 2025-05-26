// Display welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Set stdin encoding to handle text input
process.stdin.setEncoding('utf8');

// Handle data input from stdin
process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    // Remove newline character and display the name
    const name = chunk.toString().trim();
    process.stdout.write(`Your name is: ${name}\r`);
  }
});

// Handle stdin end event (when input stream is closed)
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});