#!/usr/bin/node

const request = require('request');

const todoAPIurl = process.argv[2];

request(todoAPIurl, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    const parsedTasks = JSON.parse(res.body);

    let userCounter = 1;
    let completedTasks = 0;
    const userAndTask = {};

    for (const taskObj of parsedTasks) {
      if (taskObj.userId === userCounter) { // if the current object's user id property equals the defined counter
        if (taskObj.completed === true) { // inside the same userid previously checked, check the completed property
          completedTasks += 1;
        }
      } else {
        userAndTask[userCounter] = completedTasks; // store values counted from the current userId
        userCounter += 1; // increment the defined counter to continue to the next user
        completedTasks = 0; // reset the completed task for the next user
      }
    }
    console.log(userAndTask);
  }
});
