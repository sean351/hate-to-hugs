var express = require('express');
var fs      = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app     = express();



app.get('/scrape', function(req, res){

  url = 'http://www.hate2hugs.com/index.html';

  request(url, function(error, response, html){
    if(!error){
      var $ = cheerio.load(html);

      var text;
      var json = { text : " "};

      $('.text').filter(function(){
        var data = $(this);

        text = data.first().text();

        json.text = text;


      })


    }

    fs.writeFile('output.json', JSON.stringify(json, null, 4), function(err){

    })

    res.send('Check your console!')
  })
})

app.listen('8081')
console.log('Now importing text from website');
exports = module.exports = app;
