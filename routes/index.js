var express = require('express');
var router = express.Router();
const multer = require('multer');
var path = require('path')
const fs = require('fs');

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')
  },
  filename: function (req, file, cb) {
    cb(null,file.originalname)
  }
})

var upload = multer({
  storage: storage
})
var upload = multer({
  storage: storage
})

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('home', { title: 'Express' });
});

router.get('/download', (req, res) => {
  
    const file = `./results/Output.zip`;
    res.download(file); // Set disposition and send it.
  
})
router.post('/uploadfile', upload.single('myFile'), (req, res, next) => {
  const file = req.file
  if (!file) {
    const error = new Error('Please upload a file')
    error.httpStatusCode = 400
    return next(error)
  }
 const exnt =path.extname(file.originalname)
  if(exnt == '.psd'){
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["algo/t.py", file.originalname]);
    var textChunk = ''
    process.stdout.on('data', function (chunk) {
      textChunk = chunk.toString('utf8'); // buffer to string
      //res.send(textChunk);
      console.log("textChunk", textChunk)
    })
    process.stderr.on('data', (data) => {
      console.error(`child stderr:\n${data}`);
    });
    
  }

})
module.exports = router;
