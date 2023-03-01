#!/usr/bin/env node
import {createClient} from 'redis';

// Create a Redis client
const client = createClient();

// Log a message when the client connects to Redis
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Log an error message when the client fails to connect to Redis
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
