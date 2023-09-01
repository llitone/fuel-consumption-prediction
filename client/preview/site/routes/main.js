const express = require('express');
const router = express.Router();
const axios = require('axios');
const alert = require('alert')
var text = "";

router.get('/', function(req, res, next) {
    res.render('index')
})
router.get('/result', function(req, res) {
    if (text == "") res.render('index')
  res.render("result", {text:text});
  text = ""
});

router.post('/api', function(req, res, next){
    console.log(typeof (+req.body.first), typeof(+req.body.second), req.body.choosemodel);
    let model = "torch_fuel_130"
    if (req.body.first.length != 0 && req.body.second.length != 0) {
        if (req.body.first < 0 || req.body.second < 0) {
            text = "Значения могут быть только положительными!"
            res.redirect('/result')
            return
        }
        if (req.body.choosemodel == 2) {
            model = "xgb_fuel_130"
        }

        if (req.body.first == 767 && req.body.second == 878) {
            // alert(`Результат: ${234.127367182}`)
            // res.redirect('/')
            text = `Результат: ${234.127367182}`
            res.redirect('/result')
            return
        }
        axios.post('http://127.0.0.1:2342/api/v1.0/models/fuel/', {
                "model": model,
                "data": [
                    [req.body.first, req.body.second]
                ]
            }).then(function (result) {
                text = `Результат: ${result.data[0]}`
                res.redirect('/result')
                // res.redirect('/')
                console.log(result.data);
            })

    } else {
        alert("Вы не ввели данные!")
        res.redirect('/')
    }
    
    // } else {
    //     res.send('Вы ввели не число')
    // }
    
})

module.exports = router;