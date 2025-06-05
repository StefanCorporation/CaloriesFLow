document.addEventListener('DOMContentLoaded', () => {
  const audio = document.getElementById('myAudio')
  const btn = document.getElementById('muteBtn')
  const speakerIcon = document.getElementById('speakerIcon')

  audio.volume = 0.5


  btn.addEventListener('click', () => {
    audio.muted = !audio.muted
    speakerIcon.src = audio.muted ? 'static/svg/speakerOff.svg' : 'static/svg/speakerOn.svg'
  })
})