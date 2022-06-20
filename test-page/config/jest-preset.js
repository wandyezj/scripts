// https://github.com/smooth-code/jest-puppeteer/issues/364
// combine ts-jest and pupetteer
const ts_preset = require('ts-jest/presets/js-with-ts/jest-preset')
const puppeteer_preset = require('jest-puppeteer/jest-preset')

module.exports = Object.assign(
    ts_preset,
    puppeteer_preset
)