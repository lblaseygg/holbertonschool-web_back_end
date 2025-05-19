/**
 * Function that displays a message on the standard output
 * @param {string} message - The message to display
 * @return {void}
 */
const displayMessage = (message) => {
    process.stdout.write(message + '\n');
  };
  
  module.exports = displayMessage;