import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
	  if (err) {
		  console.error(err);
	  } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

async function displaySchoolValue(schoolName) {
  console.log(await getAsync(schoolName));
}


(async () => {
  await displaySchoolValue('ALX');
  setNewSchool('ALXSanFrancisco', '100');
  await displaySchoolValue('ALXSanFrancisco');
})();


