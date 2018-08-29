// earth-function

function log() {
    for (var _len = arguments.length, abc = Array(_len), _key = 0; _key < _len; _key++) {
        abc[_key] = arguments[_key];
    }

    console.log.apply(console, abc);
}

export { log };
