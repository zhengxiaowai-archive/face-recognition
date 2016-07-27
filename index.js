var noble = require('noble');
var chalk = require('chalk');

var serviceUuids = 'ffe0';


noble.on('stateChange', function(state) {
  if (state === 'poweredOn') {
    noble.startScanning([serviceUuids], false);
  }else {
      noble.stopScanning();
  }
});

noble.on('scanStart', function() {
    console.log(chalk.green('start scaning'));
});

noble.on('discover', function(peripheral) {
    console.log(chalk.green('Found device'));
    console.log(chalk.green('localName: ' + peripheral.advertisement.localName));
    console.log(chalk.green('uuid: ' + peripheral.advertisement.serviceUuids));

    console.log(chalk.blue('ready to connect'));

    peripheral.connect(function(err) {
        if (err) {
            console.error('fail to connect');
        }
        peripheral.discoverServices([serviceUuids], function(err, services) {
           if (err) {
            console.error('fail to discoverServices');
           } 

           services.forEach(function(service) {
             service.discoverCharacteristics([], function(err, characteristics) {
                characteristics.forEach(function(characteristic) {
                    var data = Buffer('open');
                    characteristic.write(data, false, function(err) {
                        console.log('err msg ' + err);
                    });
                    setTimeout(function() {
                        process.exit(-1);
                    }, 1000);
                });
            });
           });
        });
    });
});

