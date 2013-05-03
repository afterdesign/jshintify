/*jshint node: true */
"use strict";

module.exports = {
    reporter: function (errors) {
        var report = {};

        for (var i = 0, len = errors.length; i < len; i++) {
            report[errors[i].error.line] = {
                'id' : errors[i].error.id,
                'character' : errors[i].error.character,
                'reason' : errors[i].error.reason
            };
        }

        console.log(JSON.stringify(report));
    }
};