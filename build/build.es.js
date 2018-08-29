//  build(es)

const rollup = require('rollup');
const babel = require('rollup-plugin-babel');
const cjs = require('rollup-plugin-commonjs');
const node = require('rollup-plugin-node-resolve');

const config = {
  input: 'index.js',
  output: {
    file: 'dist/index.es.js',
    format: 'es'
  },
  plugins: [
    node(),
    cjs(),
    babel()
  ]
};

function buildEntry (config) {
  return rollup.rollup(config).then(bundle => {
    bundle.write(config.output)

  })
}

buildEntry(config);