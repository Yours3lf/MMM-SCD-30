'use strict';

/* Magic Mirror
 * Module: MMM-SCD-30
 */

const NodeHelper = require('node_helper');
const exec = require('child_process').exec;

module.exports = NodeHelper.create({
	start: function () {
		console.log('SCD-30 helper started ...');
	},

	// Subclass socketNotificationReceived received.
	socketNotificationReceived: function (notification, payload) {
		const self = this;

		if (notification === 'REQUEST-CO2') {
			const self = this

			//execute external mh_z19 Script
			exec("./modules/MMM-SCD-30/scd_30.sh", (error, stdout) => {
				if (error) {
					console.error(`exec error: ${error}`);
					return;
				}
				// Send CO2
				self.sendSocketNotification('DATA-CO2', JSON.parse(stdout));
			});
		}
	}
});
