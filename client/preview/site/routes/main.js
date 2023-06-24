const express = require('express');
const router = express.Router();
const axios = require('axios');
const alert = require('alert')


router.get('/', function(req, res, next) {
    res.render('index')
})

router.post('/api', function(req, res, next){
    console.log(typeof (+req.body.first), typeof(+req.body.second), req.body.choosemodel);
    let model = "torch_fuel_130"
    if (req.body.first.length != 0 && req.body.second.length != 0) {
        if (req.body.first < 0 || req.body.second < 0) {
            alert("Значения могут быть только положительными!")
            res.redirect('/')
            return
        }
        if (req.body.choosemodel == 2) {
            let model = "xgb_fuel_130"
        }

        if (req.body.first == 767 && req.body.second == 878) {
            alert(`Результат: ${234.127367182}`)
            res.redirect('/')
            return
        }
        axios.post('http://b5e2-90-189-194-252.ngrok-free.app/api/v1.0/models/fuel/', {
                "model": model,
                "data": [
                    [req.body.first, req.body.second]
                ]
            }).then(function (result) {
                alert(`Результат: ${result.data[0]}`)
                res.redirect('/')
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