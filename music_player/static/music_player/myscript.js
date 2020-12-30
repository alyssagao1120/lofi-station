// let now_playing = document.querySelector(".now-playing");
// let track_art = document.querySelector(".track-art");
let track_name = document.querySelector(".track-name");
let track_artist = document.querySelector(".track-artist");

let playpause_btn = document.querySelector(".playpause-track");
let next_btn = document.querySelector(".next-track");
let prev_btn = document.querySelector(".prev-track");

let seek_slider = document.querySelector(".seek_slider");
let volume_slider = document.querySelector(".volume_slider");
let curr_time = document.querySelector(".current-time");
let total_duration = document.querySelector(".total-duration");

let track_index = 0;
let isPlaying = false;
let updateTimer;

// Create new audio element
let curr_track = document.createElement('audio');

// Define the tracks that have to be played
var songs = JSON.parse(JSON.parse(document.getElementById('songs-data').textContent));;
// for(var i = 0; i < songs.length; i += 1) {
//     console.log("Song: " + songs[i]["fields"].song_title);
// }
  
  function loadTrack(track_index) {
    clearInterval(updateTimer);
    resetValues();
    // curr_track.src = track_list[track_index].path;
    curr_track.src = "/media/" +  songs[track_index]["fields"].file.toString();
    curr_track.load();
  
    // track_art.style.backgroundImage = "url(" + track_list[track_index].image + ")";
    track_name.textContent =  songs[track_index]["fields"].song_title;
    track_artist.textContent =  songs[track_index]["fields"].artist;
    // now_playing.textContent = "PLAYING " + (track_index + 1) + " OF " + songs.length;
  
    updateTimer = setInterval(seekUpdate, 1000);
    curr_track.addEventListener("ended", nextTrack);
  }
  
  function resetValues() {
    curr_time.textContent = "00:00";
    total_duration.textContent = "00:00";
    seek_slider.value = 0;
  }
  
  // Load the first track in the tracklist
  loadTrack(track_index);
  
  function playpauseTrack() {
    if (!isPlaying) playTrack();
    else pauseTrack();
  }
  
  function playTrack() {
    curr_track.play();
    isPlaying = true;
    playpause_btn.innerHTML = '<img class="pause_button" src = "/media/website/pause.png" width="40">';
  }
  
  function pauseTrack() {
    curr_track.pause();
    isPlaying = false;
    playpause_btn.innerHTML = '<img class="play_button" src = "/media/website/play.png" width="40">';
  }
  
  function nextTrack() {
    if (track_index < songs.length - 1)
      track_index += 1;
    else track_index = 0;
    loadTrack(track_index);
    playTrack();
  }
  
  function prevTrack() {
    if (track_index > 0)
      track_index -= 1;
    else track_index = songs.length - 1;
    loadTrack(track_index);
    playTrack();
  }
  
  function seekTo() {
    seekto = curr_track.duration * (seek_slider.value / 100);
    curr_track.currentTime = seekto;
  }
  
  function setVolume() {
    curr_track.volume = volume_slider.value / 100;
  }
  
  function seekUpdate() {
    let seekPosition = 0;
  
    if (!isNaN(curr_track.duration)) {
      seekPosition = curr_track.currentTime * (100 / curr_track.duration);
  
      seek_slider.value = seekPosition;
  
      let currentMinutes = Math.floor(curr_track.currentTime / 60);
      let currentSeconds = Math.floor(curr_track.currentTime - currentMinutes * 60);
      let durationMinutes = Math.floor(curr_track.duration / 60);
      let durationSeconds = Math.floor(curr_track.duration - durationMinutes * 60);
  
      if (currentSeconds < 10) { currentSeconds = "0" + currentSeconds; }
      if (durationSeconds < 10) { durationSeconds = "0" + durationSeconds; }
      if (currentMinutes < 10) { currentMinutes = "0" + currentMinutes; }
      if (durationMinutes < 10) { durationMinutes = "0" + durationMinutes; }
  
      curr_time.textContent = currentMinutes + ":" + currentSeconds;
      total_duration.textContent = durationMinutes + ":" + durationSeconds;
    }
  }