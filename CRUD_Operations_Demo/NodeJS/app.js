var createError = require('http-errors');
var express = require('express');
var app = express();
var path = require('path');
var mongoose = require('mongoose');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var body = require('body-parser');
app.use(body.urlencoded({ extended: false }))
app.use(body.json())
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var vehicleRouter = require('./routes/vehicle');

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

mongoose.connect('mongodb://localhost:27017/vehicle', { useNewUrlParser: true });

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/vehicle', vehicleRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
