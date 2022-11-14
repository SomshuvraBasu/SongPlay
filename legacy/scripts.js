//provide video_id
const songs = ['1f18irP--O8','2Ey4epZA27o','5L4ZLPKSVlY','TL3jqMCFKDc','Tt-mCnzPK-o','V-FdetrFMzw',
'jKMZZX2YMg0','gg9eX9MzLxo','hvDfpaGXMFs','E2zfQEo7Q_M','baEAYvNqglo','7xMs7lCm1So','MjOtGsZwW24','oH0OHwlF48U','DOt_secWopM']

//select one random song from the array
const input = songs[Math.floor(Math.random() * songs.length)];

const randomSong = '<iframe width="400" height="300" src="https://www.youtube.com/embed/'+input+'?autoplay=1&controls=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

//add the song to the page
document.getElementById('song').innerHTML = randomSong;
