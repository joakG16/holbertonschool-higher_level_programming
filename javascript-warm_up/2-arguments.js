#!/usr/bin/node

require('process');

if (process.argv.length === 1) { // argu. starts from 1, not 0
    console.log('No argument');
} else if (process.argv.length === 2) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
