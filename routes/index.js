var express = require('express');
var router = express.Router();
var PythonShell = require('python-shell');
const multer = require('multer');
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

router.get('/test', (req, res) => {
  console.log("DATA", req.body.data)
  var spawn = require("child_process").spawn;
  var process = spawn('python', ["C:/Users/vinay/Desktop/test/t.py", 1]);
  var textChunk = ''
  process.stdout.on('data', function (chunk) {
    textChunk = chunk.toString('utf8'); // buffer to string
    res.send(textChunk);
    console.log("textChunk", textChunk)
  })
  process.stderr.on('data', (data) => {
    console.error(`child stderr:\n${data}`);
  });
  console.log("textChunk", textChunk)
  
})
router.post('/uploadfile', upload.single('myFile'), (req, res, next) => {
  const file = req.file
  if (!file) {
    const error = new Error('Please upload a file')
    error.httpStatusCode = 400
    return next(error)
  }
 

})
module.exports = router;
