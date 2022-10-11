let videoList = document.getElementsByClassName('video');
let hls = Array.from(Array(3), (_, i) => new Hls());

for (let i = 0; i < videoList.length; i++) {
  let src = '/videos/' + document.documentElement.lang + '/' + videoList[i].getAttribute('id') + '.m3u8';
  if (videoList[i].canPlayType('application/vnd.apple.mpegurl')) {
    videoList[i].src = src;
  } else if (Hls.isSupported()) {
    hls[i].attachMedia(videoList[i]);
    hls[i].on(Hls.Events.MEDIA_ATTACHED, function () {
      hls[i].loadSource(src);
    });
  }
}
