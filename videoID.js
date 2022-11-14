import data from './play.json' assert {type: 'json'};

//get the keys of the data
const songs = Object.keys(data);

//select one random song from the array
const input = songs[Math.floor(Math.random() * songs.length)];
const randomSong = '<iframe width="400" height="300" src="https://www.youtube.com/embed/'+input+'?autoplay=1&controls=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

//add the song to the page
document.getElementById('song').innerHTML = randomSong;
