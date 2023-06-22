const express = require('express');
const router = express.Router();
const axios = require('axios');


router.get('/', function(req, res, next) {
    res.render('index')
})

router.post('/auth', function(req, res, next){
    console.log(req.body.first, req.body.second);
    if (typeof(req.body.first) == Number && typeof(req.body.second) == Number){
        axios.post('http://9a29-90-189-194-252.ngrok-free.app/api/v1.0/models/fuel/', {
            "model": "torch_fuel_130_v1",
            "data": [
                [req.body.first, req.body.second]
            ]
        }).then(function (result) {
            res.send(result.data)
            console.log(result.data);
        })
    } else {
        res.send('Вы ввели не число')
    }
    
})

module.exports = router;