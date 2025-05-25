const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(process.argv[2])
      .then((fields) => {
        res.status(200).send(`This is the list of our students\nNumber of students: ${Object.values(fields).reduce((acc, curr) => acc + curr.length, 0)}\n${Object.entries(fields).map(([field, names]) => `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`).join('\n')}`);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    readDatabase(process.argv[2])
      .then((fields) => {
        res.status(200).send(`List: ${fields[major].join(', ')}`);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }
}

module.exports = StudentsController; 