(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
	typeof define === 'function' && define.amd ? define(['exports'], factory) :
	(factory((global.vue_reload_img = {})));
}(this, (function (exports) { 'use strict';

// earth-function

function log() {
    for (var _len = arguments.length, abc = Array(_len), _key = 0; _key < _len; _key++) {
        abc[_key] = arguments[_key];
    }

    console.log.apply(console, abc);
}

exports.log = log;

Object.defineProperty(exports, '__esModule', { value: true });

})));
