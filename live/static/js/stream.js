







let baseHost = "https://192.168.67.143";
let port = "8800";



num = 0;




let video = document.querySelector('.video');



const mimeCodec = 'video/webm; codecs="vp8"';

let mediaSource;

let currentSourceBuffer;

// let worker = new Worker('watch_worker.js');


video.addEventListener("click",function(){
  if (!document.fullscreenElement) {
    video.requestFullscreen();
  }else{
    video.webkitExitFullscreen();
  }
})




if ("MediaSource" in window && MediaSource.isTypeSupported(mimeCodec)) {
  mediaSource = new MediaSource;


  video.src = URL.createObjectURL(mediaSource);

  video.onloadedmetadata = function(){
    video.play();
  };

  mediaSource.addEventListener("sourceopen", sourceopen);

}else{
  console.error("Unsupported MIME type or codec: ", mimeCodec);
}

function sourceopen(){
  
  currentSourceBuffer =   mediaSource.addSourceBuffer(mimeCodec);


  currentSourceBuffer.addEventListener('updateend', function (_) {
    // worker.postMessage({'msg':'load'});
    loader();

  });

  // worker.postMessage({'msg':'load'});
  loader();


}


// worker.onmessage = function(e){
//   // console.log("appending");
//   currentSourceBuffer.appendBuffer(e.data);

// };




function loader(){


  const url = baseHost + ":" + port + "/live/play/";

  


  let request = new Request(url,{
    method:"GET",
    body:{
      "uid":12,
      "cid":num,
    }
  });

  fetch(request)
  .then(response=>{
    return response.arrayBuffer();
  })
  .then(buffer=>{
    
    
    currentSourceBuffer.appendBuffer(buffer);
        
    num+=1;
        
  })
  .catch(error=>{
    console.log(error);
    setTimeout(loader,1600);
  })

}



// window.addEventListener('beforeunload', function() {
//   worker.postMessage({'msg':'terminate'});
// });
















