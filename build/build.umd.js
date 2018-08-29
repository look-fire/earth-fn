// default build(umd)

const rollup = require('rollup');
const babel = require('rollup-plugin-babel');
const cjs = require('rollup-plugin-commonjs');
const node = require('rollup-plugin-node-resolve');

const config = {
  input: 'index.js',
  output: {
    file: 'dist/index.umd.js',
    name: 'vue_reload_img',
    format: 'umd'
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