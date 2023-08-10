const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const baseURL = 'https://swapi.dev/api';
const charactersEndpoint = `/films/${movieId}/`;

axios.get(`${baseURL}${charactersEndpoint}`)
  .then(response => {
    const characters = response.data.characters;
    return Promise.all(characters.map(characterUrl => axios.get(characterUrl)));
  })
  .then(characterResponses => {
    const characterNames = characterResponses.map(response => response.data.name);
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
