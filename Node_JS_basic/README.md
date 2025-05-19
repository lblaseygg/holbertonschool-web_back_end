# Node.js Basics Project

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Run JavaScript using Node.js
- Use Node.js modules
- Use specific Node.js modules to read files
- Use `process` to access command line arguments and the environment
- Create a small HTTP server using Node.js
- Create a small HTTP server using Express.js
- Create advanced routes with Express.js
- Use ES6 with Node.js using Babel-node
- Use Nodemon to develop faster

## Requirements

- **Allowed editors:** vi, vim, emacs, Visual Studio Code
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Node.js (version 20.x.x)
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest and the command `npm run test`
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project by running `npm run full-test`
- All of your functions/classes must be exported using this format: `module.exports = myFunction;`

## Getting Started

1. Clone the repository.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run tests:
   ```bash
   npm run test
   ```
4. Run linting:
   ```bash
   npm run lint
   ```
5. Run full tests (tests and linting):
   ```bash
   npm run full-test
   ```

## Project Structure

- `index.js`: Main entry point for the application.
- `server.js`: HTTP server implementation using Node.js or Express.js.
- `database.csv`: Sample data file for reading operations.
- `package.json`: Project configuration and dependencies.
- `.eslintrc.js`: ESLint configuration.
- `babel.config.js`: Babel configuration for ES6 support.

## Additional Notes

- Ensure all functions and classes are exported using `module.exports`.
- Use Nodemon for faster development by running:
  ```bash
  npm run dev
  ```

## License

This project is licensed under the ISC License.