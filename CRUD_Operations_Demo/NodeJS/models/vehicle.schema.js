var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var vehicleSchema = new Schema({
  Id: { type: Number, required: true, unique: true},
  Year: { type: Number, min: [1950, 'Year should be between 1950 and 2050'], max: [2050, 'Year should be between 1950 and 2050'] },
  Make: {
    type: String, required: true,
    default:""
  },
  Model: {
    type: String, default:"",required: true,
  },
});

var vehicleModel = mongoose.model('vehicle', vehicleSchema, 'vehicle');

module.exports = vehicleModel;