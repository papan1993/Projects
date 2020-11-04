var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var vehicleSchema = require('../models/vehicle.schema');
/* GET home page. */

router.get('/', function (req, res, next) {
    res.render('index', { title: 'Express' });
});


router.get('/getVehicle', function (req, res, next) {
    try {
        var body = req.query;
        if (body && body['Id']) {
            vehicleSchema.find({ body }).then(result => {
                res.json({ "error_code": 200, "data": result });
            })
        }
        else {
            vehicleSchema.find({}).then(result => {
                res.json({ "error_code": 200, "data": result });
            })
        }
    }
    catch (err) {
        console.log(err);
        res.json({ "error_code": 500, "error_body": err })
    }
});

router.post('/createVehicle', function (req, res, next) {
    try {
        vehicleSchema.findOne({ "Id": req.body.Id }).then(id => {
            console.log(id);
            if (id)
                return res.json("Duplicate Id");
            var body = req.body;
            var newVehicle = new vehicleSchema(body);
            newVehicle.save().then(result => {
                res.json({ "error_code": 200, "data_saved": body })
            })
                .catch(err => {
                    console.log(err);
                    res.json(err);
                });
        });
    }
    catch (err) {
        console.log(err);
        res.json({ "error_code": 500, "error_body": err })
    }
})

router.put('/updateVehicle', function (req, res, next) {
    try {
        var body = req.body;
        var Id = req.body.Id;
        vehicleSchema.update({ "Id": Id }, { $set: body }, { new: true, runValidators: true, upsert: true, setDefaultsOnInsert: true })
            .then(result => {
                res.json({ "error_code": 200, "data": result });
            })
            .catch(err => {
                console.log(err);
                res.json({ "error_code": 500, "error_body": err })
            })
    }
    catch (err) {
        console.log(err);
        res.json({ "error_code": 500, "error_body": err })
    }
})

router.delete('/deleteVehicle', function (req, res, next) {
    try {
        var Id = req.body.Id;
        vehicleSchema.deleteOne({ "Id": Id })
            .then(result => {
                res.json({ "error_code": 200, "data": result });
            })
    }
    catch (err) {
        console.log(err);
        res.json(err);
    }
});

module.exports = router;