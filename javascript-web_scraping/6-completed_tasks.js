#!/usr/bin/node

const request = require('request');

const todoAPIurl = process.argv[2];

request(todoAPIurl, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    const parsedTasks = JSON.parse(res.body);
    const userAndTask = {};

    for (const obj in parsedTasks) {
      if (parsedTasks[obj].completed === true) { // entering 'completed' key in current task object
        if (!userAndTask[parsedTasks[obj].userId]) {
          userAndTask[parsedTasks[obj].userId] = 1; // assign value 1 if key does not yet exist in the object (using the current userId number as key number)
        } else {
          userAndTask[parsedTasks[obj].userId] += 1; // increment the value by 1 if it exists
        }
      }
    }
    console.log(userAndTask);
  }
});

//  if (taskObj.userId === userCounter) { // if the current object's user id property equals the defined counter
//    if (taskObj.completed === true) { // inside the same userid previously checked, check the completed property
//      completedTasks += 1;
//    }
//  } else {
//    userAndTask[userCounter] = completedTasks; // store values counted from the current userId
//    userCounter += 1; // increment the defined counter to continue to the next user
//    completedTasks = 0; // reset the completed task for the next
//  }
