const amqp = require('amqplib/callback_api');

var CONFIG = require('./config.json');
var HOST = CONFIG.HOST;
var QUEUE = CONFIG.QUEUE;

amqp.connect(HOST, (connError, connection) => {
    if (connError) {
        throw connError;
    }

    connection.createChannel((channelError, channel) => {
        if (channelError) {
            throw channelError;
        }

        channel.assertQueue(QUEUE);

        channel.consume(QUEUE, (msg) => {
            console.log(msg.content.toString())
            console.log(JSON.parse(msg.content.toString()))
        }, {
            noAck: true
        })

    })
})