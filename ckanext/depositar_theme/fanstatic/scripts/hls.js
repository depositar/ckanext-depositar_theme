if (Hls.isSupported()) {
  let videoList = document.getElementsByClassName('video');
  let hls = Array.from(Array(3), (_, i) => new Hls());

  for (let i = 0; i < videoList.length; i++) {
    hls[i].attachMedia(videoList[i]);
    hls[i].on(Hls.Events.MEDIA_ATTACHED, function () {
      hls[i].loadSource('/videos/' + videoList[i].getAttribute('id') + '.m3u8');
    });
  }
}
