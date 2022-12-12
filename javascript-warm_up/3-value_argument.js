#!/usr/bin/node

if (process.argv[2]) { // This is an array containing the cmd. line arguments
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
