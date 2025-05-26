// Display welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\r\n');

// Set stdin encoding to handle text input
process.stdin.setEncoding('utf8');

// Handle data input from stdin
process.stdin.on('readable', function () {
  var chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write('Your name is: ' + chunk);
  }
});

// Handle stdin end event (when input stream is closed)
process.on('exit', function () {
  process.stdout.write('This important software is now closing\r\n');
});