#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const completedTasksByUserId = {};

  body.forEach(task => {
    if (task.completed) {
      const userId = task.userId;
      completedTasksByUserId[userId] = (completedTasksByUserId[userId] || 0) + 1;
    }
  });

  Object.entries(completedTasksByUserId).forEach(([userId, count]) => {
    console.log(`User ${userId} has completed ${count} task${count !== 1 ? 's' : ''}.`);
  });
});
