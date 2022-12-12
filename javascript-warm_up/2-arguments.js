#!/usr/bin/node

require('process');

if (process.argv[3]) {
    console.log('Arguments found');
} else if (process.argv[2]) {
    console.log('Argument found');
} else {
    console.log('No argument');
}
