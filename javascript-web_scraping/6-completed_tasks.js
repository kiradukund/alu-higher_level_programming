#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  const todos = JSON.parse(body);
  const result = {};
  todos.filter(todo => todo.completed).forEach(todo => {
    result[todo.userId] = (result[todo.userId] || 0) + 1;
  });
  console.log(result);
});
