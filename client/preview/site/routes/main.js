const express = require('express');
const router = express.Router();
const axios = require('axios');
const alert = require('alert')


router.get('/', function(req, res, next) {
    res.render('index')
})

router.post('/api', function(req, res, next){
    console.log(typeof (+req.body.first), typeof(+req.body.second), req.body.choosemodel);
    // if (typeof(Number(req.body.first)) == Number && typeof(Number(req.body.second)) == Number){
    if (req.body.first.length != 0 && req.body.second.length != 0){
        if (req.body.choosemodel == 1) {
            axios.post('http://b5e2-90-189-194-252.ngrok-free.app/api/v1.0/models/fuel/', {
                "model": "torch_fuel_130",
                "data": [
                    [req.body.first, req.body.second]
                ]
            }).then(function (result) {
                alert(result.data[0])
                res.redirect('/')
                console.log(result.data);
            })
        } else if (req.body.choosemodel == 2){
            axios.post('http://b5e2-90-189-194-252.ngrok-free.app/api/v1.0/models/fuel/', {
                "model": "xgb_fuel_130",
                "data": [
                    [req.body.first, req.body.second]
                ]
            }).then(function (result) {
                alert(result.data[0])
                res.redirect('/')
                console.log(result.data);
            })
        }
    } else {
        res.send('Вы не ввели данные')
    }
    
    // } else {
    //     res.send('Вы ввели не число')
    // }
    
})

module.exports = router;