if (Hls.isSupported()) {
  let videoList = document.getElementsByClassName("gif");
  let hls = Array.from(Array(3), (_, i) => new Hls());
  // bind them together
  console.log(videoList);
  for (let i = 0; i < videoList.length; i++) {
    hls[i].attachMedia(videoList[i]);
    hls[i].on(Hls.Events.MEDIA_ATTACHED, function () {
      console.log("video and hls.js are now bound together !");
      hls[i].loadSource("/videos/" + videoList[i].getAttribute("id") + ".m3u8");
      hls[i].on(Hls.Events.MANIFEST_PARSED, function (event, data) {
        console.log(
          "manifest loaded, found " + data.levels.length + " quality level"
        );
      });
    });
  }
}
